#importamos lo que es Flas Rext , algo asi
from flask_restx import Api, Resource
from flask import Blueprint, jsonify , request
from ..routers.auth import api


# se crean las instancias para la documentacion 
# auth ya existe  asi que vamos a  reemplazarlo con admin
admi = Blueprint('admi', __name__) # esto es el que se debe de importar en el__init__.py dentro de app

# la variable api solo se crea una vez como se creo primero la ruta auth vamos a importarla desde from ..routers.auth import api que fue la primera ruta creada
# no pueden existir dos ya que seria una especie de titulo o algo parecido en la Documentacion


admin = api.namespace ('admin', description= 'Rutas para Admin')

#  luego de esto se deben crear los Endpoint , dejo uno vacio como emeplo.

@admin.route('')
class Admin(Resource):
    def post(self):
        pass

@admin.route('/get')
class AdminGet(Resource):
    def get(self):
        pass

@admin.route('/update', methods=["PUT"])
class AdminGet(Resource):
    def put(self):
        pass