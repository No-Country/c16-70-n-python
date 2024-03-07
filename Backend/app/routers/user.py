from flask_restx import Resource
from flask import Blueprint, jsonify, request
from .auth import api
from ..models.models import User, db, Turn, Services
from ..utils.segurity import verify_token
from datetime import datetime , date

users = Blueprint("user", __name__)
user = api.namespace("user", description="Rutas User")


# [X] MARCOS
# Mostrar data del usuario
@user.route('/get')
class GetUserDataById(Resource):
    def get(self):
        """
        Obtiene los datos de un usuario específico por su ID.

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
                return jsonify({'error': 'Usuario no encontrado'}), 404
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
        except Exception as d:
            return jsonify({'message': 'Error en la operacion'})

# [X] FERNANDO
# EndPoint para que el usuario pueda editar sus Datos
@user.route('/put')
class PutDatosUser(Resource):
    def put(self):
        """
        Actualiza los datos de un usuario en la base de datos.

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

# [X] MARCOS
# Actualizar su imagen
@user.route('/img')
class PutImgUser(Resource):
    def put(self):
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


# [X] FERNANDO
# Listado de Turnos Disponibles
@user.route('/turnos')
class TurnosGet(Resource):
    def get(self):
        """
        Obtiene los turnos no asignados cuya fecha de asignación es posterior al día actual.
        
        Parámetros:
        -----------
        No recibe parámetros directamente de la solicitud.

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
        verify_token()
        id = verify_token().get('id')
        hoy = date.today()
        if id:
            select_turn = Turn.query.filter_by(turn_bol_assigned=False).filter(Turn.turn_date_date_assignment > hoy).all()
            turn_list = []  

            try:
                if select_turn:    
                    for data in select_turn:
                        service_description = None
                        if data.service:
                            service_description = data.service.ser_str_category_name
                        
                        turn_data = {
                            'idturn': data.turn_int_id,
                            'service_info': {
                                'idservice': data.service_id,
                                'service_description': service_description
                            },
                            'id_user_assig': data.turn_int_user_id,
                            'nameturn': data.turn_str_name_turn,
                            'descriptionturn': data.turn_str_description,
                            'creationdate': data.turn_date_creation_date.strftime('%Y-%m-%d'),
                            'assigmentturn': data.turn_date_date_assignment.strftime('%Y-%m-%d'),
                            'turn_start': data.turn_time_start_turn.strftime('%H:%M:%S'),
                            'turn_finish': data.turn_time_finish_turn.strftime('%H:%M:%S')
                        }
                        turn_list.append(turn_data)
                return jsonify(turn_list)
            except Exception as db:
                print("Error", db)
                return jsonify({"message": "error al conectarse con la DB"})

###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
# [X] MARCOS
# Listado de Turnos del Paciente
@user.route('/turnos/pendientes')
class GetTurnoUser(Resource):
    def get(self):
        """
        Obtiene los turnos pendientes de un usuario.
        
        Parámetros:
        -----------
        No recibe parámetros directamente de la solicitud.

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
            select_turn = Turn.query.filter_by(turn_int_user_id=id).filter(Turn.turn_date_date_assignment > hoy).all()
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

# [X] FERNANDO
#Listado de Turnos Finalizados del Paciente
@user.route('/turnos/end')
class GetTurnoUser(Resource):
    def get(self):
        """
        Obtiene los turnos finalizados de un usuario.
        
        Parámetros:
        -----------
        No recibe parámetros directamente de la solicitud.

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

# [X] MARCOS // FERNANDO
@user.route('/turno/<int:turn_int_id>')
class ProcessTurnsUser(Resource):
    
    # MARCOS
    # ver el turno por id de url
    def get(self, turn_int_id):
        """
        Obtiene el detalle del turno seleccionado.
        
        Parámetros:
        -----------
        Como parametro esta el id del turno que se ha seleccionado.

        Retorna:
        --------
        jsonify:
        
            Devuelve una lista de objetos JSON que representan los detalles del turno.
            Cada objeto JSON contiene la información detalla de un turno.

            Los campos de cada objeto JSON incluyen:
            
            - idturn: int
                El ID único del turno.
            - idservice: int
                El ID del servicio al que pertenece el turno.
            - service_description: str
                La descripcion del servicio al que pertenece el turno.
            - iduser: int
                El ID del usuario al que pertenece el turno.
            - user_first_name: str
                El primer nombre del usuario al que pertenece el turno.
            - user_last_name: str
                El apellido del usuario al que pertenece el turno.
            - user_phone: str
                El telefono del usuario al que pertenece el turno.
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
        
        turn_id = turn_int_id
        
        try:
            
            # Filtramos por el id del turno
            select_turn = Turn.query.filter_by(turn_int_user_id=turn_id)
            
            # Consultamos la data del usuario
            user = User.query.get(id)
            
            # Consultamos la data del servicio
            service_info = Services.query.get()
            
            # Verificamos si el turn existe
            if select_turn is None:
                return jsonify({'error': 'Turno no encontrado'}), 404
            
            # Mostramos los detalles del turno
            turn_data = {
                    'idturn' : select_turn.turn_int_id,
                    'service_info': {
                        'idservice': service_info.service_id,
                        'service_description': service_info.service_description
                    },
                    'user_info': {
                        'iduser': user.use_int_id,
                        'user_first_name': user.use_str_first_name,
                        'user_last_name': user.use_str_last_name,
                        'user_phone': user.use_str_phone
                    },
                    'nameturn':select_turn.turn_str_name_turn,
                    'descriptionturn': select_turn.turn_str_description,
                    'creationdate': select_turn.turn_date_creation_date.strftime('%Y-%m-%d'),
                    'assigmentturn': select_turn.turn_date_date_assignment.strftime('%Y-%m-%d'),
                    'turn_start': select_turn.turn_time_start_turn.strftime('%H:%M:%S'),
                    'turn_finish': select_turn.turn_time_finish_turn.strftime('%H:%M:%S')
            }
            return jsonify(turn_data)
        
        except Exception as d:
            return jsonify({'message': 'Error en la operacion'})

# [X] FERNANDO
@user.route('/turno/asignar/<int:turn_int_id>')
class AssignerTurnsUser(Resource):
    # Asignar un turno a un usuario
    def put(self, turn_int_id):
        
        # Verificar el token de autenticación
        user_id = verify_token().get('id')
        
        # Verificar si el usuario existe
        if user_id is None:
            return jsonify({'error': 'Usuario no encontrado'}), 404
        
        # Intentar asignar el turno al usuario
        id_turno=turn_int_id
        data = request.get_json()
        
        try:
            print(turn_int_id)
            turno = Turn.query.filter_by(turn_int_id=id_turno).first()
            if turno is None:
                return jsonify({'error': 'Turno no encontrado'})

            turno.turn_int_user_id = int(user_id)
            turno.service_id = data.get('id_servicio')
            turno.turn_bol_assigned=True
            print(turno)
            print(turno.turn_int_user_id)
            db.session.commit()
            return jsonify({'message': 'Turno asignado correctamente'})

        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'Error al asignar el turno', 'details': str(e)})

###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################

# [X] FERNANDO
# End Point Servicio
@user.route("/servicios")
class Servicios(Resource):
    def get(self):
        """ 
        Obtener Listado de Servicios
        Ejemplo: http://127.0.0.1:40709/admin/servicios?page=1
        
        Parámetros:
        -----------
        No recibe parámetros directamente de la solicitud.

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

            servicios = Servicios.query.paginate(page=page, per_page=per_page, error_out=False)

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