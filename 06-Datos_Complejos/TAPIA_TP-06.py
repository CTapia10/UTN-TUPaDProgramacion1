## Trabajo practico 6 - Datos Complejos 
## Cristian Tapia - 2025


# Ejercicio 1
# Inicializo el diccionario con los precios de las frutas
precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva':1450}

# Agrego las nuevas frutas y sus precios
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
# print(precios_frutas.keys())
# print(precios_frutas.values())


# Ejercicio 2
# Actualizo el precio de las frutas
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800
# print(precios_frutas.keys())
# print(precios_frutas.values())


# Ejercicio 3
# Lista que contiene solo los nombres de las frutas
nombres_frutas = list(precios_frutas.keys())
# print(nombres_frutas)


# # Ejercicio 4
# # Defino agenda de contactos
# agenda_contactos = {}
# # Agrego contactos a la agenda
# for i in range(2):
#     agenda_contactos[input("Ingrese el nombre del contacto: ").strip().lower()] = input("Ingrese el numero de telefono del contacto: ").strip()
# while True:
#     nombre_consulta = input("Ingrese el nombre del numero que desea consultar: ").strip().lower()
#     if nombre_consulta in agenda_contactos:
#         print(f"El numero telefonico de {nombre_consulta.title()} es: {agenda_contactos[nombre_consulta]}")
#         break
#     else:
#         print(f"El nombre ingresado ({nombre_consulta.title()}) no se encuentra en la agenda de contactos")
#         continue


# # Ejercicio 5
# from collections import Counter
# # Pido al usuario una frase
# frase = input("Ingrese una frase: ").strip()
# # Formateo string para dividir en substrings
# palabras_frase = frase.lower().split()
# # Guardo las palabras unicas dentro de un set
# palabras_unicas = set(palabras_frase)
# # Uso clase Counter para contar la cantidad de palabras dentro de la lista palabras_frase y lo guardo en un diccionario
# cantidad_palabras = dict(Counter(palabras_frase))

# print(f"La cantidad veces que se utilizan las palabras de la string: {cantidad_palabras}")
# print(f"Las palabras unicas dentro de la string son: {palabras_unicas}")


# Ejercicio 6

# Utilizo el paquete statistics de python para utilizar funciones
from statistics import mean
# Defino diccionario de alumnos, que va a contener 3 notas por cada uno
alumnos = {}
print("Ingrese el nombre de 3 alumnos y sus notas")
for i in range(3):
    alumno = input("Nombre del alumno: ")
    alumnos[alumno] = (int(input("Primer nota: ")),int(input("Segunda nota: ")),int(input("Tercer nota: ")))
for alumno, notas in alumnos.items():
    promedio = mean(notas)
    print(f"El promedio del alumno: {alumno} es de: {promedio}")


# Ejercicio 7