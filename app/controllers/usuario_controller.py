from werkzeug.security import check_password_hash, generate_password_hash
from flask import redirect, url_for, flash, session
import app.models.usuario_model as usuario_model
import re

def obtener_usuarios():
    usuarios = usuario_model.obtener_lista_usuarios()

    usuarios_obtenidos = []
    for usuario in usuarios:
        usuario_lista = list(usuario)

        # Actualizar el estado (posición 5)
        if usuario_lista[5] == 1:
            usuario_lista[5] = 'Activo'
        else:
            usuario_lista[5] = 'Inactivo'

        # Actualizar el tipo de usuario (posición 6)
        if usuario_lista[6] == 1:
            usuario_lista[6] = 'Administrador'
        elif usuario_lista[6] == 2:
            usuario_lista[6] = 'Usuario'
        else:
            usuario_lista[6] = 'Desconocido'

        usuarios_obtenidos.append(tuple(usuario_lista))

    return usuarios_obtenidos

def insertar_usuario(request):
    #verificarel POST
    if request.method == 'POST':
        #obtener los datos del formulario
        usuario = request.form['usuario']
        email = request.form['email']
        cell_phone = request.form['celular']
        password = generate_password_hash(request.form['contraseña'])
        tipo = request.form['tipo']
        estado = request.form['estado']
        # Insertar retroalimentación en la base de datos
        usuario_model.insertar_usuario_db(usuario, email, cell_phone, password, estado, tipo)
        flash('Usuario agregado correctamente', 'success')
    else:
        flash('No se pudo agregar el usuario', 'error') 
    return redirect(url_for('usuarios'))

# Actualizar usuario
def actualizar_usuario(request):
    #verificarel POST
    if request.method == 'POST':
        #obtener los datos del formulario
        id = request.form['id']
        usuario = request.form['usuario']
        email = request.form['email']
        cell_phone = request.form['celular']
        contrasena = request.form['contraseña']
        tipo = request.form['tipo']
        estado = request.form['estado']
        if re.match(r'^pbkdf2:sha256:\d+\$', contrasena):
            # La contraseña ya está cifrada, la utilizamos directamente
            password = contrasena
        else:
            # La contraseña no está cifrada, así que la ciframos
            password = generate_password_hash(contrasena)
        # Insertar retroalimentación en la base de datos
        usuario_model.actualizar_usuario_db(id, usuario, email, cell_phone, password, estado, tipo)
        flash('Usuario actualizado correctamente', 'success')
    else:
        flash('No se pudo actualizar el usuario', 'error') 
    return redirect(url_for('usuarios'))