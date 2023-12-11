from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash, session
import app.controllers.usuario_controller as usuario_controller
import app.controllers.asignacion_controller as asignacion_controller

def lista_asignaciones():
    usuarios_obtenidos = usuario_controller.obtener_usuarios()
    asignaciones_obtenidas = asignacion_controller.obtener_asignaciones()
    return render_template('asignaciones.html', usuarios_obtenidos=usuarios_obtenidos, asignaciones_obtenidas=asignaciones_obtenidas)

def insert_asignacion(request):
    asignacion_controller.insertar_asignacion(request)
    
def update_asignacion(request):
    asignacion_controller.actualizar_asignacion(request)