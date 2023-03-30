#Usando este texto, llevar a cabo:
texto = "    Lo más importante que nos ha mantenido en Python... bueno, hay 2 cosas importantes. Uno son las bibliotecas. La otra cosa que nos mantiene en Python, y esto es lo más importante, es facil de leer y entender. Cuando contratamos nuevos empleados. Solo digo, 'todo lo que escribas debe estar en python'. Sólo para que pueda leerlo. Y es increíble porque puedo ver desde el otro lado de la habitación, mirando su pantalla, si su código es bueno o malo. Porque un buen código de Python tiene una estructura muy obvia. Y eso hace que mi vida sea mucho más fácil        "

#Usar swapcase, replace, upper, in, count, find, strip

# 1: Contar las veces que la palabra Python aparece en el texto...y si a veces aparece en el texto con mayusculas y minusculas - Python, python
#z = texto.count("Python")
#l = texto.count("python")
# print(z + l)

# 2: Encontrar la ubicación (numero/indice de carácter) donde esta la primera ocurrencia de la palabra Python. ¿Y la segunda? ¿La palabra 'código' está en el texto? Usar if ... in ...:
# m = texto.find("Python")
# d = texto.find("Python", 50, len(texto))
# print(m)
# print(d)
if "código"  in texto:
    g= texto.find("código")
    print(g)

# 3: Reemplazar Python por PYTHON
#texto = texto.replace("Python", "PYTHON")

# 4: Quitar los espacios al inicio/final
texto = texto.strip()

# 5: Cambiar la letra de todo el texto a "lO MÁS IMPORTANTE QUE NOS HA MANTENIDO EN pYTHON... " - no usar replace
# x = texto.swapcase()
# print(x)
