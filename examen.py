# Crear progama con la función repetirXveces() para este código:
# pregunta = int(input("¿Cuantas veces quieres repetir?: "))
# def repetirXveces():
#     for p in range(pregunta):
#         print(p)
# repetirXveces()
# pass
# *****************************************************************#
# d = float(input("¿Qué distancia vas a recorrer?: "))
# t = float(input("¿Qué tiempo esperas tardar?: "))
# v = float(input("¿A qué velocidad viajarás?:" ))

# e = input("¿Qué parámetro deseas calcular? (d, t , v): ")

# if e == "v":
#     velocidad = d / t
#     print (f"La velocidad es: {velocidad}")
# elif e == "d":
#     distancia = v * t
#     print (f"La distancia es: {distancia}")
# else:
#     tiempo = d /v 
#     print (f"El tiempo es: {tiempo}")
# *****************************************************************#

#lista_notas = [5, 6, 4, 3, 3, 9, 10, 8]
# for i in lista_notas:
#     if i < 5:
#         print ("Lo siento no has aprobado")
    
#print(any(nota < 5 for nota in lista_notas))
# *****************************************************************#
# jon = (True, False, False, True, False)

# maria = (True, True, True, True, True)
# #Ganó jon todos los partidos? False
# #Ganó maria todos los partidos? True
# for j in jon:
#     if j == True:
#         print ("True")
#     elif j != True:
#         print ("False")

# print(all(jon))
#*****************************************************************#
#Funciones
#Crear la función para sumar 3 números
# def sumar(a , b, c):
#     return a + b + c 

# total = sumar(6, 7, 7)
# print (total)
#*****************************************************************#
#Clases
#Crear una función para validar los datos de un producto:
#ºEl nombre del producto tiene que empezar en MAYÚSCULAS.
#ºEl precio es mayor a 10 euros.
#º La cantidad disponible es entre 1 y 100.
class producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    def equipo():
        print("Bienvenid@s")

class perfume(producto):
    def __init__(self, nombre, precio, stock):
        super().__init__(self, nombre, precio, stock)
    def olor():
        print(" florales y citricos")

if __name__ == "__main__":
    

#         nombre = "Paradise"
#         precio = 10 > 0
#         stock = 100
#     value = input("¿Qué producto estás buscando?")
# for v in value:
#     if v != nombre:
#         print("Error")
#     elif v == nombre:
#         print ("Sí lo tenemos.")
# cantidad = input("¿cuántos quieres?")
# for c in cantidad:
#     if c > stock:
#         print("Lo siento no tenemos más de 100 unidades en stock...")
#     else:
#         c <= stock
#         print(" Gracias por su compra")

