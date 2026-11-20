from conexion import obtener_conexion

def obtener_salas():
    conexion=obtener_conexion()
    cursor = conexion.cursor()

    consulta ='SELECT id_sala, nombre, ubicacion, capacidad, estado FROM Sala ORDER BY nombre'
    
    cursor.execute(consulta)
    salas=cursor.fetchall()
    cursor.close()
    conexion.close()
    return salas