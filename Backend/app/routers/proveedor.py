from flask_restx import Api, Resource
from flask import Blueprint, jsonify, request
from ..routers.auth import api,descodificarToken
from ..models.models import User, Proveedor, db
from datetime import datetime

prove= Blueprint("prove",__name__)

prov = api.namespace("prove", description="Rutas para proveedor")

#arranco a escribir rutas para obtener info del proovedor
@prov.route("/get")
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
                        'register_date': data.pro_date_registration_date,
                        'suspension_date': data.pro_date_suspension_date,
                    }
                    suppliter_list.append(suppliter_data)
                return jsonify(suppliter_data)
            else:
                print(f"id {id} de usuario no encontrado en la base")
                return jsonify({"menssage":"No se encontro un proovedor asociado al usuario"})
        except Exception as db:
            print("Error",db)
            return jsonify({"menssage":"error al conectarse con la DB"})
        
@prov.route("/put")
class PostSuppliter(Resource):

    def put(self):
        #solicitud de Token
        auth = request.headers.get('Authorization')

        data = request.get_json()
        firstname = data.get("firstname")
        lastname = data.get("lastname")
        phone = data.get("phone")
        direction = data.get("direction")

        if not auth:
            return jsonify({"menssage": "Token no proporcionado"})
        
        datostoken = descodificarToken(auth)
        id = datostoken.get('id')
        #tengo dudas con que id usar para la consulta 

        try:
            supplier = Proveedor.query.filter_by(pro_int_user_id=id).first()

            if supplier:
                supplier.pro_str_first_name = firstname
                supplier.pro_str_last_name = lastname
                supplier.pro_str_phone = phone
                supplier.pro_str_direction = direction
                db.session.commit()
                return jsonify({"message": "Proveedor actualizado correctamente"})
            else:
                return jsonify({"message": "Proveedor no encontrado"})
        except Exception as e:
            print("Error:", e)
            return jsonify({"message": "Error al actualizar el proveedor"})


@prov.route("/turn")
class UpgradeProveedorTurn(Resource):
    def get(self):
        pass

@prov.route("/put")
class UpgradeProveedorTurn(Resource):
    def post(self):
        pass



# Obtener los turnos por id   Orlando
# actualizar infor del turno Orlando
# borrar turno orlando Orlando
# crear servicio == categoria orlando
# obtener categorias   
# obtener ubicacion    fernando 
# crear Ubicacion      fernando
# actualizar ubicacion fernando
# delete ubicacion     orlando


