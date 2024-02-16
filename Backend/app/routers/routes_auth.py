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
            return jsonify({'success': True}), 201
        else:
            return jsonify({'success': False}), 400

    def put(self):
        data =request.get_json()
        nombre =data.get('nombre')

        if nombre:
            resp = User.query.filter_by(nombre=nombre).first()
            db.session.commit()
            return jsonify({'messager':'dato Actualizado'})
        else:
            return jsonify({'messager':"Usuari no Encontrado"})


    def delete(self):
        data =request.get_json()
        nombre =data.get('nombre')
        if nombre:
            resp = User.query.order_by(User.nombre).all()
            db.session.delete(resp)
            db.session.commit()
            return jsonify({'mesage':'Usuario Eliminado'})
        else:
            return jsonify({'messager':'Usuario no Encontrado'})

    def get(self):
        data =request.get_json()
        nombre =data.get('nombre')
        if nombre:
            resp = User.query.order_by(User.nombre).all()
            return jsonify({resp})
