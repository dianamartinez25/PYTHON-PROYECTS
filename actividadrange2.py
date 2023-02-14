# programa para contar
accion = input("¿Teclear 'up' para contar en positivo desde cero o teclear 'down' para contar en negativo? ")
if accion == "up":
    up = int(input("Dame una cifra: "))
    for p in range(0, up, 1):
        print(p)
#numeros_de_veces = int(input("¿Cuantas veces quieres repetir?"))
if accion == "down":
    down = int(input("Dame una cifra: "))
    for d in range(-1, down, -1):
        print(d)
