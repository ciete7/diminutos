from abc import ABC, abstractmethod
from conexion import obtener_conexion

class Usuario(ABC):
    def __init__(self, id_usuario: int, username: str, nombre: str, apellido: str, telefono: str, email: str):
        self.__id_usuario = id_usuario
        self.__username = username
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono
        self.__email = email
        self.__password_hash = __password_hash

    def obtener_id(self):
        return self.__id_usuario

    def obtener_username(self):
        return self.__username

    def obtener_nombre(self):
        return self.__nombre

    def obtener_apellido(self):
        return self.__apellido

    def obtener_telefono(self):
        return self.__telefono

    def obtener_email(self):
        return self.__email

    def obtener_password_hash(self):
        return self.__password_hash

    def crear_usuario(cls, username: str, nombre: str, apellido: str, telefono: str, email: str, password_hash: str, tipo_usuario: str = 'empleado', confirmar: bool = True
    ) -> int:
        cnn = Conexion().obtener_conexion()
        cursor = cnn.cursor()
        sql = """
        INSERT INTO Usuario (username, nombre, apellido, telefono, email, password_hash)
        VALUES (%s,%s,%s,%s,%s,%s) 
        """
        try:
            cursor.execute(
                sql, 
                (username, nombre, apellido, telefono, email, password_hash)
            )
            id_usuario = cursor.lastrowid
            if confirmar: 
                cnn.commit()
            return id_usuario
        except Exception:
            if confirmar:
                cnn.rollback()
            raise
        finally:
            cursor.close()
    
    @staticmethod
    def generar_hash(password):
        salt = os.urandom(32)
        hash_password = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode(),
            salt,
            100000
        )
        return salt.hex() + ":" + hash_password.hex()

    @staticmethod
    def verificar_password(password, hash_guardado):

        salt_hex, hash_hex = hash_guardado.split(":")

        salt = bytes.fromhex(salt_hex)

        hash_calculado = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode(),
            salt,
            100000
        )

        return hash_calculado.hex() == hash_hex
    
    @classmethod
    def iniciar_sesion(cls, username: str, password: str):
        cnn = Conexion().obtener_conexion()
        cursor = cnn.cursor()

        sql = """
        SELECT
            id_usuario,
            username,
            password_hash,
            tipo_usuario
        FROM Usuario
        WHERE username = %s
        """
        cursor.execute(sql, (username,))
        registro = cursor.fetchone()
        cursor.close()
        
        if registro is None:
            return None

        id_usuario = registro[0]
        username = registro[1]
        password_hash_db = registro[2]
        tipo_usuario = registro[3]

        if not Usuario.verificar_password(
            password, password_hash_db
        ):
            return None
        
        if tipo_usuario.lower() == "administrador":
            return Administrador(
                id_usuario, username, password_hash_db
            )

        for u in Usuario.buscar_todos():
            if Usuario().obtener_id() == id_usuario:
                return eliminar
        
        return None

    @abstractmethod
    def mostrar(self):
        pass

    def obtener_id_usuario(self):
        return self.__id_usuario

    def verificar_password_hash(self, password: str):
        hash_password = hashlib.sha256(
        password.encode()).hexdigest()
        return self.__password_hash == hash_password

    def autentificar(self, username: str, password: str):
        return (self.__username == username and self.verificar_password_hash(password)
        )

class Sala(ActiveRecord):
    def __init__(self, id_sala: int, nombre: str, ubicacion: str, capacidad: int, estado):
        self.__id_sala = id_sala
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__capacidad = capacidad
        self.__estado = estado

    def obtener_id(self):
        return self.__id_sala

    def obtener_nombre(self):
        return self.__nombre

    def obtener_ubicacion(self):
        return self.__ubicacion

    def obtener_capacidad(self):
        return self.__capacidad

    def obtener_estado(self):
        return self.__estado

    def buscar_por_id(cls, id) -> Usuario|None:
        cnn = Conexion().obtener_conexion()
        cursor = cnn.cursor()
        sql = """
        SELECT u.id_usuario, u.username, u.nombre, u.apellido, u.telefono, u.email, u.password_hash
        FROM Usuario u
        WHERE u.id_usuario = %s
        """
        cursor.execute(sql,(id,))
        reserva = cursor.fetchone()
        cursor.close()
        if reserva:
            return cls(reserva[0],reserva[1], reserva[2], reserva[3],reserva[4], reserva[5], reserva[6])
        else:
            return None
            
