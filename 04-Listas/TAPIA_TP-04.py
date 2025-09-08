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
#     listaProductos.append(input("Ingrese el siguiente producto: "))
# print(f"Lista de productos: {sorted(listaProductos)}\n")
# respuesta = int(input("Desea modificar algun producto de la lista?:\n" \
#                     "   1. Si\n"\
#                     "   2. No\n"\
#                     "Respuesta: "))
# if (respuesta == 1):
#     while (respuesta != 3):
#         respuesta = int(input("\nElija una de las siguientes acciones:\n" \
#                             "   1. Agregar un producto\n"\
#                             "   2. Eliminar un producto\n"\
#                             "   3. Salir\n"\
#                             "Respuesta: "))
#         if (respuesta == 1):
#             listaProductos.append(input("Ingrese el producto que desea agregar a la lista: "))
#         elif (respuesta == 2):
#             listaProductos.remove(input(f"Ingrese el producto que desea eliminar de la lista {sorted(listaProductos)}: "))
# print(f"\nLista de productos: {sorted(listaProductos)}")
# # Reinicio respuesta
# respuesta = 0


