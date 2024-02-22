from flask_restx import Api, Resource
from flask import Blueprint, jsonify, request
from .auth import api
# from ..models.models import User, Cliente, db
from ..utils.segurity import descodificarToken

users = Blueprint("user", __name__)
user = api.namespace("user", description="Rutas User")

#MARCOS
# EndPoint Para que el usuario pueda ver su datos
@user.route('/get')
class DatosGeT(Resource):
    def get(self):
        pass

#FERNANDO
# EndPoint para que el usuario pueda editar su Dato
@user.route('/put')
class DatosPut(Resource):
    def put(self):
        # Solicitud de Token
        auth = request.headers.get('Authorization')
        if not auth:
            return jsonify({"message": "Token no proporcionado"})
        
        datosToken = descodificarToken(auth)
        id = datosToken.get('id')
        pass


#MARCOS
# Actualizar su imagen
@user.route('/img')
class ImgPut(Resource):
    def put(self):
        auth = request.headers.get('Authorization')
        if not auth:
            return jsonify({"message": "Token no proporcionado"})
        
        datosToken = descodificarToken(auth)
        id = datosToken.get('id')
        pass


#FERNANDO
#Listado de Turnos Disponibles
@user.route('/turno')
class TurnoGet(Resource):
    def get(self):
        auth = request.headers.get('Authorization')
        if not auth:
            return jsonify({"message": "Token no proporcionado"})
        
        datosToken = descodificarToken(auth)
        id = datosToken.get('id')
        pass

#MARCOS
#Listado de Turnos del Paciente
@user.route('/turnos')
class TurnoGet(Resource):
    def get(self):
        auth = request.headers.get('Authorization')
        if not auth:
            return jsonify({"message": "Token no proporcionado"})
        
        datosToken = descodificarToken(auth)
        id = datosToken.get('id')
        pass


#FERNANDO
#Listado de Turnos Finalizados del Paciente
@user.route('/turnos/end')
class TurnoGet(Resource):
    def get(self):
        auth = request.headers.get('Authorization')
        if not auth:
            return jsonify({"message": "Token no proporcionado"})
        
        datosToken = descodificarToken(auth)
        id = datosToken.get('id')
        pass

#MARCOS // FERNANDO
@user.route('/turno/<int:id>')
class TurnosCliente(Resource):
    #MARCOS
    # ver el turno por id de url
    def get(self):
        auth = request.headers.get('Authorization')
        if not auth:
            return jsonify({"message": "Token no proporcionado"})
        
        datosToken = descodificarToken(auth)
        id = datosToken.get('id')
        pass

    # FERNANDO
    # actualziar turno por url <int:id>
    # solo para abandonar el turno es decir retirar su id unico
    def put(self):
        auth = request.headers.get('Authorization')
        if not auth:
            return jsonify({"message": "Token no proporcionado"})
        
        datosToken = descodificarToken(auth)
        id = datosToken.get('id')
        pass



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