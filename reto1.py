#Este programa está hecho por Diana Martínez el día 14/02/23
print("Vamos a hacer una conversión de kilos a libras o viceversa:")
pregunta = input("¿Quieres calcular kilos o libras? (k/l): ")
if pregunta == "k":
    kilos = float(input("Dime cuántos kilos: "))
    pesolibras = kilos*2.20
    print(f"son {pesolibras} libras.")
if pregunta == "l":
    libras = float(input("Dime cuántas libras: "))
    pesokilos = libras/2.20
    print(f"son {pesokilos} kilos.")




