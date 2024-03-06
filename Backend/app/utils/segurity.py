from werkzeug.security import check_password_hash, generate_password_hash
import jwt
import os
from flask import jsonify, request
import re
from datetime import datetime,timedelta


#key = os.getenv('KEY')
#openssl rand -hex 32
key = "acd69e5a9bff4f5fbf7f2cad8ee4cfa260d1a500ceeb972d58c0e1229ed91d40"
# modulos para incryptar la password
def codificarPassword(password):
    resp = generate_password_hash(password)
    return resp


def descodificarPassword(password, passwordDB):
    resp = check_password_hash(passwordDB, password)
    return resp


# recomendacion usar Token para Autorizacion de usuario y consumir los Endpoints

def codificarToken(data):
    now = datetime.utcnow()
    expiration = now + timedelta(hours=10)
    #
    id= data.get('id')
    role= data.get('role')
    #
    playload = {
        'id' : id,
        'role': role,
        'exp': expiration
    }
    return jwt.encode(playload, key, algorithm='HS256')

# Verificacion de Token
def verify_token():
    # Solicitud de Token
        auth = request.headers.get('Authorization')
        if not auth:
            return jsonify({"message": "Token no proporcionado"})

        datosToken = descodificarToken(auth)
        return datosToken

###
def descodificarToken(token):
    token_parts = token.split()
    if len(token_parts) != 2 or token_parts[0].lower() != 'bearer':
        return jsonify({'message': 'El Token es Invalido'})

    token = token_parts[1]
    try:
        payload = jwt.decode(token, key, algorithms=['HS256'])
        # Verificar si el token ha expirado
        if 'exp' in payload and datetime.utcnow() > datetime.utcfromtimestamp(payload['exp']):
            return {'message': 'Token expirado'}
        return payload
    except jwt.ExpiredSignatureError:
        return {'message': 'Token expirado'}
    except Exception as e:
        return {'message': 'Error en el servidor', 'error': str(e)}

#
def secure_filename(filename):
    """
    Función para generar un nombre de archivo seguro.

    Args:
        filename (str): El nombre de archivo original.

    Returns:
        str: El nombre de archivo seguro.
    """
    # Remueve caracteres no seguros
    filename = re.sub(r'[^\w\s-]', '', filename)
    # Reemplaza espacios con guiones
    filename = re.sub(r'\s+', '-', filename)
    return filename
