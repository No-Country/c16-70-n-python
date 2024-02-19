from flask import Blueprint, request, jsonify, current_app
from ..models.models import User, db, Cliente, Proveedor
from flask_restx import Api, Resource
from ..utils.segurity import descodificarPassword, codificarPassword, codificarToken, descodificarToken
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
        email = data.get("email")
        password = data.get("password")

        try:
            exitsEmail = User.query.filter_by(use_str_email=email).first()

            if exitsEmail:
                passwordDB = exitsEmail.use_str_password
                compararPassword = descodificarPassword(password=password, passwordDB=passwordDB)

                if compararPassword:
                    id = exitsEmail.use_int_id
                    role = exitsEmail.use_str_type_profile

                    print(role)

                    token = codificarToken({'id': id, 'role': role})
                    print(token)
                    return jsonify({'token': token})
                else:
                    return jsonify({'message': 'La contraseña ingresada no coincide'})
            else:
                return jsonify({'message': 'El email ingresado no está registrado'})

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

#NOTA:  las rutas para lasimagenes puede ser movidas a su archivo correspondiente, queda por revisar bien la ruta delete de img
        
@autho.route("/user/img")
class Img(Resource):
    def put(self):
        #Solicitud de Token por el headers
        auth = request.headers.get('Authorization')
        img = request.files['img']

        if not auth:
            return jsonify({"message": "Token no proporcionado"})

        datosToken = descodificarToken(auth)
        id = datosToken.get('id')
        role = datosToken.get('role')

        try:
            # Verificar el rol del usuario
            if role == 'clie' or role == 'prov':
                user = None
                if role == 'clie':
                    user = Cliente.query.filter_by(cli_int_user_id=id).first()
                    if not user:
                        return jsonify({"message": "Cliente no encontrado"})
                    # Guardar la imagen para el cliente
                    user.save_cli_profile_img(img)
                elif role == 'prov':
                    user = Proveedor.query.filter_by(pro_int_user_id=id).first()
                    if not user:
                        return jsonify({"message": "Proveedor no encontrado"})
                    # Guardar la imagen para el proveedor
                    user.save_pro_str_profile_img(img)

                return jsonify({"message": "Imagen de perfil actualizada correctamente"})
            else:
                return jsonify({"message": "Rol de usuario desconocido"})

        except Exception as e:
            print("Error:", e)
            return jsonify({"message": "Error al conectarse con la BD"})


#Borrar la Iamgen 
        
    def delete(self):
        # Solicitud de Token por el headers
        auth = request.headers.get('Authorization')

        if not auth:
            return jsonify({"message": "Token no proporcionado"})

        datosToken = descodificarToken(auth)
        id = datosToken.get('id')
        role = datosToken.get('role')

        try:
            # Verificar el rol del usuario
            if role == 'clie' or role == 'prov':
                user = None
                if role == 'clie':
                    user = Cliente.query.filter_by(cli_int_user_id=id).first()
                    if not user:
                        return jsonify({"message": "Cliente no encontrado"})
                    # Eliminar la imagen del cliente
                    user.delete_profile_img()
                elif role == 'prov':
                    user = Proveedor.query.filter_by(pro_int_user_id=id).first()
                    if not user:
                        return jsonify({"message": "Proveedor no encontrado"})
                    # Eliminar la imagen del proveedor
                    user.delete_profile_img()

                return jsonify({"message": "Imagen de perfil eliminada correctamente"})
            else:
                return jsonify({"message": "Rol de usuario desconocido"})

        except Exception as e:
            print("Error:", e)
            return jsonify({"message": "Error al conectarse con la BD"})