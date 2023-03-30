class Perro:

    def __init__(self, nombre , raza , altura):
        self.nombre = nombre
        self.raza = raza
        self.altura = altura
    
    def comer(self):
        print(self.nombre + " está comiendo y es de la raza " + self.raza + ". Mide " + str(self.altura))
    
    def dormir(self):
        print("Mi perro está durmiendo")
    
    def ladrar(self):
        print("Mi perro está ladrando")
    def mostrar_datos(self):
        print(self.nombre, self.raza, self.altura)
    

# Eren = perro("Eren", "pitbull", 1.20)
# Eren.comer()

canes = []
if __name__ == "__main__":
    nombre = input("Dime el nombre: ")
    raza = input("Dime la raza: ")
    altura = input("Dime la altura: ")
    perros = Perro(nombre, raza, altura)
    nombre = input("Dime el nombre: ")
    raza = input("Dime la raza: ")
    altura = input("Dime la altura: ")
    perro1 = Perro(nombre, raza, altura)
    canes.append(perros)
    canes.append(perro1)
    #print(canes)
    for p in canes:
        p.mostrar_datos()
