#Esto es un programa para imprimir valores de una lista:

# Imprimir los valores de esta lista, excluyendo los valores en negativo (2)
# Al imprimir, imprimes "Hola numero 6" si el valor es 6. (1)
lista = [5, 3, 12, -6, -3, 1, 6, 8, -12]
for l in lista:
    if l < 0:
        continue 
    print(lista)