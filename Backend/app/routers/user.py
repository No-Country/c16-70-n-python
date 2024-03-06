from flask_restx import Resource
from flask import Blueprint, jsonify, request
from .auth import api
from ..models.models import User, db, Turn, Services
from ..utils.segurity import verify_token
from datetime import datetime , date

users = Blueprint("user", __name__)
user = api.namespace("user", description="Rutas User")


# [X] MARCOS
# Para que el usuario vea sus datos
@user.route('/get')
class GetUserDataById(Resource):
    #@app.errorhandler(200, 404, 500)
    def get(self):
        """
        Obtiene los datos de un usuario *

        Parámetros:
        -----------
        No recibe parámetros directamente de la solicitud.

        Retorna:
        --------
        jsonify:
            Un JSON que contiene los siguientes datos del usuario si se encuentra:
            - user_id: int
                El ID del usuario.
            - email: str
                El correo electrónico del usuario.
            - firstname: str
                El primer nombre del usuario.
            - lastname: str
                El apellido del usuario.
            - phone: str
                El número de teléfono del usuario.
            - profile_image: str
                La URL de la imagen de perfil del usuario.
            - register_date: str
                La fecha de registro del usuario (en formato 'YYYY-MM-DD').
            - suspension_date: str
                La fecha de suspensión del usuario (en formato 'YYYY-MM-DD').
            - status: bool
                El estado de suspensión del usuario (True si está suspendido, False si no lo está).

            Un mensaje de error si el usuario no se encuentra o si ocurre algún problema durante la operación.

        """
        verify_token()
        id = verify_token().get('id')

        try:
            user = User.query.get(id)
            if user is None:
                return jsonify({'error': 'Usuario no encontrado'})
            user_data = {
                    'user_id': user.use_int_id,
                    'email': user.use_str_email,
                    'firstname': user.use_str_first_name,
                    'lastname': user.use_str_last_name,
                    'phone': user.use_str_phone,
                    'profile_image': user.use_str_profile_img,
                    'register_date': user.use_date_register_date,
                    'status': user.use_bol_suspension,
                    'suspension_date': user.use_date_suspension_date,
                }
            return jsonify(user_data)
        except Exception as e:
            return jsonify({'message': 'Error en la operacion'})

#FERNANDO
# EndPoint para que el usuario pueda editar sus Datos
@user.route('/put')
class PutDatosUser(Resource):
    def put(self):
        """
        Actualiza los datos de un usuario *
        Parámetros:
        -----------
        No recibe parámetros directamente de la solicitud.
        Los datos para actualizar se envían en formato JSON en el cuerpo de la solicitud. Se espera que el JSON contenga los siguientes campos:

        - email: str
            El nuevo correo electrónico del usuario.
        - firstname: str
            El nuevo nombre (o primer nombre) del usuario.
        - lastname: str
            El nuevo apellido (o apellido) del usuario.
        - phone: str
            El nuevo número de teléfono del usuario.
        - suspension_date: str
            La nueva fecha de suspensión del usuario (en formato de fecha, por ejemplo, 'YYYY-MM-DD'). Puede estar vacía si el usuario no está suspendido.

        Retorna:
        --------
        jsonify:
            Un mensaje de éxito si la actualización fue exitosa.
            Un mensaje de error si ocurrió algún problema durante la actualización.

        """
        #solicito el token
        verify_token()
        id = verify_token().get('id')

        try:
            user = User.query.get(id)
            if user:
                data = request.get_json()
                user.use_str_email = data.get('email')
                user.use_str_first_name = data.get('firstname')
                user.use_str_last_name = data.get('lastname')
                user.use_str_phone = data.get('phone')

                suspension_date = data.get('suspension_date')
                if suspension_date:
                    user.use_date_suspension_date = suspension_date
                    user.use_bol_suspension = True
                else:
                    user.use_date_suspension_date = None
                    user.use_bol_suspension = False

                db.session.commit()
                return jsonify({"message": "Usuario actualizado correctamente"})
            else:
                return jsonify({'error': 'Usuario no encontrado'}), 404
        except Exception as e:
            print("Error:", e)
            return jsonify({"message": "Error al actualizar el usuario"})

