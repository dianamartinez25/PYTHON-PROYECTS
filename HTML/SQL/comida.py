from flask import Flask, render_template
from  flask_sqlalchemy import *
import os
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "menu.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Comidas(db.Model):
    ID_comida = db.Column(db.Integer,primary_key=True)
    Nombre = db.Column(db.String (100))
    Descripcion = db.Column(db.String(100))
    Tipo =  db.Column(db.String(100))
    Precio = db.Column(db.String(6))
    def __init__ (self, Nombre, Descripcion , Tipo, Precio):
         self.Nombre = Nombre
         self.Descripcion = Descripcion
         self.Tipo = Tipo
         self.Precio = Precio
with app.app_context():
     db.create_all()



with app.app_context():
    db.create_all()


@app.route("/menu")
def index():
        plato0 = Comidas(" Ensaladilla ", " Rusa", " Entrante ", "6€")
        plato1 = Comidas(" Pulpo ", " a la Gallega ", " Segundo ", "18€")
        plato2 = Comidas(" Entrecot ", " con salsa de queso azul ", " Segundo ", "12€")
        plato3 = Comidas(" Patatas ", " a la Riojana ", " Entrante ", "8€")
        plato4 = Comidas(" Mousse ", " de Chocolate ", " Postre ", "5.50€")

        db.session.add_all([plato0, plato1, plato2, plato3, plato4])
        db.session.commit()
       
        return "Bienvenid@s"
     
if __name__=="__main__":
    app.run(debug=False)

#@app.route("/comidas")
# lista_comidas = Comidas.query.all()
#return render_template("menu.html", comidas = lista_comidas)