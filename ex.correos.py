# Generar un informe con:
# - los nombres de los usuarios e.g. jon.smith, maria.fernandez
emails = ["jon.smith@microsoft.com","maria.fernandez@gmail.com"]
nombres = ("jon","maria")
dominios = []
for email in emails:
  nombre, dominio = email.split("@")
  print(nombre)
  if dominio not in dominios:
    dominios.append(dominio)
print(dominios)
x = dominios[0]
y = dominios[1]
correos = []
for nombre in nombres:
  correo = nombre + x
  corre = nombre + y
  correos.append(correo)
  correos.append(corre)

texto = ",".join(correos)
print(texto)
