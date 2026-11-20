from consulta_salas import obtener_salas

def mostrar_salas():
    salas=obtener_salas()

    print('===== Listado de salas =====')

    if len(salas) == 0:
        print('No hay salas registradas.')
        return
    
    for sala in salas:
        id_sala = sala[0]
        nombre = sala[1]
        ubicacion = sala[2]
        capacidad = sala[3]
        estado = sala[4]

        print(f'ID: {id_sala}')
        print(f'Nombre: {nombre}')
        print(f'Ubicación: {ubicacion}')
        print(f'Capacidad: {capacidad}')
        print(f'Estado: {estado}')
        print(f'-------------------------')
mostrar_salas()