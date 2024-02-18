from crypt import methods
from flask_restx import Api, Resource
from flask import Blueprint, jsonify, request
from ..routers.auth import api
from ..models.models import Cliente, db

clien = Blueprint("client", __name__)

client = api.namespace("client", description="Rutas para el modelo cliente")


# Rutas GET del cliente
<<<<<<< HEAD
@client.route("/")
=======
@client.route("")
>>>>>>> ddda51fab00c7e86548907674a749b18bf1c42be
class GetClient(Resource):
    def get(self):
        client_data = Cliente.query.all()
        
        if client_data.cli_int_user_id in client_data:
            return jsonify({'mensaje':'Usuario ya esta registrado'})
        
        client_list = []

        for data in client_data:
            clients_data = {
<<<<<<< HEAD
                'id': data.cli_int_id,
                'user_id': data.cli_int_user_id,
=======
                'id': data.cli_int_user_id,
>>>>>>> ddda51fab00c7e86548907674a749b18bf1c42be
                'firstname': data.cli_str_first_name,
                'lastname': data.cli_str_last_name,
                'phone': data.cli_str_phone,
                'direction': data.cli_str_direction,
                'profile_image': data.cli_str_profile_img,
<<<<<<< HEAD
                'register_date': data.cli_str_register_date,
                'suspension_date': data.cli_date_suspension_date,
            }
            client_list.append(clients_data)
        return jsonify({'client_data': client_list})
=======
                'register_date': data.cli_date_register_date,
                'suspension_date': data.cli_date_suspension_date,
            }
            client_list.append(clients_data)
        return jsonify(client_list)
>>>>>>> ddda51fab00c7e86548907674a749b18bf1c42be

def get_users():
    users = User.query.all()
    user_list = []
    for user in users:
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }
        user_list.append(user_data)
    return jsonify({'users': user_list})

# Rutas POST del cliente
@client.route("/post")
class Client(Resource):
    def post(self):
        pass


# Rutas PUT del cliente
<<<<<<< HEAD
#@client.rout("/cliente/int:<id>")

=======
#@client.rout("/cliente/int:<id>", methods=["PUT"])
>>>>>>> ddda51fab00c7e86548907674a749b18bf1c42be
