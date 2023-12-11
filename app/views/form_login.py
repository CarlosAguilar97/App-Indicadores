
# app/views/form_login.py

from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash, session
import app.controllers.login_controller as login_controller

submit_login_route = Blueprint('submit_login_route', __name__)

@submit_login_route.route('/login', methods=['GET', 'POST'])
def submit_login(request):
    return login_controller.submit_login(request)

def cerrar_session():
    return login_controller.logout()