class persona:

    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def hablar(self):
        print(f"Hola , soy {self.nombre}")
    

# jon = persona("Jon" , 18)
# print(jon.edad)
# jon.hablar()

# maria = persona("María" , 40)
# print(maria.nombre)
# print(maria.edad)
# maria.hablar()

personas = []
#Simulacro de lo que sería un interfaz de usuario.
if __name__ == "__main__":
    nombre = input("Introducir un nombre del usuario")
    edad = input("Introducir su edad")
    Persona = persona(nombre, edad)
    personas.append(Persona)