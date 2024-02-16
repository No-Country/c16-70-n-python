from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    
# Doc : https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#simple-example