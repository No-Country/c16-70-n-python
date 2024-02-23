from flask import Blueprint, request, jsonify, current_app
from flask_restx import Api, Resource
from ..utils.segurity import descodificarPassword, codificarPassword, codificarToken, descodificarToken
import os
from datetime import datetime , timedelta
from ..routers.auth import api
from ..models.models import User, db, Turn, Services , Generador_turn

fecha_suspension = datetime.now()

admi = Blueprint("admin", __name__)

admin = api.namespace("admin", description="Rutas administrativas")

###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
#Mostrar lista de Pacientes
@admin.route("/pacientes")
class PacientesAll(Resource):

    def get(self):
        """ 
        Obtener Listado de Paciente 
        Ejemplo: http://127.0.0.1/admin/pacientes?page=1

        """
        auth = request.headers.get('Authorization')

        if not auth:
            return jsonify({'message': "Token no proporcionado"})


        datosToken = descodificarToken(auth)
        id = datosToken.get('id')
        role = datosToken.get('role')


        try:
            if role != 'Admin':
                return jsonify({'message': 'No Estas Autorizado'})
        
            # Paginacion
            page = request.args.get('page', 1, type=int)
            per_page = request.args.get('per_page', 10, type=int)

            exitsAdmin = User.query.filter_by(use_int_id=id, use_str_role=role).first()

            if exitsAdmin is None:
                return jsonify({'message':'No estás autorizado'})

            users = User.query.paginate(page=page, per_page=per_page, error_out=False)
            #

            formatted_users = []
            for user in users.items:
                formatted_user = {
                    'id': user.use_int_id,
                    'email': user.use_str_email,
                    'first_name': user.use_str_first_name,
                    'last_name': user.use_str_last_name,
                    'phone': user.use_str_phone,
                    'profile_img': user.use_str_profile_img,
                    'register_date': user.use_date_register_date.strftime('%Y-%m-%d %H:%M:%S'),
                    'suspension': user.use_bol_suspension,
                    'suspension_date': user.use_date_suspension_date.strftime('%Y-%m-%d %H:%M:%S') if user.use_date_suspension_date else None,
                    'role': user.use_str_role
                }
                formatted_users.append(formatted_user)

            return jsonify(formatted_users)
        except Exception as e:
            return jsonify({'message': str(e)})

###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
#Detalles de un cliente, Actualizar y Borrar
@admin.route("/paciente/<int:id>")
@admin.doc(
        description="Para ruta Dinamicas .",
        params={
            'Authorization': {'description': 'El token de acceso del usuario.', 'type': 'string', 'required': True}
        }
    )
class PacientesAll(Resource):
    def get(self, id):
        """ 
        Ver Detalles del Paciente de Forma Individual
        ejempo : http://127.0.0.1/admin/paciente/1
        """
        auth = request.headers.get('Authorization')
        
        if not auth:
            return jsonify({'message': "Token no proporcionado"}), 401
    
        datosToken = descodificarToken(auth)
        token_id = datosToken.get('id')
        role = datosToken.get('role')

        try:
            # Verificar si el usuario tiene permiso para acceder a la información del paciente
            user = User.query.filter_by(use_int_id=token_id, use_str_role=role).first()
            if not user:
                return jsonify({'message': 'No estás autorizado'}), 403
            
            # Buscar al paciente por su ID
            paciente = User.query.get(id)
            if not paciente:
                return jsonify({'message': 'Paciente no encontrado'}), 404
            
            return jsonify({
                'id': paciente.use_int_id,
                'email': paciente.use_str_email,
                'first_name': paciente.use_str_first_name,
                'last_name': paciente.use_str_last_name,
                'phone': paciente.use_str_phone,
                'img': paciente.use_str_profile_img,
                'data_reister': paciente.use_date_register_date,
                'suspension': paciente.use_bol_suspension,
                'data_suspension': paciente.use_date_suspension_date,
                'role': paciente.use_str_role
            })
            
        except Exception as e:
            return jsonify({'message': str(e)})
###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
@admin.route("/paciente/<int:id>")
@admin.doc(
        description="Para ruta Dinamicas",
        params={
            'Authorization': {'description': 'El token de acceso del usuario.', 'type': 'string', 'required': True},
            'Suspender': {'description':'se debe enviar True o False'}
        }
    )
