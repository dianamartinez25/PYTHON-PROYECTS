#Usando las notas que he recibido de una programadora,he construido las clases necesarias para este programa.

class Animal():
    def __init__(self, patas, nombre, raza):
        self.patas = patas
        self.nombre = nombre
        self.raza = raza

class Perro(Animal):
    def __init__(self, patas, nombre, raza):
        super().__init__(self, patas, nombre, raza)
        
    def hacer_ruido(self):
        print("Woof, woof!")
    def correr(self):
        print("Estoy corriendo!")


class Pajaro(Animal):
    def __init__(self, patas, nombre,raza):
        super().__init__(self, patas, nombre,raza)
        self.raza = raza
    def hacerRuido(self):
        print ("Tweet, tweet!")
    def volar(self):
        pass  # todavia no tenemos detalles de este método


if __name__ == "__main__":
    a = Perro(4 , "Sasha", "Doberman")
    b = Pajaro(2, "Mel")
    a.hacer_ruido()
    a.correr()
    print(a)