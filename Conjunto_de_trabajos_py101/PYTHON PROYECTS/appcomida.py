from flask import Flask, request, render_template, redirect, url_for

from flask_sqlalchemy import *
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'menu.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Comidas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    descripcion = db.Column(db.String(200))
    tipo = db.Column(db.String(100)) # ENTRANTE, POSTRE, ...
    precio = db.Column(db.Float)
    activo = db.Column(db.Boolean, default=True)

    def __init__(self, nombre, descripcion, tipo, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.tipo = tipo
        self.precio = precio
        self.activo = True


#with app.app_context():
#    db.create_all()

@app.route("/")
def index():

    return "Hola"





@app.route("/admin_RellenarBD")
def admin_RellenarBD():
    plato1 = Comidas("Carne","Solomillo a la ...", "ENTRANTE", 45.98)
    plato2 = Comidas("Pescado", "Rape en salsa ...", "POSTRE", 12.32)
    db.session.add(plato1)
    db.session.commit()
    return "OK"


@app.route("/comidas")
def comidas():

    lista_comidas = Comidas.query.all()
    return render_template("comidas.html", comidas = lista_comidas)


if __name__=="__main__":
    app.run(debug=False)