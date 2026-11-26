from flask import Flask, render_template, request, redirect, session
from consulta_salas import Usuario, Sala

app = Flask(__name__)
app.secret_key = "cambia-esto-por-una-clave-larga-y-unica"


@app.route('/')
def inicio():
    if 'usuario_id' not in session:
        return redirect('/login')
    return f"Sesión iniciada. ID de usuario: {session['usuario_id']}"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        usuario = Usuario.iniciar_sesion(username, password)

        if usuario is None:
            return render_template('login.html', error="Usuario o contraseña incorrectos")

        session['usuario_id'] = usuario.obtener_id()
        session['nombre'] = usuario.obtener_nombre()
        session['tipo'] = 'administrador' if usuario.mostrar().startswith('Admin') else 'empleado'
        return redirect('/')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


@app.route('/salas')
def listar_salas():
    if 'usuario_id' not in session:
        return redirect('/login')
    salas = Sala.buscar_todos()
    return render_template('salas.html', salas=salas)


if __name__ == '__main__':
    app.run(debug=True)