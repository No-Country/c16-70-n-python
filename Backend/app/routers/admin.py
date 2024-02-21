from flask import Blueprint, request, jsonify, current_app
from ..models.models import User, db, Cliente, Proveedor
from flask_restx import Api, Resource
from ..utils.segurity import descodificarPassword, codificarPassword, codificarToken, descodificarToken
import os
from datetime import datetime
from ..routers.auth import api

fecha_registro = datetime.now()

admi = Blueprint("admin", __name__)

#api = Api(dmin, version="1.0", title="Agendify", description="Agendify API REST")

admin = api.namespace("admin", description="Rutas administrativas")


@admin.route("/clients")
class ClientsAll(Resource):
    @admin.doc(params={'page': 'Número de página', 'per_page': 'Número de elementos por página'})
    def get(self):
        """
        Retorna una lista paginada de clientes y usuarios.
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
            per_page = request.args.get('per_page', 5, type=int)  # Cambiado a 5 por página

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
                    'password': user.use_str_password,
                    'type_profile': user.use_str_type_profile,
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

