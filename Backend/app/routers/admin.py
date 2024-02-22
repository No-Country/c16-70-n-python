from flask import Blueprint, request, jsonify, current_app
from flask_restx import Api, Resource
from ..utils.segurity import descodificarPassword, codificarPassword, codificarToken, descodificarToken
import os
from datetime import datetime
from ..routers.auth import api
from ..models.models import User, db, Turn

fecha_suspension = datetime.now()

admi = Blueprint("admin", __name__)

admin = api.namespace("admin", description="Rutas administrativas")

###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
#Mostrar lista de Pacientes
@admin.route("/pacientes")
class PacientesAll(Resource):
    def get(self):
        """ 
        Obtener Lisado de Paciente 
        Ejemplo: http://127.0.0.1:40709/admin//pacientes?page=1

        """
        auth = request.headers.get('Authorization')

        if not auth:
            return jsonify({'message': "Token no proporcionado"})


        datosToken = descodificarToken(auth)
        id = datosToken.get('id')
        role = datosToken.get('role')


        try:
            if role != 'Admin':
                return jsonify({'message': 'No Estas Autorizado'})
        
            # Paginacion
            page = request.args.get('page', 1, type=int)
            per_page = request.args.get('per_page', 10, type=int)

            exitsAdmin = User.query.filter_by(use_int_id=id, use_str_role=role).first()

            if exitsAdmin is None:
                return jsonify({'message':'No estás autorizado'})

            users = User.query.paginate(page=page, per_page=per_page, error_out=False)
            #

            formatted_users = []
            for user in users.items:
                formatted_user = {
                    'id': user.use_int_id,
                    'email': user.use_str_email,
                    'first_name': user.use_str_first_name,
                    'last_name': user.use_str_last_name,
                    'phone': user.use_str_phone,
                    'profile_img': user.use_str_profile_img,
                    'register_date': user.use_date_register_date.strftime('%Y-%m-%d %H:%M:%S'),
                    'suspension': user.use_date_suspension,
                    'suspension_date': user.use_date_suspension_date.strftime('%Y-%m-%d %H:%M:%S') if user.use_date_suspension_date else None,
                    'role': user.use_str_role
                }
                formatted_users.append(formatted_user)

            return jsonify(formatted_users)
        except Exception as e:
            return jsonify({'message': str(e)})

###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
#Detalles de un cliente, Actualizar y Borrar
@admin.route("/paciente/<int:id>")
class PacientesAll(Resource):
    def get(self, id):
        """ 
        Ver Detalles del Paciente de Forma Individual
        """
        auth = request.headers.get('Authorization')
        
        if not auth:
            return jsonify({'message': "Token no proporcionado"}), 401
    
        datosToken = descodificarToken(auth)
        token_id = datosToken.get('id')
        role = datosToken.get('role')

        try:
            # Verificar si el usuario tiene permiso para acceder a la información del paciente
            user = User.query.filter_by(use_int_id=token_id, use_str_role=role).first()
            if not user:
                return jsonify({'message': 'No estás autorizado'}), 403
            
            # Buscar al paciente por su ID
            paciente = User.query.get(id)
            if not paciente:
                return jsonify({'message': 'Paciente no encontrado'}), 404
            
            return jsonify({
                'id': paciente.use_int_id,
                'email': paciente.use_str_email,
                'first_name': paciente.use_str_first_name,
                'last_name': paciente.use_str_last_name,
                'phone': paciente.use_str_phone,
                'img': paciente.use_str_profile_img,
                'data_reister': paciente.use_date_register_date,
                'suspension': paciente.use_date_suspension,
                'data_suspension': paciente.use_date_suspension_date,
                'role': paciente.use_str_role
            })
            
        except Exception as e:
            return jsonify({'message': str(e)})
###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
    def put(self, id):
        """ 
        Suspender Paciente
        """
        auth = request.headers.get('Authorization')
        data = request.get_json()
        suspender = data.get("suspender")
        
        if not auth:
            return jsonify({'message': "Token no proporcionado"})

        if not data:
            return jsonify({'message': "Datos no proporcionados en formato JSON"})


        datosToken = descodificarToken(auth)
        token_id = datosToken.get('id')
        role = datosToken.get('role')

        try:
            # Verificar si el usuario tiene permiso para acceder a la información del paciente
            user = User.query.filter_by(use_int_id=token_id, use_str_role=role).first()
            if not user:
                return jsonify({'message': 'No estás autorizado'})
            
            # Buscar al paciente por su ID
            paciente = User.query.get(id)
            if not paciente:
                return jsonify({'message': 'Paciente no encontrado'})

            if suspender in ['True', 'False']:
                paciente.use_date_suspension = suspender == 'True'
                paciente.use_date_suspension_date = datetime.now() if suspender == 'True' else None

                db.session.commit()
            
                return jsonify({'message': 'Cliente actualizado'})
        
        except Exception as e:
            return jsonify({'message': str(e)})
###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
    def delete(self,id):
        """ 
        Eliminar Paciente
        """
        auth = request.headers.get('Authorization')
    
        if not auth:
            return jsonify({'message': "Token no proporcionado"})

        datosToken = descodificarToken(auth)
        token_id = datosToken.get('id')
        role = datosToken.get('role')

        try:
            # Verificar si el usuario tiene permiso para eliminar pacientes
            user = User.query.filter_by(use_int_id=token_id, use_str_role=role).first()
            if not user:
                return jsonify({'message': 'No estás autorizado'})
        
            # Buscar al paciente por su ID
            paciente = User.query.get(id)
            if not paciente:
                return jsonify({'message': 'Paciente no encontrado'})

            citas = Turn.query.filter_by(turn_int_client_id=id).all()
            for cita in citas:
                db.session.delete(cita)

            db.session.delete(paciente)
            db.session.commit()
        
            return jsonify({'message': 'Cliente eliminado correctamente'})
    
        except Exception as e:
            return jsonify({'message': str(e)}), 500
###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################

#Lista de Turnos 
@admin.route("/turnos")
class Turnos(Resource):
    def get(self):
        pass
###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
#crear turno
@admin.route("/turnos")
class TurnoCrear(Resource):
    def post(self):
        pass


###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
# Obtener Detalles de un turno , actualizarlo y Borrarlo
@admin.route("/turnos/<int:id>")
class TurnoCrear(Resource):
    def get(self):
        pass
###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
    def put(self):
        pass
###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
    def delete(self):
        pass
###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
#End Point Servicio
@admin.route("/servicios")
class Servicios(Resource):
    def get(self):
        pass
###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
    # Crear Servicio
    def post(self):
        pass

