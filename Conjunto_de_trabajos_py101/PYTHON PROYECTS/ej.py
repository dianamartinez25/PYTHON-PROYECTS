import platform
import os

print(os.name)
print(platform.uname())

print(os.getcwd())

path = os.path.join(os.getcwd(), "carpeta")
print(path)

print(os.path.split(os.getcwd()))

#cambiar 'abc' para un archivo en tu directorio working.
print(os.path.isfile(os.path.join(os.getcwd(), "abc.py")))
#Cambiar 'carpeta' para una carpeta en tu directorio working.
print(os.path.isdir(os.path.join(os.getcwd(), "carpeta")))
#Cambiar 'carpeta' para un carpeta en tu directorio working
print(os.path.exists(os.path.join(os.getcwd(), "carpeta")))