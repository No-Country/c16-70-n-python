from flask import Blueprint, request, jsonify
from ..models.models import Users, db
from flask_restx import Api, Resource
from ..utils.segurity import descodificarPassword, codificarPassword

auth = Blueprint('auth', __name__)

api = Api(auth, version='1.0', title='Agendify', description='Agendify API REST')

autho = api.namespace ('', description= 'Rutas para Autotificacion')



@autho.route('/login')
class Users(Resource):
    def post(self):
        data = request.get_json()
        email= data.get('email')
        password= data.get('password')
        
        try:
            busqueda = Users.query.filter_by(use_str_email=email)
            print(busqueda)
            if busqueda :
                descodificarPassword(password=password, passwordDB=busqueda.use_str_password)

        except:
            pass