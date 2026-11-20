import MySQLdb
from MySQLdb import Connection
from abc import ABC, abstractmethod

config_bd = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '',
    'database': 'sistema_salas'
}

class Conexion:
    __instance = None
    __connection = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if self.__connection is None:
            self.__connection = MySQLdb.connect(
                host=config_bd['host'],
                port=config_bd['port'],
                user=config_bd['user'],
                passwd=config_bd['password'],
                database=config_bd['database']
            )
    
    def obtener_conexion(self):
        return self.__connection

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
    def buscar_por_id(cls, id: int):
        pass

    @classmethod
    @abstractmethod
    def buscar_todos(cls):
        pass
