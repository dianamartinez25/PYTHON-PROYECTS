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

@app.route("/")
def index():
    jon = Persona()
    jon.nombre = "jon"
    db.session.add(jon)
    db.session.commit()
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=False)