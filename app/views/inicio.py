# Compare this snippet from app/views/inicio.py:
from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash, session
import app.controllers.inicio_controller as inicio_controller