###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
# [] MARCOS
# Actualizar su imagen
@user.route('/img')
class PutImgUser(Resource):
    def put(self):
        """
        Actualiza Imagen de Perfil *
        """
        #Solicitud de Token por el headers
        verify_token()
        img = request.files['img']
        id = verify_token().get('id')
        role = verify_token().get('role')

        try:
            # Verificar el rol del usuario
            if role == 'Admin' or role == 'Paciente':

                    user = User.query.filter_by(use_int_id=id, use_str_role=role).first()

                    if not user:
                        return jsonify({"message": "Usuario no encontrado"})
                    # Guardar la imagen para el cliente
                    user.save_use_str_profile_img(img)

                    return jsonify({"message": "Imagen de perfil actualizada correctamente"})

            else:
                return jsonify({"message": "Rol de usuario desconocido"})

        except Exception as e:
            print("Error:", e)
            return jsonify({"message": "Error al conectarse con la BD"})



#FERNANDO
#Listado de Turnos Disponibles
@user.route('/turnos')
class TurnosGet(Resource):
    def get(self):
        """
        Obtiene los turnos no asignados cuya fecha de asignación es posterior al día actual *.
        paginando, ejemplo:
        /user/turnos?page=1

        Retorna:
        --------
        jsonify:
            Devuelve una lista de objetos JSON que representan los turnos disponibles.
            Cada objeto JSON contiene la información de un turno no asignado.

            Los campos de cada objeto JSON incluyen:
            - idturn: int
                El ID único del turno.
            - idservice: int
                El ID del servicio al que pertenece el turno.
            - nameturn: str
                El nombre del turno.
            - descriptionturn: str
                La descripción del turno.
            - creationdate: str
                La fecha de creación del turno en formato 'YYYY-MM-DD'.
            - assigmentturn: str
                La fecha de asignación del turno en formato 'YYYY-MM-DD'.
            - turn_start: str
                La hora de inicio del turno en formato 'HH:MM:SS'.
            - turn_finish: str
                La hora de finalización del turno en formato 'HH:MM:SS'.

            Si hay un error al conectarse con la base de datos, se devuelve un mensaje de error JSON.
        """
        auth = request.headers.get('Authorization')

        if not auth:
            return jsonify({'message': "Token no proporcionado"})

        try:
            hoy = date.today()
            # Paginacion
            page = request.args.get('page', 1, type=int)
            per_page = request.args.get('per_page', 10, type=int)

            turnos = Turn.query.filter_by(turn_bol_assigned=False).filter(Turn.turn_date_date_assignment > hoy).paginate(page=page, per_page=per_page, error_out=False)


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
                    'name': turno.turn_str_name_turn,
                    'description': turno.turn_str_description,
                    'creation_date': turno.turn_date_creation_date.strftime('%Y-%m-%d'),
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
# [] MARCOS
# Listado de Turnos del Paciente
@user.route('/turnos/pendientes')
class GetTurnoUser(Resource):
    def get(self):
        """
        Obtiene los turnos pendientes de un usuario.
        Ejemplo: http://127.0.0.1:40709/user/turnos?page=1
        Retorna:
        --------
        jsonify:
            Devuelve una lista de objetos JSON que representan los turnos finalizados de un usuario.
            Cada objeto JSON contiene la información de un turno finalizado.

            Los campos de cada objeto JSON incluyen:
            - idturn: int
                El ID único del turno.
            - idservice: int
                El ID del servicio al que pertenece el turno.
            - nameturn: str
                El nombre del turno.
            - descriptionturn: str
                La descripción del turno.
            - creationdate: str
                La fecha de creación del turno en formato 'YYYY-MM-DD'.
            - assigmentturn: str
                La fecha de asignación del turno en formato 'YYYY-MM-DD'.
            - turn_start: str
                La hora de inicio del turno en formato 'HH:MM:SS'.
            - turn_finish: str
                La hora de finalización del turno en formato 'HH:MM:SS'.

            Si hay un error al conectarse con la base de datos, se devuelve un mensaje de error JSON.
        """
        auth = request.headers.get('Authorization')

        if not auth:
            return jsonify({'message': "Token no proporcionado"})



        try:
            hoy = date.today()
            # Paginacion
            page = request.args.get('page', 1, type=int)
            per_page = request.args.get('per_page', 10, type=int)

            turnos = Turn.query.filter_by(turn_bol_assigned=False).filter(Turn.turn_date_date_assignment > hoy).paginate(page=page, per_page=per_page, error_out=False)


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
                    'name': turno.turn_str_name_turn,
                    'description': turno.turn_str_description,
                    'creation_date': turno.turn_date_creation_date.strftime('%Y-%m-%d'),
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
#FERNANDO
#Listado de Turnos Finalizados del Paciente
@user.route('/turnos/end')
class GetTurnoEnd(Resource):
    def get(self):
        """
        Obtiene los turnos finalizados de un usuario.

        Retorna:
        --------
        jsonify:
            Devuelve una lista de objetos JSON que representan los turnos finalizados de un usuario.
            Cada objeto JSON contiene la información de un turno finalizado.

            Los campos de cada objeto JSON incluyen:
            - idturn: int
                El ID único del turno.
            - idservice: int
                El ID del servicio al que pertenece el turno.
            - nameturn: str
                El nombre del turno.
            - descriptionturn: str
                La descripción del turno.
            - creationdate: str
                La fecha de creación del turno en formato 'YYYY-MM-DD'.
            - assigmentturn: str
                La fecha de asignación del turno en formato 'YYYY-MM-DD'.
            - turn_start: str
                La hora de inicio del turno en formato 'HH:MM:SS'.
            - turn_finish: str
                La hora de finalización del turno en formato 'HH:MM:SS'.

            Si hay un error al conectarse con la base de datos, se devuelve un mensaje de error JSON.
        """
        verify_token()
        id = verify_token().get('id')
        hoy = date.today()
        if id:
            select_turn = Turn.query.filter_by(turn_int_user_id=id).filter(Turn.turn_date_date_assignment < hoy).all()
            turn_list = []

            try:
                if select_turn:
                    for data in select_turn:
                        turn_data = {
                            'idturn' : data.turn_int_id,
                            'idservice':data.service_id,
                            'nameturn':data.turn_str_name_turn,
                            'descriptionturn': data.turn_str_description,
                            'creationdate': data.turn_date_creation_date.strftime('%Y-%m-%d'),
                            'assigmentturn': data.turn_date_date_assignment.strftime('%Y-%m-%d'),
                            'turn_start': data.turn_time_start_turn.strftime('%H:%M:%S'),
                            'turn_finish': data.turn_time_finish_turn.strftime('%H:%M:%S')
                            }
                        turn_list.append(turn_data)
                    return jsonify(turn_list)
                else:
                    return jsonify({"message": "No hay turnos finalizados para este usuario"})
            except Exception as db:
                print("Error", db)
                return jsonify({"message": "error al conectarse con la DB"})
