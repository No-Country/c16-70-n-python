# from flask_restx import Api, Resource
# from flask import Blueprint, jsonify, request
# from ..routers.auth import api,descodificarToken
# from ..models.models import User, Proveedor, Ubication ,db
# from datetime import datetime

# prove= Blueprint("prove",__name__)

# prov = api.namespace("prove", description="Rutas para proveedor")

# #arranco a escribir rutas para obtener info del proovedor
# @prov.route("/get")
# class GetDataSupplier(Resource):
#     def get(self):
#         #solicitud de Token
#         auth = request.headers.get('Authorization')
#         if not auth:
#             return jsonify({"menssage": "Token no proporcionado"})
        
#         datostoken = descodificarToken(auth)
#         id = datostoken.get('id')

#         try:
#             #llenamos la suppliter_list con los datos del proovedor
#             suppliter_data = Proveedor.query.filter_by(pro_int_user_id=id).all()
#             if suppliter_data:    
#                 suppliter_list = []
#                 for data in suppliter_data:
#                     suppliter_data = {
#                         'firstname': data.pro_str_first_name,
#                         'lastname': data.pro_str_last_name,
#                         'phone': data.pro_str_phone,
#                         'direction': data.pro_str_direction,
#                         'profile_image': data.pro_str_profile_img,
#                         'register_date': data.pro_date_registration_date,
#                         'suspension_date': data.pro_date_suspension_date,
#                     }
#                     suppliter_list.append(suppliter_data)
#                 return jsonify(suppliter_data)
#             else:
#                 print(f"id {id} de usuario no encontrado en la base")
#                 return jsonify({"menssage":"No se encontro un proovedor asociado al usuario"})
#         except Exception as db:
#             print("Error",db)
#             return jsonify({"menssage":"error al conectarse con la DB"})
        
# @prov.route("/put")
# class PostSuppliter(Resource):

#     def put(self):
#         #solicitud de Token
#         auth = request.headers.get('Authorization')

#         data = request.get_json()
#         firstname = data.get("firstname")
#         lastname = data.get("lastname")
#         phone = data.get("phone")
#         direction = data.get("direction")

#         if not auth:
#             return jsonify({"menssage": "Token no proporcionado"})
        
#         datostoken = descodificarToken(auth)
#         id = datostoken.get('id')
#         #tengo dudas con que id usar para la consulta 

#         try:
#             supplier = Proveedor.query.filter_by(pro_int_user_id=id).first()

#             if supplier:
#                 supplier.pro_str_first_name = firstname
#                 supplier.pro_str_last_name = lastname
#                 supplier.pro_str_phone = phone
#                 supplier.pro_str_direction = direction
#                 db.session.commit()
#                 return jsonify({"message": "Proveedor actualizado correctamente"})
#             else:
#                 return jsonify({"message": "Proveedor no encontrado"})
#         except Exception as e:
#             print("Error:", e)
#             return jsonify({"message": "Error al actualizar el proveedor"})


# @prov.route("/turn")
# class UpgradeProveedorTurn(Resource):
#     def get(self):
#         pass

# @prov.route("/put")
# class UpgradeProveedorTurn(Resource):
#     def post(self):
#         pass



# # Obtener los turnos por id   Orlando
# # actualizar infor del turno Orlando
# # borrar turno orlando Orlando
# # crear servicio == categoria orlando
# # obtener categorias   
# # crear Ubicacion      fernando
# @prov.route("/ubic")
# class post_ubic(Resource):
#     def post(self):
#         auth = request.headers.get('Authorization')

#         data = request.get_json()
#         ubication = data.get("ubication")
#         direction = data.get("direction")

#         if not auth:
#             return jsonify({"menssage": "Token no proporcionado"})
        
#         datostoken = descodificarToken(auth)
#         id = datostoken.get('id')

