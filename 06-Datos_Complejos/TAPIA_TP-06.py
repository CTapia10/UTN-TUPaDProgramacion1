# Trabajo practico 6 - Datos Complejos 
# Cristian Tapia - 2025



# Ejercicio 1
# Inicializo el diccionario con los precios de las frutas
precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva':1450}
#Agrego las nuevas frutas y sus precios
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas.keys())
print(precios_frutas.values())



# Ejercicio 2
# Actualizo el precio de las frutas
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800
print(precios_frutas.keys())
print(precios_frutas.values())



# Ejercicio 3
# Lista que contiene solo los nombres de las frutas
nombres_frutas = list(precios_frutas.keys())
print(nombres_frutas)



# Ejercicio 4
# Defino agenda de contactos
agenda_contactos = {}
# Agrego contactos a la agenda
for i in range(2):
    agenda_contactos[input("Ingrese el nombre del contacto: ").strip().lower()] = input("Ingrese el numero de telefono del contacto: ").strip()
while True:
    nombre_consulta = input("Ingrese el nombre del numero que desea consultar: ").strip().lower()
    if nombre_consulta in agenda_contactos:
        print(f"El numero telefonico de {nombre_consulta.title()} es: {agenda_contactos[nombre_consulta]}")
        break
    else:
        print(f"El nombre ingresado ({nombre_consulta.title()}) no se encuentra en la agenda de contactos")
        continue



# Ejercicio 5
from collections import Counter
# Pido al usuario una frase
frase = input("Ingrese una frase: ").strip()
# Formateo string para dividir en substrings
palabras_frase = frase.lower().split()
# Guardo las palabras unicas dentro de un set
palabras_unicas = set(palabras_frase)
# Uso clase Counter para contar la cantidad de palabras dentro de la lista palabras_frase y lo guardo en un diccionario
cantidad_palabras = dict(Counter(palabras_frase))

print(f"La cantidad veces que se utilizan las palabras de la string: {cantidad_palabras}")
print(f"Las palabras unicas dentro de la string son: {palabras_unicas}")



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
# Defino los 2 sets de notas para los parciales
# Notas primer parcial
notas_parcial_uno = {7,5,9,4,3,1,10,8}
# Notas segundo parcial
notas_parcial_dos = {6,4,7,1,5,3,2,10}
# Defino set con notas que significan desaprobado
notas_desaprobado = {0,1,2,3,4,5}
ambos_aprobados = (notas_parcial_uno & notas_parcial_dos) - notas_desaprobado
solo_uno_aprobado = (notas_parcial_uno ^ notas_parcial_dos) - notas_desaprobado
al_menos_uno_aprobado = (notas_parcial_uno | notas_parcial_dos) - notas_desaprobado
print(f"Notas de estudiantes que aprobaron los dos parciales: {ambos_aprobados}")
print(f"Notas de estudiantes que aprobaron solo uno: {solo_uno_aprobado}")
print(f"Notas de estudiantes que aprobaron al menos uno: {al_menos_uno_aprobado}")



# Ejercicio 8
# Defino funcion para verificar si existe el producto en el catalogo
def MuestroCatalogo(productos_stock):
    print("="*16+"Catálogo de productos"+"="*16)
    for i, (producto, stock) in enumerate(productos_stock.items()):
        print(f"{i}.{producto} ({stock})")
    print("="*53+"\n")

def EsDiccVacio(dicc):
    if not dicc:
        return True
    else:
        False
    
def ExisteProductoEn(prod,catalogo):
    if prod in catalogo or prod == "":
        print("\n ⚠️  Ingreso un producto vacío o esta repetido en el catalogo.\n")
        return True
    else:
        return False
    
# Defino dict que va a contener claves con nombre de productos y los valores de su stock
productos_stock = {}
opciones_menu_principal = ["1. Agregar producto",
                "2. Ingresar stock",
                "3. Consultar stock",
                "4. Salir"]
