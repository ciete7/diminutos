import mysql.connector
from mysql.connector import Error

config_bd= {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '',
    'database': 'sistema_salas'
}

def obtener_conexion():
    try:
        conexion=mysql.connector.connect(**config_bd)

        if conexion.is_connected():
            return conexion
        
        raise Error('No fue posible conectarse con MySQL.')

    except Error as error:
        raise ConnectionError(
            f'No fue posible conectarse a la base de datos: {error}'
        ) from error

if __name__=='__main__':
    conexion = obtener_conexion()
    print('Conexión exitosa.') 
    conexion.close()