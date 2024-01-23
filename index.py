from flask import Flask, render_template, request, redirect, url_for 
from app import app
import sqlite3
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG)

app = Flask(__name__)

from app import main

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
        if evento:
            return render_template('detalle_evento.html', evento=evento)
        else:
            return "Evento no encontrado", 404

if __name__ == '__main__':
    app.run(debug=True)