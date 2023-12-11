from werkzeug.security import check_password_hash, generate_password_hash
from db import obtener_conexion

def submit_login_to_db(username, password):
    conexion = obtener_conexion()
    usuario = []  # Cambiado para evitar la sombra de la variable
    try:
        with conexion.cursor() as cursor:
            # Llamada al procedimiento almacenado
            cursor.execute(
                """SELECT id, username, email, cell_phone, pwd, status, type 
                   FROM users 
                   WHERE username = %s AND status = 1""", (username,))
            fetched_user = cursor.fetchone()

            # Verificar la contraseña si se encuentra un usuario
            if fetched_user and check_password_hash(fetched_user[4], password):
                usuario = fetched_user
    finally:
        conexion.close()

    return usuario
