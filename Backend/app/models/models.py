from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from flask import Blueprint, request, jsonify, current_app

db = SQLAlchemy()

fecha_registro = datetime.now()


# ejemplo 

# Doc: https://flask-sqlalchemy.palletsprojects.com/en/2.x/models simple-example


class User(db.Model):
    __tablename__ = "user"
    use_int_id = db.Column(db.Integer, primary_key=True, unique=True)
    use_str_email = db.Column(db.String(120), unique=True)
    use_str_password = db.Column(db.String(128), nullable=False)
    use_str_type_profile = db.Column(db.String(5), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.use_str_email
    
class Proveedor(db.Model):
    __tablename__ = "proveedor"
    pro_int_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pro_int_user_id = db.Column(db.Integer, db.ForeignKey("user.use_int_id"))
    pro_str_first_name = db.Column(db.String(100), nullable=True)
    pro_str_last_name = db.Column(db.String(100),nullable=True)
    pro_str_phone = db.Column(db.String(20), nullable=True)
    pro_str_direction = db.Column(db.String(200), nullable=True)
    pro_str_profile_img = db.Column(db.String(200), nullable=True)
    pro_date_registration_date = db.Column(db.Date)
    pro_date_suspension_date = db.Column(db.Date, nullable=True)

    # Definición de la relación con Users
    user = db.relationship("User", backref="proveedor")

    #Metodo para guardar img
    def save_pro_str_profile_img(self, picture):
        if picture:
            picture_filename = f"user_{self.pro_int_user_id}_pro_str_profile_img.jpg"
            picture_path = os.path.join(current_app.root_path, 'static/pro_str_profile_imgs', picture_filename)

            os.makedirs(os.path.dirname(picture_path), exist_ok=True)

            picture.save(picture_path)
            self.pro_str_profile_img = f"profile_pictures/{picture_filename}"
            db.session.commit()

    def get_pro_str_profile_img_url(self):
        if self.pro_str_profile_img:
            return f"{request.url_root}static/{self.pro_str_profile_img}"
        else:
            return None

    def delete_profile_img(self):
        if self.pro_str_profile_img:
            # Eliminar la imagen del sistema de archivos
            img_path = os.path.join(current_app.root_path, 'static', self.pro_str_profile_img)
            if os.path.exists(img_path):
                os.remove(img_path)
            # Actualizar la base de datos
            self.pro_str_profile_img = None
            db.session.commit()

class Cliente(db.Model):
    __tablename__ = "cliente"
    cli_int_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cli_int_user_id = db.Column(db.Integer, db.ForeignKey("user.use_int_id"))
    cli_str_first_name = db.Column(db.String(100),nullable=True)
    cli_str_last_name = db.Column(db.String(100), nullable=True)
    cli_str_phone = db.Column(db.String(15), nullable=True)
    cli_str_direction = db.Column(db.String(100), nullable=True)
    cli_str_profile_img = db.Column(db.String(200), nullable=True)
    cli_date_register_date = db.Column(db.Date)
    cli_date_suspension_date = db.Column(db.Date, nullable=True)

    # Definición de la relación con Users
    user = db.relationship("User", backref="cliente")

    #metodo para guardar imagen de cliente
    def save_cli_str_profile_img(self, picture):
        if picture:
            picture_filename = f"user_{self.cli_int_user_id}_cli_str_profile_img.jpg"
            picture_path = os.path.join(current_app.root_path, 'static/cli_str_profile_imgs', picture_filename)

            os.makedirs(os.path.dirname(picture_path), exist_ok=True)

            picture.save(picture_path)
            self.cli_str_profile_img = f"profile_pictures/{picture_filename}"
            db.session.commit()

    def delete_profile_img(self):
        if self.cli_str_profile_img:
            # Eliminar la imagen del sistema de archivos
            img_path = os.path.join(current_app.root_path, 'static', self.cli_str_profile_img)
            if os.path.exists(img_path):
                os.remove(img_path)
            # Actualizar la base de datos
            self.cli_str_profile_img = None
            db.session.commit()

class ScoreProveedor(db.Model):
    __tablename__ = "score_proveedor"
    scr_int_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    scr_int_proveedor_id = db.Column(db.Integer, db.ForeignKey("proveedor.pro_int_id"))
    scr_int_cliente_id = db.Column(db.Integer, db.ForeignKey("cliente.cli_int_id"))
    scr_int_score = db.Column(db.Integer)
    scr_str_comment = db.Column(db.String(255))

    # Definición de la relación con Proveedor
    proveedor = db.relationship("Proveedor", backref="score_proveedor")

    # Definición de la relación con Cliente
    cliente = db.relationship("Cliente", backref="score_proveedor")


class Categories(db.Model):
    __tablename__ = "categories"
    cat_int_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cat_str_category_name = db.Column(db.String(100))


class Ubication(db.Model):
    __tablename__ = "ubication"
    ubi_int_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ubi_int_proveedor_id = db.Column(db.Integer, db.ForeignKey("proveedor.pro_int_id"))
    ubi_str_ubication = db.Column(db.String(100))  # Added length
    ubi_str_direction = db.Column(db.String(200))  # Added length


class Turn(db.Model):
    __tablename__ = "turn"
    turn_int_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    turn_int_proveedor_id = db.Column(db.Integer, db.ForeignKey("proveedor.pro_int_id"))
    turn_int_client_id = db.Column(db.Integer, db.ForeignKey("cliente.cli_int_id"))
    turn_int_category_id = db.Column(db.Integer, db.ForeignKey("categories.cat_int_id"))
    turn_int_ubication_id = db.Column(db.Integer, db.ForeignKey("ubication.ubi_int_id"))
    turn_str_name_turn = db.Column(db.String(100))
    turn_str_description = db.Column(db.String(200))
    turn_date_creation_date = db.Column(db.Date)
    turn_date_date_assignment = db.Column(db.Date)
    turn_time_start_turn = db.Column(db.Time)
    turn_time_finish_turn = db.Column(db.Time)
    turn_bol_assigned = db.Column(db.Boolean, default=False)