from flask import Blueprint, request, jsonify, current_app
from ..models.models import User, db, Cliente, Proveedor, Turn, ScoreProveedor, Ubication
from flask_restx import Api, Resource
from ..utils.segurity import descodificarPassword, codificarPassword, codificarToken, descodificarToken
import os
from datetime import datetime
from ..routers.auth import api

fecha_suspension = datetime.now()

admi = Blueprint("admin", __name__)

#api = Api(dmin, version="1.0", title="Agendify", description="Agendify API REST")

admin = api.namespace("admin", description="Rutas administrativas")


@admin.route("/clies")
class ClientsAll(Resource):
    @admin.doc(params={'page': 'Número de página', 'per_page': 'Número de elementos por página'})
    def get(self):
        """
        Retorna una lista paginada de clientes .
        Ejemplo de uso, http://127.0.0.1:42723/admin/clients?page=1
        """
        auth = request.headers.get('Authorization')

        if not auth:
            return jsonify({'message': "Token no proporcionado"})
        
        datosToken = descodificarToken(auth)
        id = datosToken.get('id')
        role = datosToken.get('role')

        try:
            if role != 'admin':
                return jsonify({'message': 'Solo los administradores pueden acceder a este recurso'})
            
            # Parámetros de paginación
            page = request.args.get('page', 1, type=int)
            per_page = request.args.get('per_page', 10, type=int)  # Cambiado a 10 por página

            exitsAdmin = User.query.filter_by(use_int_id=id, use_str_type_profile=role).first()

            if exitsAdmin is None:
                return jsonify({'message':'No estás autorizado para realizar la consulta'})

            # Calcular el índice de inicio y fin para la consulta
            start_index = (page - 1) * per_page
            end_index = start_index + per_page

            # Consulta paginada de usuarios y clientes
            users_and_clients = db.session.query(User, Cliente).join(Cliente, User.use_int_id == Cliente.cli_int_user_id).slice(start_index, end_index).all()
            
            # Convertir los resultados a un formato JSON
            results = []
            for user, client in users_and_clients:
                result_item = {
                    'user_id': user.use_int_id,
                    'email': user.use_str_email,
                    'client_id': client.cli_int_id,
                    'first_name': client.cli_str_first_name,
                    'last_name': client.cli_str_last_name,
                    'phone': client.cli_str_phone,
                    'direction': client.cli_str_direction,
                    'profile_img': client.cli_str_profile_img,
                    'register_date': client.cli_date_register_date.strftime('%Y-%m-%d'),
                    'suspension_date': client.cli_date_suspension_date.strftime('%Y-%m-%d') if client.cli_date_suspension_date else None
                }
                results.append(result_item)
            
            return jsonify({'data': results})

        except Exception as e:
            return jsonify({'message': str(e)})



@admin.route("/provs")
class ClientsAll(Resource):
    @admin.doc(params={'page': 'Número de página', 'per_page': 'Número de elementos por página'})
    def get(self):
        """
        Retorna una lista paginada de proveedores.
        Ejemplo de uso, http://127.0.0.1:42723/admin/proves?page=1
        """
        auth = request.headers.get('Authorization')

        if not auth:
            return jsonify({'message': "Token no proporcionado"})
        
        datosToken = descodificarToken(auth)
        id = datosToken.get('id')
        role = datosToken.get('role')

        try:
            if role != 'admin':
                return jsonify({'message': 'Solo los administradores pueden acceder a este recurso'})
            
            # Parámetros de paginación
            page = request.args.get('page', 1, type=int)
            per_page = request.args.get('per_page', 10, type=int)  # Cambiado a 5 por página

            exitsAdmin = User.query.filter_by(use_int_id=id, use_str_type_profile=role).first()

            if exitsAdmin is None:
                return jsonify({'message':'No estás autorizado para realizar la consulta'})

            # Calcular el índice de inicio y fin para la consulta
            start_index = (page - 1) * per_page
            end_index = start_index + per_page

            # Consulta paginada de usuarios y clientes
            users_and_proveedor = db.session.query(User, Proveedor).join(Proveedor, User.use_int_id == Proveedor.pro_int_user_id).slice(start_index, end_index).all()
            
            # Convertir los resultados a un formato JSON
            results = []
            for user, prov in users_and_proveedor:
                result_item = {
                    'user_id': user.use_int_id,
                    'email': user.use_str_email,
                    'type_profile': user.use_str_type_profile,
                    'prove_id': prov.pro_int_user_id,
                    'first_name': prov.pro_str_first_name,
                    'last_name': prov.pro_str_last_name,
                    'phone': prov.pro_str_phone,
                    'direction': prov.pro_str_direction,
                    'profile_img': prov.pro_str_profile_img,
                    'register_date': prov.pro_date_registration_date.strftime('%Y-%m-%d'),
                    'suspension_date': prov.pro_date_suspension_date.strftime('%Y-%m-%d') if prov.pro_date_suspension_date else None
                }
                results.append(result_item)
            
            return jsonify({'data': results})

        except Exception as e:
            return jsonify({'message': str(e)})



