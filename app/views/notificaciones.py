from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash, session
import app.controllers.notificaciones_controller as notificaciones_controller

#lista de notificaciones
def lista_notificaciones(user_id):
    notificaciones = notificaciones_controller.obtener_notificaciones(user_id)
    return render_template('notificaciones.html', notificaciones=notificaciones)

#actualizar notificacion
def update_notificacion(request):
    notificaciones_controller.actualizar_notificacion(request)