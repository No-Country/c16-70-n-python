from flask_restx import Resource
from flask import Blueprint, jsonify, request
from .auth import api
from ..models.models import User, db
from ..utils.segurity import verify_token

users = Blueprint("user", __name__)
user = api.namespace("user", description="Rutas User")


# [X] MARCOS
# Para que el usuario vea sus datos
@user.route('/get')
class GetUserDataById(Resource):
    def get(self):
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
                    'suspension_date': user.use_date_suspension_date,
                    'status': user.use_date_suspension,
                }
            return jsonify(user_data)
        except Exception as d:
            return jsonify({'message': 'Error en la operacion'})

#FERNANDO
# EndPoint para que el usuario pueda editar sus Datos
@user.route('/put')
class PutDatosUser(Resource):
    def put(self):
        verify_token()
        id = verify_token().get('id')
        pass

###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
# [] MARCOS
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



#FERNANDO
#Listado de Turnos Disponibles
@user.route('/turno')
class GetTurnUser(Resource):
    def get(self):
        verify_token()
        id = verify_token().get('id')
        pass


###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
# [] MARCOS
# Listado de Turnos del Paciente
@user.route('/turnos')
class GetTurnUser(Resource):
    def get(self):
        verify_token()
        id = verify_token().get('id')
        pass


###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
#FERNANDO
#Listado de Turnos Finalizados del Paciente
@user.route('/turnos/end')
class GetTurnoUser(Resource):
    def get(self):
        verify_token()
        id = verify_token().get('id')
        pass

###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
# [] MARCOS // FERNANDO
@user.route('/turno/<int:use_int_id>')
class ProcessTurnsUser(Resource):
    #MARCOS
    # ver el turno por id de url
    def get(self, id):
        verify_token()
        id = verify_token().get('id')
        
        pass


###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
    # FERNANDO
    # actualziar turno por url <int:id>
    # solo para abandonar el turno es decir retirar su id unico
    def put(self):
        verify_token()
        id = verify_token().get('id')
        
        pass


###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
#################End Point Viejos ##############
# # Ruta para obtener información del cliente
# @client.route("/get")
# class GetDataClient(Resource):
#     def get(self):
#         # Solicitud de Token
#         auth = request.headers.get('Authorization')
#         if not auth:
#             return jsonify({"message": "Token no proporcionado"})
        
#         datosToken = descodificarToken(auth)
#         id = datosToken.get('id')
        
#         try:
#             # Ejecuta la consulta para obtener el usuario
#             user = Cliente.query.filter_by(cli_int_user_id=id).first()
            
#             # Traemos la data del cliente
#             client_data = Cliente.query.all()
#             client_list = []
#             for data in client_data:
#                 clients_data = {
#                     'firstname': data.cli_str_first_name,
#                     'lastname': data.cli_str_last_name,
#                     'phone': data.cli_str_phone,
#                     'direction': data.cli_str_direction,
#                     'profile_image': data.cli_str_profile_img,
#                     'register_date': data.cli_date_register_date,
#                     'suspension_date': data.cli_date_suspension_date,
#                 }
#                 client_list.append(clients_data)
#             return jsonify({'users': client_list})
#         except Exception as db:
#             print("Error:", db)
#             return jsonify({"message": "Error al conectarse con la BD"})

# # Rutas registrar información del cliente
# @client.route("/post")
# class PostClient(Resource):
#     def post(self):
#         pass


# # Rutas de actualización de data del cliente
# @client.route("/put")
# class UpgradeDataClient(Resource):
#     def put(self):
#         pass

# @client.route("/img")
# class UpgrdadeImgClient(Resource):
#     def put(self):
#         #Solicitud de Token por el headers
#         auth = request.headers.get('Authorization')
#         img = request.files['img']

#         if not auth:
#             return jsonify({"message": "Token no proporcionado"})

#         datosToken = descodificarToken(auth)
#         id = datosToken.get('id')
#         role = datosToken.get('role')

#         try:
#             # Verificar el rol del usuario
#             if role == 'clie' or role == 'prov':
#                 user = None
#                 if role == 'clie':
#                     user = Cliente.query.filter_by(cli_int_user_id=id).first()
#                     if not user:
#                         return jsonify({"message": "Cliente no encontrado"})
#                     # Guardar la imagen para el cliente
#                     user.save_cli_str_profile_img(img)
#                     if not user:
#                         return jsonify({"message": "Proveedor no encontrado"})
#                     # Guardar la imagen para el proveedor
#                     user.save_pro_str_profile_img(img)

#                 return jsonify({"message": "Imagen de perfil actualizada correctamente"})
#             else:
#                 return jsonify({"message": "Rol de usuario desconocido"})

#         except Exception as e:
#             print("Error:", e)
#             return jsonify({"message": "Error al conectarse con la BD"})


# Obtener turnos
# actualziar ,el campo de turno.
# obtener categorias
# ver Ubicacion 