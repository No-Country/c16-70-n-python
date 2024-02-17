# from flask import Blueprint, request, jsonify
# from ..models.models import User, db
# from flask_restx import Api, Resource

# auth = Blueprint('auth', __name__)

# api = Api(auth, version='1.0', title='Agendify', description='Agendify API REST')

# users = api.namespace ('Users', description= 'Rutas para Autotificacion')

# @users.route('/user')
# class Users(Resource):
#     def post(self):
#         data = request.get_json()
#         nombre = data.get('nombre')
        
#         if nombre:
#             new_user = User(nombre=nombre)
#             db.session.add(new_user)
#             db.session.commit()

#             return jsonify({'mensaje':'usuario creado'})
#         else:
#             return jsonify({'mensaje':'Error al crear el usuario'})
# #UPDATE
#     def put(self):
#         consulta = request.get_json()
#         nombre = consulta.get('nombre')
#         user_id = consulta.get('id')

#         if nombre is None:
#             return jsonify({'message': 'Falta el nombre del usuario a actualizar'})

#         if user_id:
#             resp = User.query.filter_by(id=user_id).first()
#             print('\033[93m',resp)
#             if resp:
#                 resp.nombre = nombre
#                 db.session.commit()
#                 return jsonify({'message': 'Usuario actualizado correctamente'})
#             else:
#                 return jsonify({'message': 'Usuario no encontrado'})
#         else:
#             return jsonify({'message': 'Falta el ID del usuario a actualizar'})
        
# #DELETE
#     def delete(self):
#         consulta = request.get_json()
#         user = consulta.get('id')

#         if user:
#             resp = User.query.filter_by(id=user).first()
#             if resp:
#                 print('\033[93m',resp)
#                 db.session.delete(resp)
#                 db.session.commit()
#                 return jsonify({'message': 'Usuario eliminado correctamente'})
#             else:
#                 return jsonify({'message': 'Usuario no encontrado'})
#         else:
#             return jsonify({'message': 'Falta el nombre del usuario a eliminar'})
# #GET
#     def get(self):
#         consulta = request.get_json()

#         user = consulta.get('id')

#         print(consulta)
#         if user :

#             resp = User.query.filter_by(id=user).first()
#             if resp:
#                 print('\033[93m',resp)
#                 print('tipo de dato',type(resp))
#                 return jsonify({'datos':resp.nombre})
#             else:
#                 return jsonify({'error': 'User not found'})
#         else:
#             return jsonify({'error': 'Invalid request'})
