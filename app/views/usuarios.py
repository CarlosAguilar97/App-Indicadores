from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash, session
import app.controllers.usuario_controller as usuario_controller

def lista_usuarios():
    usuarios_obtenidos = usuario_controller.obtener_usuarios()
    return render_template('usuarios.html', usuarios_obtenidos=usuarios_obtenidos)

def insert_usuario(request):
    usuario_controller.insertar_usuario(request)
    
def update_usuario(request):
    usuario_controller.actualizar_usuario(request)
    
    