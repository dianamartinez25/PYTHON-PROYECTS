#El objetivo de este programa es introducir la edad de los usuarios la veces que sean necesarias para que los datos que se metan no sean incorrectos.
limite_max = 65
limite_min = 18
l = int(input("Introduce la edad del usuario: "))
if l < limite_min:
    print("Lo siento es muy joven")
if l > limite_max:
    print("Es demasiado mayor")
respuesta = input("¿Quieres continuar? (s/n) ")
while respuesta == "s":
    limite_min = 18
    limite_max = 65 
    l = int(input("Introduce la edad del usuario: "))
    if l < limite_min:
       print("Lo siento es muy joven")
    if l > limite_max:
        print("Es demasiado mayor")
    respuesta = input("¿Quieres continuar? (s/n) ")


if respuesta == "n":
    print("Fin del programa.")