while True:
    # Mostramos las opciones del menu al usuario
    print("="*54)
    print("Bienvenido al catálogo de productos, elija una opción")
    print("="*54)
    for opcion in opciones_menu_principal:
        print(opcion)
    print("="*54)
    # Pedimos al usuario que seleccione una de las opciones
    seleccion = input("Opción seleccionada: ").strip()
    print("="*54+"\n")
    match seleccion:
        case "1":
            nuevo_producto = input("Ingrese el producto que desea agregar al catálogo: ").strip().capitalize()
            if ExisteProductoEn(nuevo_producto,productos_stock):
                continue
            else:
                productos_stock.setdefault(nuevo_producto, 0)
                print(f"\n✅ Se ingreso con éxito el producto: {nuevo_producto} al catalogo. \n")
                
        case "2":
            # Si no hay productos cargados no debe permitir agregar stock
            if EsDiccVacio(productos_stock):
                print("⚠️  No existen productos en el catálogo. Para ingresar la cantidad de unidades primero debe ingresar productos.\n")
                continue
            # En caso que existan muestro los productos actuales para que el usuario seleccione al cual desea agregar stock
            MuestroCatalogo(productos_stock)
            producto_agregar_stock = input("Ingrese el producto al que desea agregarle unidades: ").strip().capitalize()
            if producto_agregar_stock in productos_stock:
            # Verifico que la cantidad de unidades a ingresar sea valida
                while True:
                    cantidad = input("\nIngrese las unidades que desea agregar al stock: ").strip()
                    if not cantidad.isdigit():
                        print("\n ⚠️  Ingrese una cantidad valida (numero entero mayor a 0).")
                        continue
                    # Despues de verificar que no hayan signos especiales transformo a entero
                    cantidad = int(cantidad)
                    if cantidad <= 0:
                        print("\n ⚠️  Ingrese una cantidad valida (numero entero mayor a 0).\n")
                        continue
                    break
                productos_stock[producto_agregar_stock] =+ cantidad
                print(f"\n✅ Se agregaron con éxito {cantidad} unidades al producto: {producto_agregar_stock}. \n")
            else:
                print(f"⚠️  No existe el producto {producto_agregar_stock} en el catálogo. Ingrese un producto valido.\n")
                continue
            
        case "3":
            if EsDiccVacio(productos_stock):
                print("⚠️  No existen productos en el catálogo.\n")
                continue
            else:
                MuestroCatalogo(productos_stock)
        case "4":
            print("Saliendo del programa... ¡Hasta luego!")
            break
        # Opcion inválida
        case _:
            print("⚠️  Opción inválida. Por favor, elija una opción del 1 al 4.\n")
            continue



# Ejercicio 9 
# Defino agenda con dias horarios y su actividad
agenda = {("lunes","10:00"): "Reunion",
        ("martes","16:00"): "Clase de ingles",
        ("miercoles","14:00"): "Clase de matematicas",
        ("jueves","11:00"): "Clase de programacion",
        ("viernes","15:00"): "Evento especial",
        ("sabado","20:00"): "Fiesta de cumpleaños",
        ("domingo","09:00"): "Entrenar"}
print("Para consultar en la agenda ingrese dia y hora")
dia = input("Indique el dia: ")
hora = input("Indique la hora en formato correcto (hh:mm): ")
if (dia,hora) in agenda:
    print(f"La actividad para el dia {dia} en la agenda es: {agenda[(dia,hora)]}")
else:
    print(f"No hay actividad para el dia {dia} en la agenda")



# Ejercicio 10
# Defino diccionario original con valores de ejemplo
original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
# Inicializo diccionario invertido
invertido = {}
# Para cada key y valor en el diccionario "original" inserto key y valor invertidos en el diccionario "invertido"
for key, valor in original.items():
    invertido[valor] = key
# Muestro en pantalla el resultado
print(f"Diccionario original: {original}")
print(f"Diccionario invertido: {invertido}")