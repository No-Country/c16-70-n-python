from flask import Blueprint, request, jsonify, current_app
from ..models.models import User, db
from flask_restx import Api, Resource
from ..utils.segurity import descodificarPassword, codificarPassword, codificarToken, descodificarToken
# import os
from datetime import datetime
import traceback

fecha_registro = datetime.now()

auth = Blueprint("auth", __name__)

api = Api(auth, version="1.0", title="Agendify", description="Agendify API REST")

autho = api.namespace("auth", description="Rutas para Autotificacion")


###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
# @app.errorhandler(404)
#@auth.doc(description="")
#@auth.doc(params={
#})
@autho.route("/register")
class Users(Resource):
    @autho.doc(
        description="Registrar un nuevo usuario.",
        params={
            'email': 'El correo electrónico del usuario a registrar.',
            'password': 'La contraseña del usuario a registrar.'
        },
        responses={
            200: 'Éxito. El usuario fue creado exitosamente.',
            400: 'Error de solicitud. El correo electrónico ya está en uso o los datos de entrada son inválidos.',
            500: 'Error del servidor. No se pudo completar la solicitud debido a un problema en el servidor.'
        }
    )
    #@app.errorhandler(404)
    def post(self):
        """
        Registrar Usuario *
        """
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")
        """ esto esta comentado para probar despues
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        phone = data.get("phone")
        """

        try:
            exitsEmail = User.query.filter_by(use_str_email=email).first()
            # esta funcion es para cree un admin mientras estamos en produccion sino existe
            User.ensure_admin_exists()
            if exitsEmail:
                return jsonify({"message": "El correo electrónico ya está en uso. Por favor, utilice otro."})

            passwordH = codificarPassword(password)
            new_user = User(use_str_email=email,
                            use_str_password=passwordH,
                            use_date_register_date=fecha_registro,
                            #use_str_first_name=first_name,
                            #use_str_last_name=last_name,
                            #use_str_phone=phone
                            )
            db.session.add(new_user)
            db.session.commit()

            return jsonify({"message": "El usuario fue creado exitosamente"})

        except Exception as e:
            print("Error:", e)
            return jsonify({"message": "Error al conectarse con la BD"})
###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
# Login
@autho.route("/login")
class Login(Resource):
    @autho.doc(
        description="Iniciar sesión de usuario.",
        params={
            'email': 'El correo electrónico del usuario para iniciar sesión.',
            'password': 'La contraseña del usuario para iniciar sesión.'
        },
        responses={
            200: 'Éxito. La autenticación fue exitosa y se ha generado un token de acceso.',
            400: 'Error de solicitud. El correo electrónico o la contraseña proporcionados son incorrectos.',
            500: 'Error del servidor. No se pudo completar la solicitud debido a un problema en el servidor.'
        }
    )
    def post(self):
        """
        Login de Usuario *
        """
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        try:
            exitsEmail = User.query.filter_by(use_str_email=email).first()

            if exitsEmail:
                passwordDB = exitsEmail.use_str_password
                compararPassword = descodificarPassword(password=password, passwordDB=passwordDB)
#se le agrego una sangria extra al if compararPassword.
                if compararPassword:
                    id = exitsEmail.use_int_id
                    role = exitsEmail.use_str_role

                    print(role)

                    token = codificarToken({'id': id, 'role': role})

                    #print(token)
                    return jsonify({'token': token})

                else:
                    return jsonify({'message': 'Datos incorrectos'})

        except Exception as e:
            error_message = {
                "error_type": type(e).__name__,
                "error_message": str(e),
                "stack_trace": traceback.format_exc(),
                }
            print("Error:", error_message)
            return jsonify({"message": "Error en el Servidor", "error": error_message})
    #    except Exception as e:
    #        print("Error:", e)
    #        return jsonify({"message": "Error en el Servidorr"})
###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
#route de ejemplo
@autho.route("/rol")
class Token(Resource):
    @autho.doc(
        description="Muestra el tipo de rol que posee el usuario",
        params={
            'Authorization': {'description': 'El token de acceso del usuario.', 'type': 'string', 'required': True}
        },
        responses={
            200: 'Éxito. Se devuelve el tipo de rol del usuario.',
            401: 'Error de autenticación. El token de acceso no se proporcionó correctamente o no es válido.',
            500: 'Error del servidor. No se pudo completar la solicitud debido a un problema en el servidor.'
        }
    )
    def post(self):
        """
        Conocer el del Usuario Rol *
        """
        auth = request.headers.get('Authorization')
        if not auth:
            return jsonify({"message": "Token no proporcionado"})

        datosToken = descodificarToken(auth)
        id = datosToken.get('id')
        role = datosToken.get('role')
        print (role)

        try:
            consulta = User.query.filter_by(use_int_id=id, use_str_role=role).first()

            if consulta:
                return jsonify({'role':consulta.use_str_role})

        except Exception as e:
            print("Error:", e)
            return jsonify({"message": "Error En el Servidor"})


