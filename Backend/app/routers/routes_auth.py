from flask import Blueprint, request, jsonify
from ..models.models import User, db
from flask_restx import Api, Resource

auth = Blueprint('auth', __name__)

api = Api(auth, version='1.0', title='Agendify', description='Agendify API REST')

users = api.namespace ('Users', description= 'Rutas para Autotificacion')

@users.route('/user')
class Users(Resource):
    def post(self):
        data = request.get_json()
        nombre = data.get('nombre')
        
        if nombre:
            new_user = User(nombre=nombre)
            db.session.add(new_user)
            db.session.commit()

            return jsonify({'mensaje':'usuario creado'})
        else:
            return jsonify({'mensaje':'Error al crear el usuario'})
    
    def put(self):
        nombre = request.args.get('nombre')

        if nombre:
            user = User.query.filter_by(nombre=nombre).first()
            if user:
                user.nombre = request.args.get('nuevo_nombre')
                db.session.commit()
                return jsonify({'message': 'Usuario actualizado correctamente'}), 200
            else:
                return jsonify({'message': 'Usuario no encontrado'}), 404
        else:
            return jsonify({'message': 'Falta el nombre del usuario a actualizar'}), 400

    def delete(self):
        nombre = request.args.get('nombre')

        if nombre:
            user = User.query.filter_by(nombre=nombre).first()
            if user:
                db.session.delete(user)
                db.session.commit()
                return jsonify({'message': 'Usuario eliminado correctamente'}), 200
            else:
                return jsonify({'message': 'Usuario no encontrado'}), 404
        else:
            return jsonify({'message': 'Falta el nombre del usuario a eliminar'}), 400
#GET
    def get(self):
        nombre = request.args.get('nombre')

        if nombre:
            user = User.query.filter_by(nombre=nombre).first()
            db.session.
            return jsonify(user)
        else:
            return jsonify({'message': 'Usuario no encontrado'})
