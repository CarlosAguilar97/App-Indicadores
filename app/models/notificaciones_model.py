from db import obtener_conexion

#oberner lista de notificaciones
def obtener_notificaciones_db(user_id):
    conexion = obtener_conexion()
    notificaciones = []  # Cambiado para evitar la sombra de la variable
    try:
        with conexion.cursor() as cursor:
            # Llamada al procedimiento almacenado
            cursor.execute(
                """SELECT n.id, n.user_id, u.username, n.assing_id, a.task, a.description, n.status, n.fecha
                    FROM notification n
                    INNER JOIN assignment a ON a.id = n.assing_id
                    INNER JOIN users u ON u.id = n.user_id
                    WHERE a.user_id = %s
                    ORDER BY n.id DESC""",(user_id))
            notificaciones = cursor.fetchall()
          
    finally:
        conexion.close()

    return notificaciones

# registrar notificacion
def insertar_notificacion_db(user_id, assing_id, estado, fecha):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            # Llamada al procedimiento almacenado
            cursor.execute(
                """INSERT INTO notification (user_id, assing_id, status, fecha) 
                   VALUES (%s, %s, %s, %s)""",
                (user_id, assing_id, estado, fecha))
            conexion.commit()
    finally:
        conexion.close()
        
# Actualizar notificacion y asignacion en una misma sentencia sql
def actualizar_notificacion_db(id, estado, fecha):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            # Llamada al procedimiento almacenado
            cursor.execute(
                """UPDATE notification n
                   INNER JOIN assignment a ON a.id = n.assing_id
                   SET n.status = %s, a.status = %s, n.fecha = %s
                   WHERE n.id = %s""",
                (estado, estado, fecha, id))
            conexion.commit()
    finally:
        conexion.close()
