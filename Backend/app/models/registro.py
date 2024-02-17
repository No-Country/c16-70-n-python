from flask import Blueprint, request, redirect, url_for, render_template
from .models import User, Proveedor, Cliente, db

registro_bp = Blueprint('registro', __name__)

@registro_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        correo = request.form.get('correo')
        contrasena = request.form.get('contrasena')
        tipo_perfil = request.form.get('tipo_perfil')

        # Verificar si el correo ya está registrado
        if User.query.filter_by(correo=correo).first():
            return 'El correo ya está registrado.'

        # Crear un nuevo usuario
        nuevo_usuario = User(nombre=nombre, correo=correo, tipo_perfil=tipo_perfil)
        nuevo_usuario.set_password(contrasena)  # Suponiendo que tienes un método para hashear la contraseña
        db.session.add(nuevo_usuario)
        db.session.commit()

        if tipo_perfil == 'proveedor':
            # Redirigir al registro de proveedor
            return redirect(url_for('registro.registro_proveedor', user_id=nuevo_usuario.id))
        elif tipo_perfil == 'cliente':
            # Redirigir al registro de cliente
            return redirect(url_for('registro.registro_cliente', user_id=nuevo_usuario.id))

    return render_template('registro.html')

@registro_bp.route('/registro/proveedor/<int:user_id>', methods=['GET', 'POST'])
def registro_proveedor(user_id):
    if request.method == 'POST':
        # Procesar los detalles del proveedor y guardarlos en la base de datos
        proveedor = Proveedor(user_id=user_id, nombre_empresa=request.form.get('nombre_empresa'), direccion=request.form.get('direccion'))
        db.session.add(proveedor)
        db.session.commit()
        return 'Registro de proveedor exitoso.'

    return render_template('registro_proveedor.html')

@registro_bp.route('/registro/cliente/<int:user_id>', methods=['GET', 'POST'])
def registro_cliente(user_id):
    if request.method == 'POST':
        # Procesar los detalles del cliente y guardarlos en la base de datos
        cliente = Cliente(user_id=user_id, nombre_completo=request.form.get('nombre_completo'), direccion=request.form.get('direccion'))
        db.session.add(cliente)
        db.session.commit()
        return 'Registro de cliente exitoso.'

    return render_template('registro_cliente.html')