#  rutaspendiendes,para  actulizar la suspnsion de los usuarios

@admin.route("/clie/<int:id>")
class ClientID(Resource):
    def put(self, id):
        """
        Suspender La cuenta del cliente url
        """
        auth = request.headers.get('Authorization')
        
        if not auth:
            return jsonify({'message': "Token no proporcionado"})
    
        datosToken = descodificarToken(auth)
        token_id = datosToken.get('id')
        role = datosToken.get('role')

        try:

            if role != 'admin':
                return jsonify({'message': 'Solo los administradores pueden acceder a este recurso'})
            
            client = Cliente.query.filter_by(cli_int_id=id).first()
            if not client:
                return jsonify({'message': 'Cliente no encontrado'})
            
            client.cli_date_suspension_date = fecha_suspension

            db.session.commit()
            
            return jsonify({'message': 'Cliente suspendido'})
        
        except Exception as e:
            return jsonify({'message': str(e)})

#Delete Cliente 
    def delete(self, id):
        """
        Eliminar la cuenta del cliente y sus datos relacionados.
        """
        auth = request.headers.get('Authorization')
        
        if not auth:
            return jsonify({'message': "Token no proporcionado"})
    
        datosToken = descodificarToken(auth)
        token_id = datosToken.get('id')
        role = datosToken.get('role')

        try:
            if role != 'admin':
                return jsonify({'message': 'Solo los administradores pueden acceder a este recurso'})
            
            client = Cliente.query.filter_by(cli_int_id=id).first()
            if client:
                db.session.delete(client)
            else:
                return jsonify({'message': 'Cliente no encontrado'})
            
            #tabla de turnos
            turns = Turn.query.filter_by(turn_int_client_id=id).all()
            for turn in turns:
                db.session.delete(turn)
            
            # tabla de user
            user = User.query.filter_by(use_int_id=id).first()
            if user:
                db.session.delete(user)
            
            db.session.delete(client)
            db.session.commit()
            
            return jsonify({'message': 'Cliente y sus datos relacionados eliminados correctamente'})
        
        except Exception as e:
            return jsonify({'message': str(e)})



@admin.route("/prov/<int:id>")
class ProvvID(Resource):
    def put(self, id):
        """ 
        Suspender la Cuenta de un Proveedor por ID
        """
        auth = request.headers.get('Authorization')
        
        if not auth:
            return jsonify({'message': "Token no proporcionado"})
    
        datosToken = descodificarToken(auth)
        token_id = datosToken.get('id')
        role = datosToken.get('role')

        try:

            if role != 'admin':
                return jsonify({'message': 'Solo los administradores pueden acceder a este recurso'})
            
            prov = Proveedor.query.filter_by(pro_int_user_id=id).first()
            if not prov:
                return jsonify({'message': 'Proveedor no encontrado'})
            
            prov.pro_date_suspension_date = fecha_suspension
            
            db.session.commit()
            
            return jsonify({'message': 'Proveedor suspendido'})
        
        except Exception as e:
            return jsonify({'message': str(e)})
        

#Eliminar Proveedor
    def delete(self, id):
        """ 
        Eliminar la cuenta de un proveedor y sus datos relacionados.
        """
        auth = request.headers.get('Authorization')
        
        if not auth:
            return jsonify({'message': "Token no proporcionado"})
    
        datosToken = descodificarToken(auth)
        token_id = datosToken.get('id')
        role = datosToken.get('role')

        try:
            if role != 'admin':
                return jsonify({'message': 'Solo los administradores pueden acceder a este recurso'})

            prove = Proveedor.query.filter_by(pro_int_user_id =id).first()
            if prove:
                db.session.delete(prove)
            else:
                return jsonify({'message': 'Proveedor No Encontrado'})

            turns  = Turn.query.filter_by(turn_int_proveedor_id=id).all()
            for turn in turns:
                db.session.delete(turn)

            scores  = ScoreProveedor.query.filter_by(scr_int_proveedor_id=id).all()
            for score in scores:
                db.session.delete(score)

            ubications  = Ubication.query.filter_by(ubi_int_proveedor_id=id).all()
            for ubication in ubications:
                db.session.delete(ubication)

            # Eliminar el usuario asociado al proveedor
            user = User.query.filter_by(use_int_id=id).first()
            if user:
                db.session.delete(user)

            db.session.commit()
            
            return jsonify({'message': 'Datos del Proveedor fueron eliminadas'})
        
        except Exception as e:
            return jsonify({'message': str(e)})