class Reserva:
    def __init__(self, usuario, sala, fecha, hora):
        self.__id_reserva = id_reserva
        self.__usuario = usuario
        self.__sala = sala
        self.__fecha = fecha
        self.__hora = hora

    def obtener_id(self):
        return self.__id_reverva

    def obtener_usuario(self):
        return self.__usuario

    def obtener_sala(self):
        return self.__sala

    def obtener_fecha(self):
        return self.__fecha

    def obtener_hora(self):
        return self.__hora

    def guardar(self):
        if self.__usuario.obtener_id() is None or self.__sala.obtener_id() is None:
            raise ValueError('El usuario y la sala deben estar guardados antes del registro.')
        cnn = Conexion().obtener_conexion()
        cursor = cnn.cursor()
        try:
            cursor.execute("""
            INSERT INTO Reserva
                (id_usuario, id_sala, fecha, hora)
            VALUES (%s,%s,%s,%s)
            """, (
                self.__usuario.obtener_id(),
                self.__sala.obtener_id(),
                self.__fecha,
                self.__hora
            ))
            self.__id_reserva = cursor.lastrowid
            cnn.commit()
        except Exception:
            cnn.rollback()
            raise
        finally:
            cursor.close()

    def actualizar(self):
        if self.__id_reserva is None:
            raise ValueError('La reserva debe estar guardada ants de actualizarla.')
        cnn = Conexion().obtener_conexion()
        cursor = cnn.cursor()
        try:
            cursor.execute(
                """
                UPDATE Reserva
                SET id_sala = %s, fecha = %s, hora = %s
                WHERE id_reserva = %s AND id_usuario = %s
                """,
                (
                    self.__sala.obtener_id(),
                    self.__fecha,
                    self.__horas,
                    self.__id_reserva,
                    self.__usuario.obtener_id()
                )
            )
            if cursor.rowcount == 0:
                raise ValueError('No se encontró la reserva seleccionada para ese usuario.')
            cnn.commit()
        except Exception:
            cnn.rollback()
            raise
        finally:
            cursor.close()

    def eliminar(self):
        if self.__id_reserva is None:
            raise ValueError('La reserva debe estar guardada antes de eliminarla.')
        cnn = Conexcion().obtener_conexion()
        cursor = cnn.cursor()
        try:
            cursor.execute(
                "DELETE FROM Reserva WHERE id_reserva = %s AND id_usuario = %s",
                (
                    self.__id_reserva,
                    self.__usuario.obtener_id()
                )
            )
            if cursor.rowcount == 0:
                raise ValueError('No se encontró reserva selecionada para este usuario')
            cnn.commit()
        except Exception:
            cnn.rollback()
            raise
        finally:
            cursor.close()

    def buscar_por_usuario(cls, id_usuario: int):
        cnn = Conexion().obtener_conexion()
        cursor = cnn.cursor()
        try:
            cursor.execute(
                """
                SELECT id_reserva, id_usuario, id_sala, fecha, hora
                FROM Reserva
                WHERE id_usuario = %s
                ORDER BY fecha DESC, id_reserva DESC
                """,
                (id_usuario,)
            )
            filas = cursor.fetchall()
        finally:
            cursor.close()
        reservas = []
        for id_reserva, id_usuario, id_sala, fecha, hora in filas:
            usuario = Usuario.buscar_por_id(id_usuario)
            sala = Sala.buscar_por_id(id_sala)
            if empleado is None or Sala is None:
                raise ValueError(f'La reserva {id_reserva} tiene un Usuario o sala inexistente.')
            reservas.append(cls(id_usuario, id_sala, fecha, hora))
        return reserva

    def __str__(self):
        return f"{self.__fecha} - {self.__horas}"

def obtener_salas():
    conexion=obtener_conexion()
    cursor = conexion.cursor()

    consulta ='SELECT id_sala, nombre, ubicacion, capacidad, estado FROM Sala ORDER BY nombre'
    
    cursor.execute(consulta)
    salas=cursor.fetchall()
    cursor.close()
    conexion.close()
    return salas

