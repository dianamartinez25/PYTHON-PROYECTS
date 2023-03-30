#Completar las funciones de este programa.
#devolver el nombre de usuario
def get_usuario():
    usuario = input( "Introduce tu nombre de usuario: ")
    return usuario

def get_edad():
    edad = input("Introduce tu edad: ")
    return edad

def get_password():
    password = input("Introduce tu contraseña: ")
    return password

#programa main()
if __name__ == "__main__":
    usuario = get_usuario()
    edad = get_edad()
    password = get_password()

print(f"Bienvenido {usuario}. Tu edad es {edad} y tu contraseña es {password}.")