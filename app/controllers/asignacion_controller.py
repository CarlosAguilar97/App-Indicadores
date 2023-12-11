from werkzeug.security import check_password_hash, generate_password_hash
from flask import redirect, url_for, flash, session
import app.models.asignacion_model as asignacion_model
import app.models.notificaciones_model as notificaciones_model
from datetime import datetime

#funcion de obtener asignaciones
def obtener_asignaciones():
    asignaciones = asignacion_model.obtener_lista_asignaciones()

    asignaciones_obtenidas = []
    for asignacion in asignaciones:
        asignacion_lista = list(asignacion)

        # Actualizar el estado (posición 6) hay nuevos estados Pendiente, completado, Observado, Cancelado

        if asignacion_lista[6] == 1:
            asignacion_lista[6] = 'Pendiente'
        elif asignacion_lista[6] == 0:
            asignacion_lista[6] = 'Completado'
        elif asignacion_lista[6] == 2:
            asignacion_lista[6] = 'Observado'
        elif asignacion_lista[6] == 3:
            asignacion_lista[6] = 'Cancelado'
        else:
            asignacion_lista[6] = 'Desconocido'

        asignaciones_obtenidas.append(tuple(asignacion_lista))

    return asignaciones_obtenidas

#funcion de insertar asignacion
def insertar_asignacion(request):
    #verificarel POST
    now = datetime.now()
    fecha = now.strftime("%Y-%m-%d")
    if request.method == 'POST':
        #obtener los datos del formulario
        usuario = request.form['usuario']
        tarea = request.form['tarea']
        descripcion = request.form['descripcion']
        fecha_in = fecha
        estado = 1
        # Insertar retroalimentación en la base de datos
        id_noti = asignacion_model.insertar_asignacion_db(usuario, tarea, descripcion, fecha_in, estado)
        notificaciones_model.insertar_notificacion_db(usuario, id_noti, estado, fecha_in)
        
        flash('Asignacion agregada correctamente', 'success')
    else:
        flash('No se pudo agregar la asignacion', 'error') 
    return redirect(url_for('asignaciones'))

# actualizar asignacion
def actualizar_asignacion(request):
    now = datetime.now()
    fecha = now.strftime("%Y-%m-%d")
    #verificarel POST
    if request.method == 'POST':
        #obtener los datos del formulario
        id = request.form['id']
        usuario = request.form['usuario']
        tarea = request.form['tarea']
        descripcion = request.form['descripcion']
        fecha_in = fecha
        estado = request.form['estado']
        asignacion_model.actualizar_asignacion_db(id, usuario, tarea, descripcion, fecha_in, estado)
        flash('Asignacion actualizada correctamente', 'success')
    else:
        flash('No se pudo actualizar la asignacion', 'error') 
    return redirect(url_for('asignaciones'))