class PacientesAll(Resource):
    def put(self, id):
        """ 
        Suspender : 'True' o 'False'
        ejempo : http://127.0.0.1/admin/paciente/1
        """
        auth = request.headers.get('Authorization')
        data = request.get_json()
        suspender = data.get("suspender")
        
        if not auth:
            return jsonify({'message': "Token no proporcionado"})

        if not data:
            return jsonify({'message': "Datos no proporcionados en formato JSON"})


        datosToken = descodificarToken(auth)
        token_id = datosToken.get('id')
        role = datosToken.get('role')

        try:
            # Verificar si el usuario tiene permiso para acceder a la información del paciente
            user = User.query.filter_by(use_int_id=token_id, use_str_role=role).first()
            if not user:
                return jsonify({'message': 'No estás autorizado'})
            
            # Buscar al paciente por su ID
            paciente = User.query.get(id)
            if not paciente:
                return jsonify({'message': 'Paciente no encontrado'})

            if suspender in ['True', 'False']:
                paciente.use_bol_suspension = suspender == 'True'
                paciente.use_date_suspension_date = datetime.now() if suspender == 'True' else None

                db.session.commit()
            
                return jsonify({'message': 'Cliente actualizado'})
        
        except Exception as e:
            return jsonify({'message': str(e)})
###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
    def delete(self,id):
        """ 
        Eliminar Paciente
        """
        auth = request.headers.get('Authorization')
    
        if not auth:
            return jsonify({'message': "Token no proporcionado"})

        datosToken = descodificarToken(auth)
        token_id = datosToken.get('id')
        role = datosToken.get('role')

        try:
            # Verificar si el usuario tiene permiso para eliminar pacientes
            user = User.query.filter_by(use_int_id=token_id, use_str_role=role).first()
            if not user:
                return jsonify({'message': 'No estás autorizado'})
        
            # Buscar al paciente por su ID
            paciente = User.query.get(id)
            if not paciente:
                return jsonify({'message': 'Paciente no encontrado'})

            citas = Turn.query.filter_by(turn_int_client_id=id).all()
            for cita in citas:
                db.session.delete(cita)

            db.session.delete(paciente)
            db.session.commit()
        
            return jsonify({'message': 'Datos del Paciente eliminados correctamente'})
    
        except Exception as e:
            return jsonify({'message': str(e)}), 500
###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################

#Lista de Turnos 
@admin.route("/turnos")
class Turnos(Resource):
    def get(self):
        """ 
        Obtener Listado de Turnos
        Ejemplo: http://127.0.0.1:40709/admin/turnos?page=1

        """
        auth = request.headers.get('Authorization')

        if not auth:
            return jsonify({'message': "Token no proporcionado"})


        datosToken = descodificarToken(auth)
        id = datosToken.get('id')
        role = datosToken.get('role')


        try:
            if role != 'Admin':
                return jsonify({'message': 'No Estas Autorizado'})
        
            # Paginacion
            page = request.args.get('page', 1, type=int)
            per_page = request.args.get('per_page', 10, type=int)

            exitsAdmin = User.query.filter_by(use_int_id=id, use_str_role=role).first()

            if exitsAdmin is None:
                return jsonify({'message':'No estás autorizado'})

            turnos = Turn.query.paginate(page=page, per_page=per_page, error_out=False)
            #

            lista_turno = []
            for turno in turnos.items:
                formatted_turno = {
                    'id': turno.turn_int_id,
                    'service_id': turno.service_id,
                    'user_id': turno.turn_int_user_id,
                    'name': turno.turn_str_name_turn,
                    'description': turno.turn_str_description,
                    'creation_date': turno.turn_date_creation_date,
                    'date_assignment': turno.turn_date_date_assignment.strftime('%Y-%m-%d %H:%M:%S'),
                    'start_turn': turno.turn_time_start_turn,
                    'finish_turn': turno.turn_time_finish_turn('%Y-%m-%d %H:%M:%S'),
                    'bol_assigned': turno.turn_bol_assigned
                }
                lista_turno.append(formatted_turno)

            return jsonify(lista_turno)
        except Exception as e:
            return jsonify({'message': str(e)})
