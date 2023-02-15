#TRABAJO HECHO EN CASA:
    
    
# programa para gestionar los invitados de la fiesta
fiesta=[]
print("Estamos organizando los preparativos para la fiesta que daremos este fin de semana. A continuación os haremos unas preguntas: ")

gente = int(input("¿Cuánta gente acudirá a la fiesta?: "))
MAX_INVITADOS  = 10
if gente > MAX_INVITADOS:
    print(f"Lo siento, solo se admiten {MAX_INVITADOS} personas para acudir a la fiesta. ")
else:
    for i in range(gente):
        invitados = (input("¿Podrías decirme el nombre de cada invitado? "))
        print(f"Bienvenido a la fiesta {invitados}")
        fiesta.append(invitados)

print(fiesta)

   #más :
    # preguntar al usuario por el nombre de cada invitado. - repetir X veces.
    # imprimir un mensaje individual para cada invitado.


    # avanzado - guardar cada nombre en una lista e imprimir la lista al final del programa
    #pista - invitados.append()
