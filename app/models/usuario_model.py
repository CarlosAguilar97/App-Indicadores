from db import obtener_conexion

def obtener_lista_usuarios():
    conexion = obtener_conexion()
    usuarios = []  # Cambiado para evitar la sombra de la variable
    try:
        with conexion.cursor() as cursor:
            # Llamada al procedimiento almacenado
            cursor.execute(
                """SELECT id, username, email, cell_phone, pwd, status, type 
                   FROM users""")
            usuarios = cursor.fetchall()
          
    finally:
        conexion.close()

    return usuarios

# registrar usuario
def insertar_usuario_db(usuario, email, cell_phone, password, estado, tipo):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            # Llamada al procedimiento almacenado
            cursor.execute(
                """INSERT INTO users (username, email, cell_phone, pwd, status, type) 
                   VALUES (%s, %s, %s, %s, %s, %s)""",
                (usuario, email, cell_phone, password, estado, tipo))
            conexion.commit()
    finally:
        conexion.close()
        
# Actualizar usuario
def actualizar_usuario_db(id, usuario, email, cell_phone, password, estado, tipo):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            # Llamada al procedimiento almacenado
            cursor.execute(
                """UPDATE users 
                   SET username = %s, email = %s, cell_phone = %s, pwd = %s, status = %s, type = %s 
                   WHERE id = %s""",
                (usuario, email, cell_phone, password, estado, tipo, id))
            conexion.commit()
    finally:
        conexion.close()