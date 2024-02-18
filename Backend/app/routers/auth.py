from flask import Blueprint, request, jsonify
from ..models.models import User, db
from flask_restx import Api, Resource
from ..utils.segurity import descodificarPassword, codificarPassword, codificarToken

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
        except:
            return jsonify({'message':'Error al conectarse con la Base de Datos'})