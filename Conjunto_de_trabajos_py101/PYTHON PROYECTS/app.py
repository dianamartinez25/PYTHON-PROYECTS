from flask import Flask, render_template
from  flask_sqlalchemy import *
import os
app = Flask(__name__) #instanciar

basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "database.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Persona (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

# with app.app_context():
    # db.create_all()

@app.route("/")
def index():
    jon = Persona()
    jon.nombre = "jon"
    db.session.add( jon)
    db.session.commit()
    return "Hello World"

@app.route("/sql_all")
def sql_all():
    persona = Persona.query.get(2) # o tbn puede ser query.first()
    s = persona.nombre
    #personas = Persona.query.all()
    #return reder_template("personas.html", personas = ...)
    # personas = Persona.query.filter_by(salario > 2000)
    # s = ""
    # for p in personas:
    #     s = s + "  " + p.nombre
    return s 

 

if __name__ == "__main__":
    app.run(debug=False)