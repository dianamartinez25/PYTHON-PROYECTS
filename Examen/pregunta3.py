# Esto es un programa de calculo.
# def area(a, b):
#     return a * b

# if __name__ == "__main__":
#     inicio = float(input("Dime la medida de la base: "))
#     second = float(input("Dame la medida de la altura: "))
#     z = area (inicio, second)
#     print(f"{z} es el área.")


#Modificar la función para que si el usuario ejecuta area(10), por defecto coge el valor 3 de altura (1)
def area (a, b):
    return a * b 

if __name__ == "__main__":
    inicio = float(input("Dime la medida de la base: "))
    if inicio == 10:
        second = 3
        z = area (inicio, second)
        print(f"{z} es el área.")
