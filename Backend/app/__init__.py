# importamos flask
from flask import Flask, Blueprint

# importacion de la instancia db de SQLalchemy
from .models.models import db
from .routers.auth import auth
# from .routers.cliente import clien
# from .routers.admin import admi
# from .routers.proveedor import prove
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
    
    # SQlite --> Para desarrollo Descomenta esta linea y comenta la configuracion para MySQl
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_path
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_size': 20,
    'pool_timeout': 30, 
    }

    # MySQL ---> Cuando ya esta Desplegado


    #app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DB')}"
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)


    app.register_blueprint(auth)
    # app.register_blueprint(clien)
    # app.register_blueprint(admi)
    # app.register_blueprint(prove)

    return app

