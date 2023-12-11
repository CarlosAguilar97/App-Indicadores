from db import obtener_conexion
#oberner lista de asignaciones
def obtener_lista_asignaciones():
    conexion = obtener_conexion()
    asignaciones = []  # Cambiado para evitar la sombra de la variable
    try:
        with conexion.cursor() as cursor:
            # Llamada al procedimiento almacenado
            cursor.execute(
                """SELECT a.id, a.user_id, u.username, a.task, a.description, a.fecha_in, a.status 
                    FROM assignment a
                    INNER JOIN users u ON u.id = a.user_id 
                    ORDER BY a.id DESC""")
            asignaciones = cursor.fetchall()
          
    finally:
        conexion.close()

    return asignaciones

# registrar asignacion
def insertar_asignacion_db(usuario, tarea, descripcion, fecha, estado):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            # Llamada al procedimiento almacenado
            cursor.execute(
                """INSERT INTO assignment (user_id, task, description, fecha_in, status) 
                   VALUES (%s, %s, %s, %s, %s)""",
                (usuario, tarea, descripcion, fecha, estado))
            # Obtener el ID de la fila recién insertada
            id_insertada = cursor.lastrowid
            conexion.commit()
            # Retornar el ID de la fila recién insertada
            return id_insertada
    finally:
        conexion.close()

# Actualizar asignacion
def actualizar_asignacion_db(id, usuario, tarea, descripcion, fecha, estado):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            # Llamada al procedimiento almacenado
            cursor.execute(
                """UPDATE assignment 
                   SET user_id = %s, task = %s, description = %s, fecha_in = %s, status = %s 
                   WHERE id = %s""",
                (usuario, tarea, descripcion, fecha, estado, id))
            conexion.commit()
    finally:
        conexion.close()