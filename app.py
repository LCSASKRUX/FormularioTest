#FLASK FRAMEWORK PARA LA APLICACION WEB CREAR CONEXION CON LA BASE DE DATOS Y LA VISTA DE LA APLICACION
from flask import Flask, jsonify, redirect, render_template, request;
#IMPORTANDO LA CONFIGURACION 
from config import config;
#LIBRERIA PARA CONECTAR BASE DE DATOS A FLASK TAMBIEN PUEDE SER SQLALCHEMY,MYSQL ENTRE OTROS
import psycopg2

#CREA LA CONEXION
app = Flask(__name__)
conn = psycopg2.connect(
    host=config['development'].DB_HOST,
    database=config['development'].DB_NAME,
    user=config['development'].DB_USER,
    password=config['development'].DB_PASSWORD
)

#RUTA PARA LA VISTA DE LA APLICACION
@app.route('/',methods=['GET','POST'])
def index():
    try:
        if request.method == 'POST':
            nombre = request.form['nombre']
            apellido = request.form['apellido']
            
            cur = conn.cursor()
            cur.execute("INSERT INTO users (nombre, apellido) VALUES (%s, %s)", (nombre, apellido))
            conn.commit()
            cur.close()
            cur = conn.cursor()
            cur.execute("SELECT * FROM users")
            users = cur.fetchall()
            return render_template('index.html', users=users)
        else:
            cur = conn.cursor()
            cur.execute("SELECT * FROM users")
            users = cur.fetchall()
            cur.close()
            return render_template('index.html', users=users)
    except Exception as e:
        return(str(e))
        

#INICIALIZACION DE VARIABLES DE LA APLICACION
if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.run(debug=True)