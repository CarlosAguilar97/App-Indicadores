#Librerias para implementar el Servidor y Base de Datos
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash, session
from datetime import datetime
from flask_mysqldb import MySQL
from config import config
import app.views.form_login as views_login
import app.views.inicio as views_inicio
import app.views.usuarios as views_usuarios
import app.views.asignacion as views_asignacion
import app.views.retroalimentaciones as views_retroalimentaciones
import app.views.notificaciones as views_notificaciones

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
db=MySQL(app)

@app.route('/')
def Index():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        views_login.submit_login(request)
    else:
        return 'No hay datos'
    return redirect(url_for('inicio'))

@app.route('/inicio')
def inicio():
    if 'username' in session:
        return render_template('inicio.html')
    else:
        return redirect(url_for('Index'))
    
@app.route('/usuarios')
def usuarios():
    if 'username' in session:
        return views_usuarios.lista_usuarios()
    else:
        return redirect(url_for('Index'))

@app.route('/agregar_usuario', methods=['GET', 'POST'])
def agregar_usuario():
    if 'username' in session:
        if request.method == 'POST':
            views_usuarios.insert_usuario(request)
            return redirect('/usuarios')
        else:
            return 'No hay datos'
    else:
        return redirect('/usuarios')
    
@app.route('/actualizar_usuario', methods=['GET', 'POST'])
def actualizar_usuario():
    if 'username' in session:
        if request.method == 'POST':
            views_usuarios.update_usuario(request)
            return redirect('/usuarios')
        else:
            return 'No hay datos'
    else:
        return redirect('/usuarios')
    
# cerrar session
@app.route('/logout')
def logout():
    views_login.cerrar_session()
    return redirect(url_for('Index'))

#ruta asignacion
@app.route('/asignaciones')
def asignaciones():
    if 'username' in session:
        return views_asignacion.lista_asignaciones()
    else:
        return redirect(url_for('Index'))
    
@app.route('/agregar_asignacion', methods=['GET', 'POST'])
def agregar_asignacion():
    if 'username' in session:
        if request.method == 'POST':
            views_asignacion.insert_asignacion(request)
            return redirect('/asignaciones')
        else:
            return 'No hay datos'
    else:
        return redirect('/asignaciones')
    
# modificar asignacion
@app.route('/actualizar_asignacion', methods=['GET', 'POST'])
def actualizar_asignacion():
    if 'username' in session:
        if request.method == 'POST':
            views_asignacion.update_asignacion(request)
            return redirect('/asignaciones')
        else:
            return 'No hay datos'
    else:
        return redirect('/asignaciones')
    
#ruta asignacion
@app.route('/retroalimentaciones')
def retroalimentaciones():
    if 'username' in session:
        return views_retroalimentaciones.lista_retroalimentaciones(session['id'])
    else:
        return redirect(url_for('Index'))

@app.route('/agregar_alimentacion', methods=['GET', 'POST'])
def agregar_alimentacion():
    if 'username' in session:
        if request.method == 'POST':
            views_retroalimentaciones.insert_retroalimentacion(request)
            return redirect('/retroalimentaciones')
        else:
            return 'No hay datos'
    else:
        return redirect('/retroalimentaciones')

# ruta de notificaciones
@app.route('/notificaciones')
def notificaciones():
    if 'username' in session:
        return views_notificaciones.lista_notificaciones(session['id'])
    else:
        return redirect(url_for('Index'))
    

#ruta para inicializar el servidor
if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()
    