###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
#crear turno
@admin.route("/turnos")
class TurnoCrear(Resource):
    def post(self):
        """
        Crear un nuevo turno
        """
        auth = request.headers.get('Authorization')
        data = request.get_json()
        
        service_id = data.get("service_id")
        user_id = data.get("user_id")
        name = data.get("name")
        description = data.get("description")
        start_time = data.get("start_time")
        end_time = data.get("end_time")

        if not auth:
            return jsonify({'message': "Token no proporcionado"}), 401

        try:

            if not all([service_id, user_id, start_time, end_time]):
                return jsonify({'message': "Datos incompletos"})

            new_turn = Turn(
                service_id=service_id,
                turn_int_user_id=user_id,
                turn_str_name_turn=name,
                turn_str_description=description,
                turn_time_start_turn=start_time,
                turn_time_finish_turn=end_time,
                turn_date_creation_date=datetime.now(),
                turn_date_date_assignment=datetime.now(),
                turn_bol_assigned=False
            )

            db.session.add(new_turn)
            db.session.commit()

            return jsonify({'message': 'Turno creado correctamente'})

        except Exception as e:
            return jsonify({'message': str(e)})


###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
# Obtener Detalles de un turno , actualizarlo y Borrarlo
@admin.route("/turnos/<int:id>")
class TurnoCrear(Resource):
    def get(self, id):
        """
        Obtener detalles de un turno por su ID
        """
        auth = request.headers.get('Authorization')

        if not auth:
            return jsonify({'message': "Token no proporcionado"}), 401

        datosToken = descodificarToken(auth)
        token_id = datosToken.get('id')
        role = datosToken.get('role')

        try:
            if role != 'Admin':
                return jsonify({'message': 'No Estas Autorizado'}), 403
        
            turno = Turn.query.get(id)
            if not turno:
                return jsonify({'message': 'Turno no encontrado'}), 404

            # Aquí puedes formatear la información del turno como desees
            return jsonify({
                'id': turno.turn_int_id,
                'service_id': turno.service_id,
                'user_id': turno.turn_int_user_id,
                'name': turno.turn_str_name_turn,
                'description': turno.turn_str_description,
                'start_time': str(turno.turn_time_start_turn),
                'end_time': str(turno.turn_time_finish_turn),
                'assigned': turno.turn_bol_assigned
            }), 200

        except Exception as e:
            return jsonify({'message': str(e)}), 500
###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
    def put(self, id):
        """
        Actualizar un turno existente por su ID
        """
        auth = request.headers.get('Authorization')

        if not auth:
            return jsonify({'message': "Token no proporcionado"}), 401

        datosToken = descodificarToken(auth)
        token_id = datosToken.get('id')
        role = datosToken.get('role')

        try:
            if role != 'Admin':
                return jsonify({'message': 'No Estas Autorizado'}), 403

            # Aquí puedes obtener los datos actualizados del turno desde la solicitud JSON
            data = request.get_json()

            # Buscar el turno en la base de datos
            turno = Turn.query.get(id)
            if not turno:
                return jsonify({'message': 'Turno no encontrado'}), 404

            # Actualizar los campos del turno con los datos proporcionados
            # Por ejemplo:
            turno.turn_str_name_turn = data.get('name', turno.turn_str_name_turn)
            turno.turn_str_description = data.get('description', turno.turn_str_description)
            # Actualiza los demás campos según sea necesario

            # Guardar los cambios en la base de datos
            db.session.commit()

            return jsonify({'message': 'Turno actualizado correctamente'}), 200

        except Exception as e:
            return jsonify({'message': str(e)}), 500
###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
    def delete(self, id):
        """
        Eliminar un turno por su ID
        """
        auth = request.headers.get('Authorization')

        if not auth:
            return jsonify({'message': "Token no proporcionado"}), 401

        datosToken = descodificarToken(auth)
        token_id = datosToken.get('id')
        role = datosToken.get('role')

        try:
            if role != 'Admin':
                return jsonify({'message': 'No Estas Autorizado'}), 403

            # Buscar el turno en la base de datos
            turno = Turn.query.get(id)
            if not turno:
                return jsonify({'message': 'Turno no encontrado'}), 404

            # Eliminar el turno de la base de datos
            db.session.delete(turno)
            db.session.commit()

            return jsonify({'message': 'Turno eliminado correctamente'}), 200

        except Exception as e:
            return jsonify({'message': str(e)}), 500
