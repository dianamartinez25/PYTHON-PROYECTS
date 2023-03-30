#Seleccionar un valor aleatorio
#entre 12 y 18
#si es 15, imprimir "es 15!!"

# variable = input("Selecciona un valor aleatorio entre 12 y 18: ")
import random
# variable = random.randint(12, 18)
# if variable == 13:
#     print(f"Es {variable}!!")
# elif variable !=13:
#     print(f"Es {variable}")

lista = ("Jon", "Maria", "Juan", "Asier")
y = random.choice(lista)
print(y)
if y == "Maria" or y == "Juan":
    print("Maria y Juan no estan hoy en clase")
elif y == "Asier" or  y== "Jon":
    print("Asier y Jon estan en clase")

