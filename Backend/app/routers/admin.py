from flask import Blueprint, request, jsonify, current_app
from flask_restx import Api, Resource
from ..utils.segurity import descodificarPassword, codificarPassword, codificarToken, descodificarToken
import os
from datetime import datetime , timedelta
from ..routers.auth import api
from ..models.models import User, db, Turn, Services

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
    @admin.doc(
        description="Ver Pacientes.",
        params={
            'token': 'Token del Admin',
        },
    )
    def get(self):
        """
        Obtener La Lista de Pacientes *
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
# Esta Ruta No se esaba viendo o vizualizando
@admin.route("/paciente/<int:id>")
@admin.doc(
        description="Ver un Paciene .",
        params={
            'Authorization': {'token': 'El token de acceso del usuario.', 'required': True}
        }
    )
class GETPaciente(Resource):
    def get(self, id):
        """
        Ver Detalles del Paciente de Forma Individual * (Estaba Oculto ya fue reparado, Ojo Con usar dos veces el nombre de la Classes )
        """
        auth = request.headers.get('Authorization')

        if not auth:
            return jsonify({'message': "Token no proporcionado"})

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

    def put(self, id):
        """
        Modifica el usuario para suspenderlo *
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
            paciente = User.query.filter_by(use_int_id=id).first()
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
#    def delete(self,id):
#        """
#        Eliminar Paciente (para revisar)
#        """
#        auth = request.headers.get('Authorization')

#        if not auth:
#            return jsonify({'message': "Token no proporcionado"})

#        datosToken = descodificarToken(auth)
#        token_id = datosToken.get('id')
 #       role = datosToken.get('role')

#        try:
#            # Verificar si el usuario tiene permiso para eliminar pacientes
#            user = User.query.filter_by(use_int_id=token_id, use_str_role=role).first()
#            if not user:
#                return jsonify({'message': 'No estás autorizado'})
#
#            # Buscar al paciente por su ID
#            paciente = User.query.filter_by(use_int_id=id).first()
#            if not paciente:
#                return jsonify({'message': 'Paciente no encontrado'})
#
#            citas = Turn.query.filter_by(turn_int_client_id=id).all()
#            for cita in citas:
#                db.session.delete(cita)

#            db.session.delete(paciente)
#            db.session.commit()

#            return jsonify({'message': 'Datos del Paciente eliminados correctamente'})

#        except Exception as e:
#            return jsonify({'message': str(e)}), 500
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
                    #'user_id': turno.turn_int_user_id,
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
#Lista de Turnos Asignados
#NOTA este End Point deberia de usar paginacion y cuidado con usar el mismo nombre de otra clase existente,
#Se preseno un Caso que se Ocutaban algunos EndPoints por ejemplo ver paciente por Id. Ya se reparo
@admin.route("/turnos/assigned")
class Turnos(Resource):
    def get(self):
        """
        Obtener Listado de Turnos ASIGNADOS
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

            turnos = Turn.query.filter_by(turn_bol_assigned=True).paginate(page=page, per_page=per_page, error_out=False)
            #

            lista_turno = []
            for turno in turnos.items:
                service_description = None
                if turno.service:
                    service_description = turno.service.ser_str_category_name

                formatted_turno = {
                    'id': turno.turn_int_id,
                    'service_info': {
                        'idservice': turno.service_id,
                        'service_description': service_description
                    },
                    'paciente': turno.turn_int_user_id,
                    'name': turno.turn_str_name_turn,
                    'description': turno.turn_str_description,
                    'creation_date': turno.turn_date_creation_date,
                    'date_assignment': turno.turn_date_date_assignment.strftime('%Y-%m-%d %H:%M:%S'),
                    'start_turn': str(turno.turn_time_start_turn),
                    'finish_turn': str(turno.turn_time_finish_turn),
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
        Maneja las solicitudes POST para crear un nuevo turno*.

        Solicitud:
        - Cabeceras:
            - Authorization: Token para la autenticación.
        - Carga útil JSON:
            - fecha (str): Fecha en formato 'AAAA-MM-DD'.
            - inicio (str): Hora de inicio en formato 'HH:MM'.
            - fin (str): Hora de finalización en formato 'HH:MM'.
            - duracion (int): Duración de cada turno en minutos.

        Retorna:
        - Respuesta JSON:
            - message: Indica el resultado de la operación.

        Descripción:
        Este punto final crea nuevos turnos basados en los datos proporcionados en la carga útil JSON. Requiere
        autenticación a través de la cabecera 'Authorization'. Extrae el ID de usuario del token obtenido del encabezado
        de autorización. Procesa la carga útil JSON para extraer la fecha, hora de inicio, hora de finalización y duración
        de cada turno. Luego, intenta crear nuevas entradas de turno en la base de datos. Si ya existen turnos para la
        fecha proporcionada, devuelve un mensaje indicando que ya existen entradas para esa fecha. De lo contrario, crea
        nuevas entradas de turno con los parámetros especificados y guarda los cambios en la base de datos.
        """
        auth = request.headers.get('Authorization')
        if not auth:
            return jsonify({"message": "Token no proporcionado"})

        datostoken = descodificarToken(auth)
        id = datostoken.get('id')

        data = request.get_json()
        fecha_j = data.get('fecha')
        fecha = datetime.strptime(fecha_j, '%Y-%m-%d').date()
        inicio_j = data.get('inicio')
        inicio = datetime.strptime(inicio_j, '%H:%M').time()
        fin_j = data.get('fin')
        fin = datetime.strptime(fin_j, '%H:%M').time()
        duracion = int(data.get('duracion'))

        try:
            hoy = datetime.now().date()

            consulta = Turn.query.filter_by(turn_date_date_assignment=fecha).first()

            if consulta:
                return jsonify({'message': 'Ya hay datos en la tabla para esta fecha'})
            else:
                hora_inicio_turnos = inicio
                while hora_inicio_turnos < fin:
                    hora_fin_turno = datetime.combine(datetime.min, hora_inicio_turnos) + timedelta(minutes=duracion)
                    hora_fin_turno = hora_fin_turno.time()

                    new_turn = Turn(
                        turn_int_user_id=id,# Esta linea si se quita entonces no es necesario que todos los turnos se le asignen al admin ,deberia de quitarse
                        turn_date_creation_date=hoy,
                        turn_date_date_assignment=fecha,
                        turn_time_start_turn=hora_inicio_turnos,
                        turn_time_finish_turn=hora_fin_turno,
                        turn_bol_assigned=False
                    )

                    hora_inicio_turnos = hora_fin_turno
                    db.session.add(new_turn)

                db.session.commit()
                return jsonify({'message': 'Turnos habilitados exitosamente'})

        except Exception as e:
            print("Error:", e)
            return jsonify({"message": "Error en el servidor"})
        """
        Crear un nuevo turno

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
"""

