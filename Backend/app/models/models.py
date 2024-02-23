from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from flask import Blueprint, request, jsonify, current_app
from ..utils.segurity import codificarPassword

db = SQLAlchemy()

# ejemplo 
# Doc: https://flask-sqlalchemy.palletsprojects.com/en/2.x/models simple-example

# se junto los datosque serepiten en unasolatabla
# el usuario que se registre automaticamente rendra el rol de Paciente

class User(db.Model):
    __tablename__ = "user"
    use_int_id = db.Column(db.Integer, primary_key=True, unique=True)
    use_str_email = db.Column(db.String(120), unique=True)
    use_str_password = db.Column(db.String(128), nullable=False)
    use_str_first_name = db.Column(db.String(100),nullable=True, default= '')
    use_str_last_name = db.Column(db.String(100), nullable=True, default= '')
    use_str_phone = db.Column(db.String(15), nullable=True, default= '')
    use_str_profile_img = db.Column(db.String(200), nullable=True, default= 'profile_pictures/logo.png')
    use_date_register_date = db.Column(db.DateTime)
    use_bol_suspension = db.Column(db.Boolean, default=False)
    use_date_suspension_date = db.Column(db.DateTime, nullable=True)
    use_str_role = db.Column(db.String(50), default="Paciente") 

    def __repr__(self):
        return '<User %r>' % self.use_str_email

# Metodos .... 
    
    # 1-) Metodo para que el backEnd coloque la hora de registro
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.set_register_date()  # Llama al método para establecer la hora de registro

    def set_register_date(self):
        self.use_date_register_date = datetime.now() 

    # 2-) Metodo para guardar la imagen de perfil se mejoro el nombre de la imagen y carpeta
    def save_use_str_profile_img(self, picture):
        if picture:
            picture_filename = f"user_{self.use_int_id}_img.jpg"
            picture_path = os.path.join(current_app.root_path, 'static/imgs', picture_filename)

            os.makedirs(os.path.dirname(picture_path), exist_ok=True)

            picture.save(picture_path)
            self.use_str_profile_img = f"profile_pictures/{picture_filename}"
            db.session.commit()

    # 3-) Se debe revisar este metodo es para eliminar la imagen por defecto
    def delete_profile_img(self):
        if self.use_str_profile_img:
            img_path = os.path.join(current_app.root_path, 'static', self.use_str_profile_img)
            if os.path.exists(img_path):
                os.remove(img_path)

            self.use_str_profile_img = None
            db.session.commit()

    #4-) Metodo para crear un admin por defecto crea uno con el email,password, y role
    @classmethod
    def ensure_admin_exists(cls):
        admin = cls.query.filter_by(use_str_role='Admin').first()
        if not admin:
            # Si no existe un administrador, crea uno automáticamente
            passwordAdmin = 'admin'
            password = codificarPassword(passwordAdmin)
            admin = cls(
                use_str_email='admin@admin.com',
                use_str_password=password,
                use_str_role='Admin'
            )
            db.session.add(admin)
            db.session.commit()


# tablaServices
class Services(db.Model):
    __tablename__ = "services"
    ser_int_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ser_str_category_name = db.Column(db.String(100))

# Tabla Turn
class Turn(db.Model):
    __tablename__ = "turn"
    turn_int_id = db.Column(db.Integer, primary_key=True, autoincrement=True) # queda
    service_id = db.Column(db.Integer, db.ForeignKey("services.ser_int_id")) # queda
    turn_int_user_id = db.Column(db.Integer, db.ForeignKey("user.use_int_id")) #queda
    turn_str_name_turn = db.Column(db.String(100)) # dia 
    turn_str_description = db.Column(db.String(200)) # No va 
    turn_date_creation_date = db.Column(db.Date) # Paciente, solo love el Cliente
    turn_date_date_assignment = db.Column(db.Date) # No va, 
    turn_time_start_turn = db.Column(db.Time)  # ver Cliente, Admin. Hora que inicia 
    turn_time_finish_turn = db.Column(db.Time)  # ver Admin , ver Cliente pasarlo como a boleano .
    turn_bol_assigned = db.Column(db.Boolean, default=False) # Si asignado .   # se debe crear una columna mas tipo boolean para finalizar el turno
    
    service = db.relationship("Services", backref="turns")

    #metodo para que tambien se vea la categoria del Turno 
    def get_service_info(self):
        return {
            'category_name': self.service.ser_str_category_name,
        }
    

class Generador_turn(db.Model):
    gnt_str_dia = db.Column(db.String(100)) # lunes/martes/miercoles/jueves
    gnt_str_horainicio = db.Column(db.String(100)) # hora inicio de dispo
    gnt_str_horafin = db.Column(db.String(100)) # hora fin de dispo
    gnt_str_duracionturn = db.Column(db.String(100)) # duracion de turnos

