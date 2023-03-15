from flask import Flask, render_template
app1 = Flask(__name__)
lista_de_coches = []
class Vehiculo:
    def __init__(self, nombre, modelo, año , color, imagen):
        self.nombre = nombre
        self.modelo = modelo
        self.año = año
        self.color = color
        self.imagen = imagen

v1 = Vehiculo("Mazda", "6", "2016", "azul", "mazda.jpg")
v2 = Vehiculo("Audi", "A6", "2023", "gris", "2023.jpg" )
v3 = Vehiculo("Hyundai", "Creta", "2017", "blanco", "Creta.jpg")
lista_de_coches.append(v1)
lista_de_coches.append(v2)
lista_de_coches.append(v3)

@app1.route("/")
def motor():
    return render_template("index1.html", coche = lista_de_coches)

if __name__ == "__main__":
    app1.run()
