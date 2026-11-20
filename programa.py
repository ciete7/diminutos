import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from consulta_salas import *
from conexion import Conexion

VENTANA_DIMENSIONES = '640x480'
usuario_tipo_actual = None
usuario_actual = None

def mostrar_ventana(tipo: str = 'info', mensaje: str = None, padre: tk.Tk = None):
    if mensaje is None:
        mensaje = 'Mensaje predeterminado'
    match tipo:
        case 'info':
            messagebox.showinfo('Información', mensaje, parent=padre)
        case 'error':
            messagebox.showerror('Error', mensaje, parent=padre)
        case 'advertencia':
            messagebox.showwarning('Advertencia', mensaje, parent=padre)

def ventana_login():
    login = tk.Tk()
    login.title("Inicio de Sesión")
    login.geometry("350x200")

    tk.Label(login, text="Usuario").pack(pady=5)
    username_entry = tk.Entry(login)
    username_entry.pack()

    tk.Label(login, text="Contraseña").pack(pady=5)
    password_entry = tk.Entry(login, show="*")
    password_entry.pack()

    def iniciar_sesion():
        global usuario_actual, usuario_tipo_actual
        username = username_entry.get().strip()
        password = password_entry.get()

        if not username or not password:
            mostrar_ventana("error", "Debe ingresar usuario y contraseña.", login)
            return

        try:
            usuario = Usuario.iniciar_sesion(username, password)
            if usuario is None:
                mostrar_ventana("error", "Usuario o contraseña incorrectos.", login)
                return

            usuario_actual = usuario
            if isinstance(usuario, Administrador):
                usuario_tipo_actual = "administrador"
            else:
                usuario_tipo_actual = "empleado"

            login.destroy()
            main()  # Asegúrate de tener definida esta función
        except Exception as e:
            mostrar_ventana("error", f"Error al iniciar sesión:\n{e}", login)

    tk.Button(login, text="Iniciar Sesión", command=iniciar_sesion).pack(pady=15)
    login.mainloop()

if __name__ == '__main__':
    ventana_login()
