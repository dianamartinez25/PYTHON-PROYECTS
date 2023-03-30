from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import *
import os
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Comidas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    descripcion = db.Column(db.String(200))
    tipo = db.Column(db.String(100)) # ENTRANTE, POSTRE, ...
    precio = db.Column(db.Float)


    def __init__(self, nombre, descripcion, tipo, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.tipo = tipo
        self.precio = precio
 


@app.route("/")
def index():
    return ("Hola")
       
     
@app.route("/comidas")
def comidas():
    plato0 = Comidas(" Ensaladilla ", " Rusa", " Entrante ", 6)
    plato1 = Comidas(" Pulpo ", " a la Gallega ", " Segundo ", 18)
    plato2 = Comidas(" Entrecot ", " con salsa de queso azul ", " Segundo ", 12)
    plato3 = Comidas(" Patatas ", " a la Riojana ", " Entrante ", 8)
    plato4 = Comidas(" Mousse ", " de Chocolate ", " Postre ", 5.50)

    db.session.add_all([plato0, plato1, plato2, plato3, plato4])
    db.session.commit()
       
    return "Bienvenid@s"
# lista_comidas = Comidas.query.all()
#return render_template("menu.html", comidas = lista_comidas)

if __name__=="__main__":
    app.run(debug=False)