#         try:
#             proveedor = Proveedor.query.filter_by(pro_int_user_id=id).first()
#             if proveedor:
#                 new_ubication = Ubication(ubi_int_proveedor_id=proveedor.pro_int_id, ubi_str_ubication=ubication, ubi_str_direction=direction)
#                 db.session.add(new_ubication)
#                 db.session.commit()
#             else:
#                 return jsonify({"menssage":"No existe el usuario en la tabla proveedor"})

#         except Exception as db:
#             print("Error",db)
#             return jsonify({"menssage":"error al conectarse con la DB"})



# # obtener ubicacion    fernando 
# @prov.route("/ubic")
# class get_ubic(Resource):
#     def get(self):
#         auth = request.headers.get('Authorization')

#         if not auth:
#             return jsonify({"menssage": "Token no proporcionado"})
        
#         datostoken = descodificarToken(auth)
#         id = datostoken.get('id')

#         try:
#             proveedor = Proveedor.query.filter_by(pro_int_user_id=id).first()
#             if proveedor:
#                 id_proveedor = proveedor.pro_int_id
#             else:
#                 return jsonify({"menssage":"el usuario no existe en la tabla proveedor"})
#             ubicacion_data = Ubication.query.filter_by(ubi_int_proveedor_id=id_proveedor).all()
#             if ubicacion_data:
#                 ubicaciones = []
#                 for data in ubicacion_data:
#                     ubicacion_data = {
#                         'id_ubicacion': data.ubi_int_id,
#                         'ubicacion': data.ubi_str_ubication,
#                         'direction': data.ubi_str_direction,
#                     }
#                     ubicaciones.append(ubicacion_data)
#                 return jsonify(ubicaciones)
#             else:
#                 return jsonify({"menssage":"el proveedor no tiene ubicaciones disponibles"})
#         except Exception as db:
#             print("Error",db)
#             return jsonify({"menssage":"error al conectarse con la DB"})


# # actualizar ubicacion fernando
# @prov.route("/ubic")
# class put_ubic(Resource):
#     def put(self):
#         auth = request.headers.get('Authorization')

#         data = request.get_json()
#         id_ubicacion = data.get("id_ubicacion")
#         ubicacion = data.get("ubicacion")
#         direction = data.get("direction")
#         if not auth:
#             return jsonify({"menssage": "Token no proporcionado"})
        
#         datostoken = descodificarToken(auth)
#         id_user = datostoken.get('id')
#         proveedor = Proveedor.query.filter_by(pro_int_user_id=id_user).first()
#         id_proveedor = proveedor.pro_int_id

#         try:
#             ubicacion_q = Ubication.query.filter_by(ubi_int_id=id_ubicacion).first()
#             if ubicacion_q.ubi_int_proveedor_id == id_proveedor:
#                 ubicacion_q.ubi_str_ubication = ubicacion
#                 ubicacion_q.ubi_str_direction = direction
#                 db.session.commit()
#                 return jsonify({"message": "Ubicacion actualizada correctamente"})
#             else:
#                 return jsonify({"message": "Ubicacion no encontrada"})

#         except Exception as db:
#             print("Error",db)
#             return jsonify({"menssage":"error al conectarse con la DB"})

# delete ubicacion     orlando




@user.route('/turno/asignar/<int:turn_int_id>')
class AssignerTurnsUser(Resource):
    # Asignar un turno a un usuario
    def put(self, turn_int_id):
        # Verificar el token de autenticación
        user_id = verify_token().get('id')

        # Verificar si el usuario existe
        if user_id is None:
            return jsonify({'error': 'Usuario no encontrado'}), 404

        # Intentar asignar el turno al usuario
        try:
            turno = Turn.query.filter_by(turn_int_id=turn_int_id).first()
            if turno is None:
                return jsonify({'error': 'Turno no encontrado'}), 404

            turno.turn_int_user_id = user_id
            db.session.commit()
            return jsonify({'message': 'Turno asignado correctamente'}), 200

        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'Error al asignar el turno', 'details': str(e)}), 500