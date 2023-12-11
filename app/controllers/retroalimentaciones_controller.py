from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash, session,Flask
import app.models.retroalimentaciones_model as retroalimentacion_model
from datetime import datetime
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)  

#obtener retroalimentaciones
def obtener_retroalimentaciones(user_id):
    retroalimentaciones = retroalimentacion_model.obtener_retroalimentaciones_db(user_id)
    return retroalimentaciones

def insertar_retroalimentacion(request):
    now = datetime.now()
    fecha = now.strftime("%Y-%m-%d")
    if request.method == 'POST':
        #obtener los datos del formulario
        user_id = session['id']
        contenido = request.form['contenido']
        file = request.files['fileInput']
        fecha_in = fecha
        if file.filename != '':

            nombre_archivo = secure_filename(file.filename)

            upload_folder = os.path.join(app.root_path,'..','static','carga',contenido)
            os.makedirs(upload_folder, exist_ok=True) 
            
            ruta_archivo = os.path.join(upload_folder, nombre_archivo)
            file.save(ruta_archivo)
            # Insertar retroalimentación en la base de datos
            retroalimentacion_model.insertar_retroalimentacion_db(user_id, contenido, ruta_archivo, fecha_in)
            flash('Retroalimentacion agregada correctamente', 'success')
        
    else:
        flash('No se pudo agregar la retroalimentacion', 'error')
    return redirect(url_for('retroalimentaciones'))

