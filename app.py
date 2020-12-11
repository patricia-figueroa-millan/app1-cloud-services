from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
Bootstrap(app)

#Configuracón para conexión con postgress
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:12345@localhost:5432/escolares'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://biviwnyxsklbky:6c9a71b37656deebb1d8503ed64c25e334ac4b9f027084da20591b8996a72927@ec2-18-233-32-61.compute-1.amazonaws.com:5432/d1imngndkjkpog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class Alumnos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30))
    apellido = db.Column(db.String(100))


lista = ["Nostros", "Contacto", "Preguntas Frecuentes" ]

@app.route('/', methods=['GET', 'POST'])
def index():
    print("index")
    if request.method == "POST":
        print("request")
        campo_nombre = request.form['nombre']
        campo_apellido= request.form['apellido']
        alumno = Alumnos(nombre=campo_nombre,apellido=campo_apellido)
        db.session.add(alumno)
        db.session.commit()
        mensaje = "Alumno registrado"
        return render_template("index.html",mensaje = mensaje)
    return render_template("index.html", variable = lista)
    #return redirect(url_for('acerca'))

@app.route('/acerca')
def acerca():
    consulta = Alumnos.query.all()
    print(consulta)
    return render_template("acerca.html", variable = consulta)


if __name__ == "__main__":
    app.run()
