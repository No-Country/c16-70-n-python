from crypt import methods
from flask_restx import Api, Resource
from flask import Blueprint, jsonify, request
from ..routers.auth import api
from ..models.models import Cliente, db

client = Blueprint("admin", __name__)

client = api.namespace("admin", description="Rutas para el modelo cliente")


# Rutas GET del cliente
@client.route("/client")
class GetClient(Resource):
    def get_client():
        client_data = Cliente.query.all()
        client_list = []
        for data in client_data:
            clients_data = {
                'id': client_data.cli_int_user_id,
                'email': client_data.email,
                'firstname': client_data.cli_str_first_name,
                'lastname': client_data.cli_str_last_name,
                'phone': client_data.cli_str_phone,
                'direction': client_data.cli_str_direction,
                'profile_image': client_data.cli_str_profile_img,
                'register_date': client_data.cli_str_register_date,
                'suspension_date': client_data.cli_date_suspension_date,
            }
        client_list.append(clients_data)
        return jsonify({'client_data': client_list})


# Rutas POST del cliente
@client.route("/cliente/post", methods=["POST"])
class Client(Resource):
    def post_client():
        pass


# Rutas PUT del cliente
@client.rout("/cliente/int:<id>", methods=["PUT"])