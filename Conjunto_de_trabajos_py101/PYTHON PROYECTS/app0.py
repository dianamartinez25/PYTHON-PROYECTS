from flask import Flask, render_template

app = Flask(__name__) #instanciar
class Empleado:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


@app.route("/") #acceso a ruta dentro de la web (en este caso no hay ruta)
def hello_world():
    jon = Empleado("Jon", "Smith", 25)
    return render_template("index.html",empleado = jon ) # Lo que aparece principalmente en la web o entorno "*<p>kjd<p>*"

@app.route("/adios") #ruta dentro de la web
def adioós():
    sHTML = "<h1>GOODBYEE</h1>"
    sHTML = sHTML + "<h2>GOODBYEE!!</h2>"
    return sHTML

@app.route("/help")
def ayuda():
    return "Si necesitas ayuda contactanos: 943442516"

if __name__ == "__main__":
    app.run() #( punto de acceso a servidor web)

#"<h1>jbhfeudfwehi<h1>"
#"<h2>wkndnhfkenhfie<h2>"