###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
#End Point Servicio
@admin.route("/servicios")
class Servicios(Resource):
    def get(self):
        """ 
        Obtener Listado de Servicios
        Ejemplo: http://127.0.0.1:40709/admin/servicios?page=1

        """
        auth = request.headers.get('Authorization')

        if not auth:
            return jsonify({'message': "Token no proporcionado"})


        datosToken = descodificarToken(auth)
        id = datosToken.get('id')
        role = datosToken.get('role')


        try:
            if role != 'Admin':
                return jsonify({'message': 'No Estas Autorizado'})
        
            # Paginacion
            page = request.args.get('page', 1, type=int)
            per_page = request.args.get('per_page', 10, type=int)

            exitsAdmin = User.query.filter_by(use_int_id=id, use_str_role=role).first()

            if exitsAdmin is None:
                return jsonify({'message':'No estás autorizado'})

            servicios = Servicios.query.paginate(page=page, per_page=per_page, error_out=False)
            #

            lista_servicio = []
            for servicio in servicios.items:
                formatted_turno = {
                    'id': servicio.ser_int_id,
                    'name': servicio.ser_str_category_name
                }
                lista_servicio.append(formatted_turno)

            return jsonify(lista_servicio)
        except Exception as e:
            return jsonify({'message': str(e)})
###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
    # Crear Servicio
    def post(self):
        """ 
        Crear Servicio
        """
        auth = request.headers.get('Authorization')
        data = request.get_json()
        name = data.get("name")

        if not auth:
            return jsonify({'message': "Token no proporcionado"})


        datosToken = descodificarToken(auth)
        id = datosToken.get('id')
        role = datosToken.get('role')


        try:
            if role != 'Admin':
                return jsonify({'message': 'No Estas Autorizado'})
        
            exitsAdmin = User.query.filter_by(use_int_id=id, use_str_role=role).first()

            if exitsAdmin is None:
                return jsonify({'message':'No estás autorizado'})

            existing_service = Services.query.filter_by(ser_str_category_name=name).first()
            if existing_service:
                return jsonify({'message': 'Ya existe un servicio con este nombre'})


            new_servicio = Services(ser_str_category_name=name)
            db.session.add(new_servicio)
            db.session.commit()

            return jsonify({'message':'El Servicio Fue Creado'})
        except Exception as e:
            return jsonify({'message': str(e)})



#########################################################################################################################################################################################################################################################################################################esto es lo que estoy agregando para revisar
        
@admin.route("/turnosgenerador")
class Turnos(Resource):
    def post(self):
        """
        Registrar la configuracion para generar disponiblidad de turnos
        """
        auth = request.headers.get('Authorization')
        if not auth:
            return jsonify({"message": "Token no proporcionado"})
        datostoken = descodificarToken(auth)
        id = datostoken.get('id')

        data = request.get_json()
        fecha = data.get('fecha')
        inicio = data.get('inicio_dispo')
        fin = data.get('fin_dispo')
        duracion = data.get('duracion_turnos')

        try:
            fecha_objeto = datetime.strptime(fecha, '%Y-%m-%d')
            hoy = datetime.now().date()

            consulta = Turn.query.filter_by(turn_date_creation_date=fecha).first()

            if consulta:
                return jsonify({'message': 'Ya hay datos en la tabla para esta fecha'})
            else:
                hora_inicio_turnos = datetime.strptime(inicio, '%H:%M').time()
                while hora_inicio_turnos < datetime.strptime(fin, '%H:%M').time():
                    hora_fin_turno = datetime.combine(datetime.min, hora_inicio_turnos) + timedelta(minutes=duracion)

                    new_turn = Turn(turn_int_user_id=id,
                                    turn_date_creation_date=hoy,
                                    turn_time_start_turn=hora_inicio_turnos.strftime('%H:%M'),
                                    turn_time_finish_turn=hora_fin_turno.time().strftime('%H:%M'),
                                    turn_bol_assigned=False)

                    hora_inicio_turnos = hora_fin_turno.time()
                    db.session.add(new_turn)

                db.session.commit()
                return jsonify({'message': 'Configuración de turnos registrada correctamente'})

        except Exception as e:
            print("Error:", e)
            return jsonify({"message": "Error en el servidor"})


        except Exception as e:
            print("Error:", e)
            return jsonify({"message": "Error En el Servidor"})
