#ACTIVIDAD 1
#Preguntar al usuario por su nombre y edad. Mostrar el siguiente mensaje:
# “[nombre] cumplirás [edad] en tu siguiente cumpleaños.”

# import time
# DORMIR = 5
# DORMIR1 = 3
# DORMIR2 = 4
# print("Bienvenid@, a continuación vamos a hacerte unas preguntas para saber más sobre ti:")
# time.sleep(DORMIR) 
# p = input("¿Quieres continuar?, (s/n): ")
# if p == "n" or p == "N":
#     print("Otra vez será.")
# else:
#     p == "s" or p == "S"
#     print("Prosigamos:")
#     time.sleep(DORMIR1)
#     nombre = input("¿Cuál es tu nombre?: ")
#     nombre = nombre.capitalize()
#     time.sleep(DORMIR1)
#     edad = int(input("¿Qué edad tienes?: "))
#     time.sleep(DORMIR1)
#     print("Login ...")
#     edad1 = edad + 1
#     time.sleep(DORMIR2)
#     print(f"Hola {nombre}, nos alegra conocerte.")
#     time.sleep(DORMIR1)
#     print(f"Tienes {edad} años y en tu próximo cumpleaños cumplirás {edad1} años.")
#     time.sleep(DORMIR2)
#     print("¡Gracias por confiar en nosotros!")

#ACTIVIDAD 2
# Crear un programa para conseguir el siguiente resultado en la pantalla,
# donde pregunta al usuario por sus dos compañeros:
# “Tus compañeros son Maria y Jon”

import time
DORMIR = 2.5
DORMIR2 = 2
print("Esto es una prueba de programa:")
time.sleep(DORMIR)
print("Hola..")
n = input("¿Cómo te llamas?")
n = n.capitalize()
time.sleep(DORMIR)
c = input(f"{n}, ¿conoces a todos tus compañeros de clase?: (s/n):")
 
 if c == "n" or c == "N":
    print("Para que este programa funcione debes darme nombres ...")

 else:
    c == "s" or c == "S"



# Ejecutar este instrucción:
# >> print("Hola", 2023, "Agura", 5_000_000_000)

# Cúal es la diferencia entre estas instrucciones:
# >> hijos = input("¿Cuántos hijos tienes?")
# >> print(hijos*5)
# y
# >> hijos = int(input("¿Cuántos hijos tienes?"))
# >> print(hijos*5)
