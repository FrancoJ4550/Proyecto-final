from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Crear la tabla de comentarios si no existe
def create_table():
    conn = sqlite3.connect('comentarios.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comentarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            fecha TEXT NOT NULL,
            comentario TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

create_table()

# Ruta principal para mostrar y agregar comentarios
@app.route('/')
def index():
    conn = sqlite3.connect('comentarios.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM comentarios')
    comentarios = cursor.fetchall()
    conn.close()
    return render_template('index.html', comentarios=comentarios)

# Ruta para agregar comentarios
@app.route('/agregar_comentario', methods=['POST'])
def agregar_comentario():
    usuario = request.form['usuario']
    comentario = request.form['comentario']

    conn = sqlite3.connect('comentarios.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO comentarios (usuario, fecha, comentario) VALUES (?, datetime("now"), ?)', (usuario, comentario))
    conn.commit()
    conn.close()

    return redirect(url_for('paginaPabellon'))

# Ruta para eliminar comentarios
@app.route('/eliminar_comentario', methods=['POST'])
def eliminar_comentario():
    comentario_id = request.form['comentario_id']
    usuario = request.form['usuario']

    conn = sqlite3.connect('comentarios.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM comentarios WHERE id = ? AND usuario = ?', (comentario_id, usuario))
    conn.commit()
    conn.close()

    return redirect(url_for('paginaPabellon'))

# Ruta para editar comentarios
@app.route('/editar_comentario', methods=['POST'])
def editar_comentario():
    comentario_id = request.form['comentario_id']
    usuario = request.form['usuario']
    nuevo_comentario = request.form['nuevo_comentario']

    conn = sqlite3.connect('comentarios.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE comentarios SET comentario = ? WHERE id = ? AND usuario = ?', (nuevo_comentario, comentario_id, usuario))
    conn.commit()
    conn.close()

    return redirect(url_for('paginaPabellon'))

@app.route('/paginaMUAC')
def paginaMUAC():
    conn = sqlite3.connect('comentarios.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM comentarios')
    comentarios = cursor.fetchall()
    conn.close()
    return render_template('paginaMUAC.html', comentarios=comentarios)

@app.route('/paginaBN')
def paginaBN():
    conn = sqlite3.connect('comentarios.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM comentarios')
    comentarios = cursor.fetchall()
    conn.close()
    return render_template('paginaBN.html', comentarios=comentarios)

@app.route('/paginaJardinB')
def paginaJardinB():
    conn = sqlite3.connect('comentarios.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM comentarios')
    comentarios = cursor.fetchall()
    conn.close()
    return render_template('paginaJardinB.html', comentarios=comentarios)

@app.route('/paginaMUCA')
def paginaMUCA():
    conn = sqlite3.connect('comentarios.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM comentarios')
    comentarios = cursor.fetchall()
    conn.close()
    return render_template('paginaMUCA.html', comentarios=comentarios)

@app.route('/paginaPabellon')
def paginaPabellon():
    conn = sqlite3.connect('comentarios.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM comentarios')
    comentarios = cursor.fetchall()
    conn.close()
    return render_template('paginaPabellon.html', comentarios=comentarios)

@app.route('/paginaUNIVERSUM')
def paginaUNIVERSUM():
    conn = sqlite3.connect('comentarios.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM comentarios')
    comentarios = cursor.fetchall()
    conn.close()
    return render_template('paginaUNIVERSUM.html', comentarios=comentarios)

if __name__ == '__main__':
    app.run(debug=True)
