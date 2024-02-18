from crypt import methods
from flask_restx import Api, Resource
from flask import Blueprint, jsonify, request
from ..routers.auth import api
from ..models.models import Cliente, db

clien = Blueprint("client", __name__)

client = api.namespace("client", description="Rutas para el modelo cliente")


# Rutas GET del cliente
@client.route("")
class GetClient(Resource):
    def get(self):
        client_data = Cliente.query.all()
        client_list = []

        for data in client_data:
            clients_data = {
                'id': data.cli_int_user_id,
                'firstname': data.cli_str_first_name,
                'lastname': data.cli_str_last_name,
                'phone': data.cli_str_phone,
                'direction': data.cli_str_direction,
                'profile_image': data.cli_str_profile_img,
                'register_date': data.cli_date_register_date,
                'suspension_date': data.cli_date_suspension_date,
            }
            client_list.append(clients_data)
        return jsonify(client_list)


# Rutas POST del cliente
@client.route("/post")
class Client(Resource):
    def post(self):
        pass


# Rutas PUT del cliente
#@client.rout("/cliente/int:<id>", methods=["PUT"])