class Instrumento:
    def __init__(self, nombre, tipo, precio, cuerdas):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
        self.cuerdas = cuerdas
        self.__precio_coste = precio - 20

    def tocar(self):
        print(f"{self.nombre} está tocando y tiene: {self.cuerdas}")

class Piano(Instrumento):
    def __init__(self, nombre, tipo, precio, cuerdas, teclas):
          super().__init__(nombre, tipo, precio, cuerdas)
          self.teclas = teclas
    
    def tocar(self):
        print("Melodía de piano")


guitarra = Instrumento("guitarra", "cuerdas", 100, 20)
guitarra.tocar()
piano1 = Piano("piano", "teclas", 200, 50, 120)
print(piano1.teclas)
piano1.tocar()