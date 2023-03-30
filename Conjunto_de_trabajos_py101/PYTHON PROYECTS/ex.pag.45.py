#ACTIVIDAD 1
#Completar la función para imprimir el número X veces a la pantalla:
#devolver el número del usuario
# def get_numero():
#     numero = int(input("Introduce un número: " ))
#     return numero
 
# # imprimir un número x veces, imprimiendolo a la pantalla
# # parámetros contar - int
# def repetir_numero(numero):
#     for n in range(numero):
#         print(numero)
        
# if __name__ == "__main__":
#     print("Esto es un programa para repetir un número. ")
#     numero = get_numero()
#     repetir_numero((numero))

#ACTIVIDAD 2
import time
DORMIR = 0.10 # segundos
DORMIR1 = 0.50
DORMIR2 = 0.60
def msg():
    print("Me he despertado " )

def msg_medio():
    print("He desayunado")

def msg_final():
    print("Me he ido al trabajo")

if __name__== "__main__":
    time.sleep ( DORMIR)
    msg()
    time.sleep (DORMIR2)
    msg_medio()
    time.sleep(DORMIR1)
    msg_final()
 