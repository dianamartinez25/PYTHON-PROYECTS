class Vehiculo:
    
    def __init__(self,marca,modelo,fuelnivelactual,ruedas,color):
        self.marca=marca
        self.modelo=modelo
        self.fuelnivelactual=fuelnivelactual
        self.ruedas=ruedas
        self.color=color
        self.fuel_maximo=10
        self.conduzco=False
        self.estropeado=False
        self.fuel_minimo=5
    def conducir(self):
        if  self.estropeado==True  :
            print("No puedo conducir")
            
        elif self.fuel_nivel_actual < 5:
            print("Llenar deposito")
            self.llenar_deposito()


        else:
            print("Puedo conducir")
            self.fuelnivelactual=self.fuelnivelactual -1
            print(self.fuelnivelactual)

    def llenar_deposito(self):
            self.fuel_maximo=10
        
            self.conduzco=True
            print("Echo gasolina y puedo conducir")


    def averiado(self):
        
        if self.estropeado ==True:
            self.conduzco=False
            print("Vehiculo averiado")
        else:
            print("No averiado")
class Camion(Vehiculo):
    def __init__(self,marca,modelo,fuelnivelactual,ruedas,color,cabina):
        super().__init__(marca,modelo,fuelnivelactual,ruedas,color)
        self.cabina=cabina
    def dormir(self):
        print("Puedo dormir en el camion")

class Moto(Vehiculo):
    def __init__(self,marca,modelo,fuelnivelactual,ruedas,color,cadena,manillar):
        super().__init__(marca,modelo,fuelnivelactual,ruedas,color)
        self.cadena=cadena
        self.manillar=manillar
    def hacer_caballito(self):
        print("Con la moto puedo hacer el caballito")


if __name__=="__main__":
    
    veh1=Vehiculo("Focus","XX4",15,4,"Azul")
    veh1.estropeado=False
    veh1.llenar_deposito()
    cam=Camion("Pegaso","cxe4",10,8,"Verde",cabina=True)
    print(cam.dormir())
    mot1=Moto("bultaco","fgre",15,2,"Amarillo",8,120)
    print(mot1.hacer_caballito())
