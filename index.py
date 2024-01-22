from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


DATABASE = 'eventos.db'
def get_db():
  db = sqlite3.connect(DATABASE)
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
        cursor.execute('INSERT INTO eventos (titulo, fecha) VALUES (?, ?)', (titulo, fecha))
        db.commit()
        db.close()

        return redirect(url_for('index'))

    return render_template('agregar_evento.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
