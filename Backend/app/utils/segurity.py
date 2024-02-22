from werkzeug.security import check_password_hash, generate_password_hash
import jwt
import os
from flask import jsonify
import re
from datetime import datetime,timedelta

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
    now = datetime.utcnow()
    expiration = now + timedelta(hours=1)
    playload = {
        'id' : data.get('id'),
        'role': data.get('role'),
        'exp': expiration
    }
    return jwt.encode(playload, key, algorithm='HS256')


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
