#Como un arquitecto quiero calcular metros cuadrados (m2) de una Superticie (largo y ancho)
#para no tener que calcularlo de forma manual y posiblemente calcularlo incorrectamente.
def superficie(n,m):
    return n * m 
import time 
DORMIR = 0.30
l = float(input("Dame el largo: "))
time.sleep(DORMIR)
a = float(input("Dame el ancho: "))
if __name__ == "__main__":
   r = superficie(l, a)
   print(f"Tu superficie es de {r} m2")