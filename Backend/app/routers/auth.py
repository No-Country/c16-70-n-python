from flask import Blueprint, request, jsonify
from ..models.models import User, db
from flask_restx import Api, Resource
from ..utils.segurity import descodificarPassword, codificarPassword, codificarToken, descodificarToken

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

        try:
            exitsEmail = User.query.filter_by(use_str_email=email).first()

            if exitsEmail:
                return jsonify({"messager":"Email en uso Porfavor Intente con Otro"})
            if not exitsEmail:
                passwordH = codificarPassword(password)
                new_user = User(use_str_email=email, use_str_password=passwordH, use_str_type_profile=role)
                db.session.add(new_user)
                db.session.commit()
            return jsonify({"messager":"EL Usuario Fue Creado"})
        except Exception as e:
            print("Error:", e)
            return jsonify({"message": "Error al conectarse con la BD"})
        

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
                if user.use_str_type_profile == "clien":
                    print('El rol es de cliente')
                    return jsonify({'role': user.use_str_type_profile})
                elif user.use_str_type_profile == "Provi":
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