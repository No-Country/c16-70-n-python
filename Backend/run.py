# importamos la funcion create_app() y la instancia db para crear las tablas automaticamente cuando se inicia Flask
# comando para correr flask  --> python run.py --debug
# si tienen problemas con el puerto escriban dentro de (app.run (debug=True port=0))
# automaticamente flask podra inciar en un puerto de forma aleatoria
from app import create_app, db

app = create_app()

# Endpoint de prueba
@app.route("/hello")
def hello():
    return  "Hello, World!"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=0)