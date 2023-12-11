from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash, session
import app.controllers.retroalimentaciones_controller as retroalimentaciones_controller

def lista_retroalimentaciones(user_id):
    retroalimentaciones = retroalimentaciones_controller.obtener_retroalimentaciones(user_id)
    return render_template('retroalimentacion.html', retroalimentaciones=retroalimentaciones)

def insert_retroalimentacion(request):
    retroalimentaciones_controller.insertar_retroalimentacion(request)
