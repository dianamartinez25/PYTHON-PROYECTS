# Crear progama con la función repetirXveces() para este código:
# pregunta = int(input("¿Cuantas veces quieres repetir?: "))
# def repetirXveces():
#     for p in range(pregunta):
#         print(p)
# repetirXveces()
# pass

d = float(input("¿Qué distancia vas a recorrer?: "))
t = float(input("¿Qué tiempo esperas tardar?: "))
v = float(input("¿A qué velocidad viajarás?:" ))

e = input("¿Qué parámetro deseas calcular? (d, t , v): ")

if e == "v":
    velocidad = d / t
    print (f"La velocidad es: {velocidad}")
elif e == "d":
    distancia = v * t
    print (f"La distancia es: {distancia}")
else:
    tiempo = d /v 
    print (f"El tiempo es: {tiempo}")

