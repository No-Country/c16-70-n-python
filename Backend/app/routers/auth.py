from flask import Blueprint, request, jsonify
from ..models.models import User, db, Cliente, Proveedor
from flask_restx import Api, Resource
from ..utils.segurity import descodificarPassword, codificarPassword, codificarToken, descodificarToken, secure_filename
import os
from datetime import datetime

fecha_registro = datetime.now()

auth = Blueprint("auth", __name__)

api = Api(auth, version="1.0", title="Agendify", description="Agendify API REST")

autho = api.namespace("", description="Rutas para Autotificacion")


@autho.route("/register")
class Users(Resource):
    def post(self):
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")
        role = data.get("role")
        nombre = data.get("nombre")
        apellido = data.get("apellido")
        telefono = data.get("telefono")
        direccion = data.get("direccion")
        
        try:
            exitsEmail = User.query.filter_by(use_str_email=email).first()

            if exitsEmail:
                return jsonify({"message": "El correo electrónico ya está en uso. Por favor, utilice otro."})
            
            passwordH = codificarPassword(password)
            new_user = User(use_str_email=email, use_str_password=passwordH, use_str_type_profile=role)
            db.session.add(new_user)
            db.session.commit()
            id_user = new_user.use_int_id
            print ('esta es la nueva id del usuario', id_user)
            
            if role == 'clie':
                new_cliente = Cliente(cli_int_user_id=id_user, cli_str_first_name=nombre, cli_str_last_name=apellido, 
                                    cli_str_phone=telefono, cli_str_direction=direccion, cli_date_register_date=fecha_registro)
                db.session.add(new_cliente)
                db.session.commit()

            elif role == 'prov':
                new_proveedor = Proveedor(pro_int_user_id=id_user, pro_str_first_name=nombre, pro_str_last_name=apellido,
                                        pro_str_phone=telefono, pro_str_direction=direccion, pro_date_registration_date =fecha_registro)
                db.session.add(new_proveedor)
                db.session.commit()
                
            else:
                return jsonify({"message": "El rol proporcionado es incorrecto"})

            return jsonify({"message": "El usuario fue creado exitosamente"})

        except Exception as e:
            print("Error:", e)
            return jsonify({"message": "Error al conectarse con la base de datos"})

####Login
@autho.route("/login")
class Login(Resource):
    def post(self):
        data = request.get_json()
        email= data.get("email")
        password= data.get("password")

        try:
            exitsEmail = User.query.filter_by(use_str_email=email).first()

            if exitsEmail:
                passwordDB = exitsEmail.use_str_password
                compararPassword= descodificarPassword(password=password, passwordDB=passwordDB)
            if  compararPassword is False:
                return jsonify({'message':'la password no Coiciden'})
            
            if compararPassword is True:
                id = exitsEmail.use_int_id
                role= exitsEmail.use_str_type_profile

                print (role)

                token = codificarToken({'id':id, 'role':role})
                print (token)
                return jsonify({'token':token})
        except Exception as e:
            print("Error:", e)
            return jsonify({"message": "Error al conectarse con la BD"})
        

#route de ejemplo
@autho.route("/rol")
class Token(Resource):
    def post(self):
        auth = request.headers.get('Authorization')
        if not auth:
            return jsonify({"message": "Token no proporcionado"})

        datosToken = descodificarToken(auth)
        id = datosToken.get('id')
        role = datosToken.get('role')

        try:
            # Ejecuta la consulta para obtener el usuario
            user = User.query.filter_by(use_int_id=id, use_str_type_profile=role).first()

            if user:
                if user.use_str_type_profile == "clie":
                    print('El rol es de cliente')
                    return jsonify({'role': user.use_str_type_profile})
                elif user.use_str_type_profile == "prov":
                    print('El usuario tiene un rol de Proveedor')
                    return jsonify({'role': user.use_str_type_profile})
                else:
                    print('El usuario tiene un rol desconocido:', user.use_str_type_profile)
                    return jsonify({'role': user.use_str_type_profile})
            else:
                print('Usuario no encontrado')
                return jsonify({"message": "Usuario no encontrado"})

        except Exception as e:
            print("Error:", e)
            return jsonify({"message": "Error al conectarse con la BD"})


# EndPoint para Actualizar la Imagen
# se pueden mover para las rutas respectivas

# @autho.route("/user/img")
# class Img(Resource):
#     def post(self):
#         #Solicitud de Token por el headers
#         auth = request.headers.get('Authorization')
#         if not auth:
#             return jsonify({"message": "Token no proporcionado"}), 401

#         datosToken = descodificarToken(auth)
#         id = datosToken.get('id')
#         role = datosToken.get('role')

#         try:
#             # Verificar el rol del usuario
#             if role == 'clie' or role == 'prov':
#                 # Obtener el usuario
#                 user = None
#                 if role == 'clie':
#                     user = Cliente.query.filter_by(cli_int_user_id=id).first()
#                 elif role == 'prov':
#                     user = Proveedor.query.filter_by(pro_int_user_id=id).first()
                
#                 if not user:
#                     return jsonify({"message": "Usuario no encontrado"}), 404
                
#                 # Verificar si la solicitud contiene una imagen
#                 if 'image' not in request.files:
#                     return jsonify({"message": "No se encontró ninguna imagen en la solicitud"}), 400
                
#                 image_file = request.files['image']
                
#                 # Verificar si el nombre de archivo está vacío
#                 if image_file.filename == '':
#                     return jsonify({"message": "Nombre de archivo vacío"}), 400
                
#                 # Guardar la imagen
#                 filename = secure_filename(image_file.filename)
#                 file_path = os.path.join('fotos', 'profile_pictures', filename)
#                 image_file.save(file_path)
                
#                 # Actualizar el campo de la imagen de perfil en la base de datos
#                 if role == 'clie':
#                     Cliente.cli_str_profile_img = file_path
#                 elif role == 'prov':
#                     Proveedor.pro_str_profile_img = file_path
                
#                 db.session.commit()
                
#                 return jsonify({"message": "Imagen de perfil actualizada correctamente"}), 200
#             else:
#                 return jsonify({"message": "Rol de usuario desconocido"}), 400

#         except Exception as e:
#             print("Error:", e)
#             return jsonify({"message": "Error al conectarse con la BD"}), 500



#Actualizar la imagen 
    # def put(self):
    #     auth = request.headers.get('Authorization')
    #     if not auth:
    #         return jsonify({"message": "Token no proporcionado"})

    #     datosToken = descodificarToken(auth)
    #     id = datosToken.get('id')
    #     role = datosToken.get('role')


#Borrar la Iamgen 
        
    # def delete(self):
    #     auth = request.headers.get('Authorization')
    #     if not auth:
    #         return jsonify({"message": "Token no proporcionado"})

    #     datosToken = descodificarToken(auth)
    #     id = datosToken.get('id')
    #     role = datosToken.get('role')