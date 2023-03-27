from flask import Flask,current_app,g
from flask_sqlalchemy import *
import os
app=Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(basedir, 'menus.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
class Platos(db.Model):
    id_plato = db.Column(db.Integer,primary_key=True)
    nombre_plato=db.Column(db.String (100), nullable=False)
    desc_plato=db.Column(db.String(100),nullable=False)
    precio_plato=db.Column(db.String(6),nullable=False)
if os.path.isfile('C:\PYTHON\Trabajo_curso\.venv\menus.db')==False:
    print('El archivo no existe.');
    with app.app_context():
        db.create_all()
@app.route("/")
def index():
    resp=input("Teclea los datos del nuevo plato(s/n): ")
    while resp != "n":
        tipoPlato1=Platos()
        plat=input("Teclea el plato: ")
        tipoPlato1.nombre_plato=plat
        descr=input("Descripcion: ")
        tipoPlato1.desc_plato=descr
        pvp=input("Precio: ")
        tipoPlato1.precio_plato=pvp
        db.session.add(tipoPlato1)
        resp=input("¿Teclear otro tipo de plato(s/n?: ")

    db.session.commit()
    return "Datos en la base de datos"


if __name__=="__main__":
    app.run(debug=False)
