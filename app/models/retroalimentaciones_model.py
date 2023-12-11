from db import obtener_conexion

#oberner lista de retroalimentaciones
def obtener_retroalimentaciones_db(user_id):
    conexion = obtener_conexion()
    retroalimentaciones = []  # Cambiado para evitar la sombra de la variable
    try:
        with conexion.cursor() as cursor:
            # Llamada al procedimiento almacenado
            cursor.execute(
                """SELECT r.id, r.user_id, r.content, r.file, r.fecha_in
                    FROM feedback r
                    WHERE r.user_id = %s
                    ORDER BY r.id DESC""",(user_id))
            retroalimentaciones = cursor.fetchall()
          
    finally:
        conexion.close()

    return retroalimentaciones

# registrar retroalimentacion
def insertar_retroalimentacion_db(user_id, contenido, ruta_archivo, fecha_in):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            # Llamada al procedimiento almacenado
            cursor.execute(
                """INSERT INTO feedback (user_id, content, file, fecha_in) 
                   VALUES (%s, %s, %s, %s)""",
                (user_id, contenido, ruta_archivo, fecha_in))
            conexion.commit()
    finally:
        conexion.close()