###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
# [] MARCOS // FERNANDO
@user.route('/turno/<int:turno>')
class ProcessTurnsUser(Resource):
    #MARCOS
    # ver el turno de forma individual , usando la url para que sea dinamicas las rutas
    def get(self, id):
        """
        Ver turno
        """
        verify_token()
        id = verify_token().get('id')
        pass

@user.route('/turno/asignar/<int:turn>')
class AssignerTurnsUser(Resource):
    @user.doc(
        description="Solicitar Turno",
        params={
            'id_servicio': 'id de Servicio',
            'token':'token de auorizacion',
        },
    )
    def put(self, turn):
        """
        Soliciar Turno *
        """

        data = request.get_json()
        # Verificar el token de autenticación
        user_id = verify_token().get('id')
        id_servicio = data.get('id_servicio')

        # Verificar si el usuario existe
        if user_id is None:
            return jsonify({'error': 'Usuario no encontrado'})

        id_turno = turn
        try:
            turno = Turn.query.filter_by(turn_int_id=id_turno).first()

            if turno is None:
                return jsonify({'error': 'Turno no encontrado'})

            turno.turn_int_user_id = int(user_id)
            turno.service_id = int(id_servicio)
            turno.turn_bol_assigned = True
            db.session.commit()

            return jsonify({'message': 'Turno asignado correctamente'})

        except Exception:
            db.session.rollback()
            return jsonify({'error': 'Error al asignar el turno'})

###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
#End Point Servicio
@user.route("/servicios")
class Servicios(Resource):
    def get(self):
        """
        Obtener Listado de Servicios *
        """
        auth = request.headers.get('Authorization')

        if not auth:
            return jsonify({'message': "Token no proporcionado"})


        verify_token()
        id = verify_token().get('id')

        try:
            # Paginacion
            page = request.args.get('page', 1, type=int)
            per_page = request.args.get('per_page', 10, type=int)

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

