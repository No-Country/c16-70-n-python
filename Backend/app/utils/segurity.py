from werkzeug.security import check_password_hash, generate_password_hash
import jwt
import os
from flask import jsonify
import re


key = os.getenv('KEY')

# modulos para incryptar la password
def codificarPassword(password):
    resp = generate_password_hash(password)
    return resp


def descodificarPassword(password, passwordDB):
    resp = check_password_hash(passwordDB, password)
    return resp


# recomendacion usar Token para Autorizacion de usuario y consumir los Endpoints

def codificarToken(data):
    playload = {
        'id' : data.get('id'),
        'role': data.get('role')
    }
    return jwt.encode(playload, key, algorithm='HS256')


###
def descodificarToken(token):
    token_parts = token.split()
    if len(token_parts) != 2 or token_parts[0].lower() != 'bearer':
        return jsonify({'message': 'El Token es Invalido'}), 401
    
    token = token_parts[1]

    try:
        payload = jwt.decode(token, key, algorithms='HS256')

        return (payload)
    ###
    except jwt.ExpiredSignatureError:
         return {'message': 'Token expirado, inicie sesión nuevamente'}, 401
    except jwt.InvalidTokenError:
        return {'message': 'Token inválido'}, 401
    except Exception as e:
        return {'message': 'Error en el servidor', 'error': str(e)}, 500



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
