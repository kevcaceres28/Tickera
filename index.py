from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)


DATABASE = 'postgresql://usuario:contraseña@localhost:5432/nombre_de_la_base_de_datos'

def get_db():
    db = psycopg2.connect(DATABASE)
    return db

@app.route('/')
def index():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM eventos')
    eventos = cursor.fetchall()
    db.close()
    return render_template('index.html', eventos=eventos)

@app.route('/agregar_evento', methods=['GET', 'POST'])
def agregar_evento():
    if request.method == 'POST':
        titulo = request.form['titulo']
        fecha = request.form['fecha']

        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO eventos (titulo, fecha) VALUES (%s, %s)', (titulo, fecha))
        db.commit()
        db.close()

        return redirect(url_for('index'))

    return render_template('agregar_evento.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
