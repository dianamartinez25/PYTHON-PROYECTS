class vehiculo:
    def __init__(self, marca, modelo, tipo, fuel_Maximo, fuel_Nivel_Actual, averiado, ruedas, color):
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.fuel_Maximo = fuel_Maximo
        self.fuel_Nivel_Actual = fuel_Nivel_Actual
        self.averiado = False
        self.ruedas = ruedas
        self.color = color

    def conducir(self):
        print("Estoy conduciendo")

class camion(vehiculo):
    def __init__(self, marca, modelo, tipo, fuel_Maximo, fuel_Nivel_Actual, averiado, ruedas, color):
        super().__init__(self, marca, modelo, tipo, fuel_Maximo, fuel_Nivel_Actual, averiado, ruedas, color)
        
    def conducir(self):
        print("Estoy conduciendo un camión")

class moto(vehiculo):
    def __init__(self, marca, modelo, tipo, fuel_Maximo, fuel_Nivel_Actual, averiado, ruedas, color):
        super().__init__(self, marca, modelo, tipo, fuel_Maximo, fuel_Nivel_Actual, averiado, ruedas, color)
        
    def conducir(self):
        print("Estoy conduciendo una moto")

if __name__ == "__main__":
    csm = vehiculo()