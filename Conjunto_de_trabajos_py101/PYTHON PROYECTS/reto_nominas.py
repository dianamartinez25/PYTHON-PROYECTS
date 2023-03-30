# Una compañera ha dejado el trabajo, me han pedido que continue con su proyecto de nominas.
#Usando su trabajo ya hecho, he de terminar el programa.
#RETO: Sistema para calcular las nóminas:


# notas:
# crear clases para:
# Empleado (atrbutos: nombre, salario; métodos calcular_salario (salario *1.1)
# Hay que desarollar más el método de calculo = hablar con analistas)
# Programador (atributos: lenguaje_de programacion)
# Quizás otros tipo de empleado Analista

# Requisitos para entregar:
# Diagrama de las clases
# Breve descripción del proyecto (unos líneas dentro del codigo)
# Código (a través de github)
# Separación de las clases en módulos

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_salario(self):
        print("Calculando salario")
    
class Programador(Empleado):
    def __init__(self, nombre, salario):
        super().__init__(self, nombre, salario)
    







if __name__ == "__main__":


# class Sistema_Nominas:
# # paramétro - una lista de clase Empleado
# def calcular_nominas(self, empleados):
# print("Calculando nominas")
# print ("=================")
# for empleado in empleados:
#     print(f"Nomina para: {empleado.name} - {empleado. lenguaje}")
# print(f"- $ : {empleado.calcular_nomina()}")
# print("")
# empleados = []
# #rellenar la lista de empleados con datos de diferentes tipos de empleados
# #Jon, programador de Python
# # Maria, programa dor de Java
# # Leo, programador de HTML
# #Ejecutar el metodo para calcular los salarios
# nominas = Sistema_Nominas()
# nominas. calcular_nominas(empleados)