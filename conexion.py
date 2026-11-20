import MySQLdb
from MySQLdb import Connection
from abc import ABC, abstractmethod
import mysql.connector
from mysql.connector import Error

config_bd= {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '',
    'database': 'sistema_salas'
}

class Conexión(ABC):
    __instance = None
    __connection = None

    def __new__(cls):
        if cls.instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if self.__connection is None:
            self.__connection = MySQLdb.connect(
                host = DB_HOST,
                user = DB_USER,
                passwd = DB_PASS,
                database = DB_NAME
            )
    
    def obtener_conexion(self):
        return self.__conection

class ActiveRecord(ABC):
    @abstractmethod
    def guardar(self):
        pass

    @abstractmethod
    def actualizar(self) -> None:
        pass

    @abstractmethod
    def eliminar(self) -> None:
        pass

    @classmethod
    @abstractmethod
    def buscar_por_id(cls, id:int):
        pass

    @classmethod
    @abstractmethod
    def buscar_todos(cls):
        pass

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
