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
    csm = moto("Honda", "Hornet", "diesel",90, 16, False, "2", "rojo")
    mnd = vehiculo("Mazda", "6", "gasolina", 120, 60, True, "4", "negro")
    csm.conducir()
    mnd.conducir(f"{csm.modelo}")
