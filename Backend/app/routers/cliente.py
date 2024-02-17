from flask_restx import Api, Resource
from flask import Blueprint, jsonify, request
from ..routers.auth import api

client = Blueprint("admin", __name__)

client = api.namespace("admin", description="Rutas para el modelo cliente")


# Rutas para obtener la informacion del cliente
@client.route("/client")
class GetClient(Resource):
    def get_client():
        pass


# Ruta para crear usuarios
@client.route("/cliente/post", methods=["POST"])
class Client(Resource):
    def post_client():
        pass
