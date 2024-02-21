from flask_restx import Api, Resource
from flask import Blueprint, jsonify, request
from ..routers.auth import api,descodificarToken
from ..models.models import User, Proveedor, db
from datetime import datetime

suppl= Blueprint("supplier",__name__)

supplier = api.namespace("supplier", description="Rutas para proveedor")

#arranco a escribir rutas para obtener info del proovedor
@supplier.route("/get")
class GetDataSupplier(Resource):
    def get(self):
        #solicitud de Token
        auth = request.headers.get('Authorization')
        if not auth:
            return jsonify({"menssage": "Token no proporcionado"})
        
        datostoken = descodificarToken(auth)
        id = datostoken.get('id')

        try:
            #llenamos la suppliter_list con los datos del proovedor
            suppliter_data = Proveedor.query.filter_by(pro_int_user_id=id).all()
            if suppliter_data:    
                suppliter_list = []
                for data in suppliter_data:
                    suppliter_data = {
                        'firstname': data.pro_str_first_name,
                        'lastname': data.pro_str_last_name,
                        'phone': data.pro_str_phone,
                        'direction': data.pro_str_direction,
                        'profile_image': data.pro_str_profile_img,
                        'register_date': data.pro_date_register_date,
                        'suspension_date': data.pro_date_suspension_date,
                    }
                    suppliter_list.append(suppliter_list)
                return jsonify({'users':suppliter_list})
            else:
                print(f"id {id} de usuario no encontrado en la base")
                return jsonify({"menssage":"No se encontro un proovedor asociado al usuario"})
        except Exception as db:
            print("Error",db)
            return jsonify({"menssage":"error al conectarse con la DB"})
        
@supplier.route("put")
class PostSuppliter(Resource):
    def put(self):
        data = request.get_json()
        user_id = data.get("iduser")
        firstname = data.get("firstname")
        lastname = data.get("lastname")
        phone = data.get("phone")
        direction = data.get("direction")
        profile_image = data.get("profile_image")
        date_suspension = data.get("date_suspension")

        try:
            supplier = Proveedor.query.filter_by(pro_int_user_id=user_id).first()

            if supplier:
                supplier.pro_str_first_name = firstname
                supplier.pro_str_lastname = lastname
                supplier.pro_str_phone = phone
                supplier.pro_str_direction = direction
                supplier.pro_str_profile_img = profile_image
                supplier.pro_date_suspension_date = date_suspension
                db.session.commit()
                return jsonify({"message": "Proveedor actualizado correctamente"})
            else:
                return jsonify({"message": "Proveedor no encontrado"})
        except Exception as e:
            print("Error:", e)
            return jsonify({"message": "Error al actualizar el proveedor"})



