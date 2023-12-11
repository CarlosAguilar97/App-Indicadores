from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash, session
import app.models.notificaciones_model as notificaciones_model
from datetime import datetime

def obtener_notificaciones(user_id):
    obtener_notificaciones2 = notificaciones_model.obtener_notificaciones_db(user_id)
    obtener_notificaciones = []

    for notificaciones in obtener_notificaciones2:
        notificacion_lista = list(notificaciones)

        # Actualizar el estado (posición 6) hay nuevos estados Pendiente, completado, Observado, Cancelado
        if notificacion_lista[6] == 1:
            notificacion_lista[6] = 'Pendiente'
        elif notificacion_lista[6] == 0:
            notificacion_lista[6] = 'Completado'
        elif notificacion_lista[6] == 2:
            notificacion_lista[6] = 'Observado'
        elif notificacion_lista[6] == 3:
            notificacion_lista[6] = 'Cancelado'
        else:
            notificacion_lista[6] = 'Desconocido'

        # Convertir la lista actualizada de nuevo a una tupla
        notificacion_tupla = tuple(notificacion_lista)
        obtener_notificaciones.append(notificacion_tupla)

    return obtener_notificaciones

#actualizar notificacion
def actualizar_notificacion(request):
    if request.method == 'POST':
        estado = request.form['estado']
        id_notificacion = request.form['id_notificacion']
        fecha = datetime.now()
        id_asignacion = request.form['id_asignacion']
        notificaciones_model.actualizar_notificacion_db(request)

