# importamos flask
from flask import Flask, Blueprint

# importacion de la instancia db de SQLalchemy
from .models.models import db

# importacion de la rutas
from .routers.auth import auth
from .routers.cliente import clien
# para leer variables de entorno
import os
from dotenv import load_dotenv

# llamamos ala funcion load_dotenv para optener las variables  necesarias
load_dotenv()

# configuracion para crear una base de datos en sqlite , la base de datos se peude crear fuera de la carpeta app
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, "..", "producionDB.db")



def create_app():
    app = Flask(__name__)

    # Configura la base de datos

    # SQlite --> Para desarrollo Descomenta esta linea y comenta la configuracion para MySQl
    #app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_path
    # MySQL ---> Cuando ya esta Desplegado

    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DB')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Registrar los blueprints
    # es una forma pararegistrar que rutas deseas crear asi se evita de crear muchas rutas en un solo archivo

    app.register_blueprint(auth)
    app.register_blueprint(clien)

    return app