###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
# Obtener Detalles de un turno , actualizarlo y Borrarlo
@admin.route("/turnos/<int:id>")
class TurnoCrear(Resource):
    @admin.doc(
        description=" Ver y acualizar Turno",
        params={
            'token': 'Token del Admin'
        },
    )
    def get(self, id):
        """
        Obtener detalles de un turno por su ID *
        """
        auth = request.headers.get('Authorization')

        if not auth:
            return jsonify({'message': "Token no proporcionado"})

        datosToken = descodificarToken(auth)
        token_id = datosToken.get('id')
        role = datosToken.get('role')

        try:
            if role != 'Admin':
                return jsonify({'message': 'No Estas Autorizado'})

            turno = Turn.query.filter_by(turn_int_id=id).first()
            if not turno:
                return jsonify({'message': 'Turno no encontrado'})

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
            })

        except Exception as e:
            return jsonify({'message': str(e)})
###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
    @admin.doc(
        description=" Ver y acualizar Turno",
        params={
            'token': 'Token del Admin',
            'paciente_id': 'id del Paciente',
            'servicio_id': 'id de servicio',
        },
    )
    def put(self, id):
        """
        Actualizar un turno existente por su ID *
        """
        auth = request.headers.get('Authorization')
        data = request.get_json()
        paciente_id = data.get("pacienteId")
        servicio_id = data.get("servicio")

        if not auth:
            return jsonify({'message': "Token no proporcionado"})

        datos_token = descodificarToken(auth)
        token_id = datos_token.get('id')
        role = datos_token.get('role')

        try:
            if role != 'Admin':
                return jsonify({'message': 'No Estás Autorizado'})

            # Buscar el turno en la base de datos
            turno = Turn.query.get(id)
            if not turno:
                return jsonify({'message': 'Turno no encontrado'})

            # Actualizar los campos del turno con los datos proporcionados
            if paciente_id is not None:
                turno.turn_int_user_id = paciente_id
            if servicio_id is not None:
                turno.service_id = servicio_id

            # Guardar los cambios en la base de datos
            db.session.commit()

            return jsonify({'message': 'Turno actualizado correctamente'})

        except Exception as e:
            return jsonify({'message': str(e)})
###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
    def delete(self, id):
        """
        Eliminar un turno por su ID *
        """
        auth = request.headers.get('Authorization')

        if not auth:
            return jsonify({'message': "Token no proporcionado"})

        datosToken = descodificarToken(auth)
        token_id = datosToken.get('id')
        role = datosToken.get('role')

        try:
            if role != 'Admin':
                return jsonify({'message': 'No Estas Autorizado'})

            # Buscar el turno en la base de datos
            turno = Turn.query.get(id)
            if not turno:
                return jsonify({'message': 'Turno no encontrado'})

            # Eliminar el turno de la base de datos
            db.session.delete(turno)
            db.session.commit()

            return jsonify({'message': 'Turno eliminado correctamente'})

        except Exception as e:
            return jsonify({'message': str(e)})
###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
#End Point Servicio
@admin.route("/servicios")
class Servicios(Resource):
    def get(self):
        """
        Obtiene un listado paginado de servicios disponibles *.

        Retorna:
        - Si la solicitud es exitosa, devuelve un listado paginado de servicios como JSON con un código de estado 200.
        - Si no se proporciona un token de autorización, devuelve un mensaje de error con un código de estado 400.
        - Si el usuario no está autorizado como administrador, devuelve un mensaje de error con un código de estado 403.
        - Si ocurre un error interno, devuelve un mensaje de error con un código de estado 500.
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

            servicios = Services.query.paginate(page=page, per_page=per_page, error_out=False)
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
@admin.route("/servicios")
class POSTServicios(Resource):
    @admin.doc(
        description="Crear Servicio.",
        params={
            'token': 'Token del Admin',
            'name': 'Nombre del Servicio'
        },
    )
    def post(self):
        """
        Crear Servicio *
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
