# Trabajo practico 4 - Listas 
# Cristian Tapia - 2025

# # Ejercicio 1
# # Utilizo el paquete statistics de python para utilizar funciones
# from statistics import mean
# # Importo modulo random para utilizar metodo randint()
# import random
# # Inicializo lista que va a almacenar las notas de los alumnos
# listaNotas = []
# # Inicializo variables para guardar nota mas alta y nota mas baja
# notaBaja = 11
# notaAlta = -1
# # Rango de 10 notas
# for i in range(0,10):
#     listaNotas.append(random.randint(1,10))
   
#     # Condiciones para verificar si la nota es mas baja o mas alta
#     if (listaNotas[i] < notaBaja):
#         notaBaja = listaNotas[i]
#     elif (listaNotas[i] > notaAlta):
#         notaAlta = listaNotas[i] 
# media = mean(listaNotas)
# # Imprimo los resultados en pantalla
# print(f"Notas cargadas en el sistema: {listaNotas}")
# print(f"La media de las notas es: {media}")
# print(f"La nota mas baja es: {notaBaja} y la mas alta es: {notaAlta} ")


# # Ejercicio 2

# # Inicializo lista que va a almacenar los productos ingresados por el usuario
# listaProductos = []
# # Inicializo variable de rango limite "hasta" de la iteracion
# hastaPos = 5
# listaProductos.append(input("Ingrese el primer producto: "))
# # Utilizo un for para definir el rango de iteracion
# for num in range(1,hastaPos):
#     # Pido al usuario ingresar los productos
#     ## TODO: Averiguar funcion similar a TRIM() para formatear los datos ingresados y no haya espacios adicionales
#     listaProductos.append(input("Ingrese el siguiente producto: "))
# print(f"\n# Lista de productos: {sorted(listaProductos)} #")
# respuesta = int(input(f"\nDesea modificar algun producto?\n" \
#                     "   1. Si\n"\
#                     "   2. No\n"\
#                     "Respuesta: "))
# if (respuesta == 1):
#     while (respuesta != 3):
#         print(f"\n# Lista de productos hasta el momento: {sorted(listaProductos)} #\n")
#         respuesta = int(input("Elija una de las siguientes acciones:\n" \
#                             "   1. Agregar un producto\n"\
#                             "   2. Eliminar un producto\n"\
#                             "   3. Salir\n"\
#                             "Respuesta: "))
#         if (respuesta == 1):
#             listaProductos.append(input(f"Ingrese el producto que desea agregar a la lista: "))
#         elif (respuesta == 2):
#             listaProductos.remove(input(f"Ingrese el producto que desea eliminar de la lista: "))
# print(f"\n# Lista de productos final: {sorted(listaProductos)} #")
# # Reinicio respuesta
# respuesta = 0


# # Ejercicio 3

# # Importo modulo random para utilizar metodo randint()
# import random
# # Inicializo lista que va a almacenar los numeros al azar, los numeros pares y los numeros impares
# listaRandint = []
# listaPares = []
# listaImpares = []
# # Guardo en lista los 15 numeros al azar del 1 al 10
# for i in range(0,15):
#     listaRandint.append(random.randint(1,100))
# # Recorro la lista de numeros al azar y los guardo en su lista correspondiente
# for num in listaRandint:
#     if ((num % 2) == 0):
#         listaPares.append(num)
#     else:
#         listaImpares.append(num)
# # Muestro en pantalla las listas generadas con su contenido
# print(f"Lista con numeros pares : {listaPares}")
# print(f"Lista con numeros impares : {listaImpares}")

# # Ejercicio 4

# # Dada la lista "datos" con valores repetidos:
# datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
# datosSinRepetir = []
# for num in datos:
#     if num not in datosSinRepetir:
#         datosSinRepetir.append(num)
# print(f"Lista con datos repetidos : {datos}")
# print(f"Lista sin datos repetidos : {datosSinRepetir}")

# # Ejercicio 5

# # Inicializo lista que va a almacenar los nombres de los alumnos
# listaAlumnos = []
# # Inicializo variable de rango limite "hasta" de la iteracion
# HASTAPOS = 8
# listaAlumnos.append(input("Ingrese el primer nombre de la lista de estudiantes presentes: "))
# # Utilizo un for para definir el rango de iteracion
# for num in range(1,HASTAPOS):
#     # Pido al usuario ingresar los nombres de los alumnos
#     listaAlumnos.append(input("Ingrese el siguiente nombre de la lista: "))
# print(f"\n# Lista de alumnos presentes ingresados: {sorted(listaAlumnos)} #")
# respuesta = int(input(f"\nDesea realizar una modificacion?\n" \
#                     "   1. Si\n"\
#                     "   2. No\n"\
#                     "Respuesta: "))
# if (respuesta == 1):
#     while (respuesta != 3):
#         print(f"\n# Alumnos ingresados hasta el momento: {sorted(listaAlumnos)} #\n")
#         respuesta = int(input("Elija una de las siguientes acciones:\n" \
#                             "   1. Agregar un alumno a la lista\n"\
#                             "   2. Eliminar un alumno de la lista\n"\
#                             "   3. Salir\n"\
#                             "Respuesta: "))
#         if (respuesta == 1):
#             listaAlumnos.append(input(f"Ingrese el alumno que desea agregar a la lista: "))
#         elif (respuesta == 2):
#             listaAlumnos.remove(input(f"Ingrese el alumno que desea eliminar de la lista: "))
# print(f"\n# Lista de alumnos presentes final: {sorted(listaAlumnos)} #")