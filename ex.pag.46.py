#Como un arquitecto quiero calcular metros cuadrados (m2) de una Superticie (largo y ancho)
#para no tener que calcularlo de forma manual y posiblemente calcularlo incorrectamente.

import time 
DORMIR = 0.30

def superficie(n,m):
    return n * m 


if __name__ == "__main__":
   l = float(input("Dame el largo: "))
   time.sleep(DORMIR)
   a = float(input("Dame el ancho: "))
   r = superficie(l, a)
   print(f"Tu superficie es de {r} m2")
