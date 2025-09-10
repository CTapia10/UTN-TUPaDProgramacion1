# Trabajo practico 4 - Listas 
# Cristian Tapia - 2025

# Ejercicio 1
# Utilizo el paquete statistics de python para utilizar funciones
from statistics import mean
# Importo modulo random para utilizar metodo randint()
import random
# Inicializo lista que va a almacenar las notas de los alumnos
listaNotas = []
# Inicializo variables para guardar nota mas alta y nota mas baja
notaBaja = 11
notaAlta = -1
# Rango de 10 notas
for i in range(0,10):
    listaNotas.append(random.randint(1,10))
   
    # Condiciones para verificar si la nota es mas baja o mas alta
    if (listaNotas[i] < notaBaja):
        notaBaja = listaNotas[i]
    elif (listaNotas[i] > notaAlta):
        notaAlta = listaNotas[i] 
media = mean(listaNotas)
# Imprimo los resultados en pantalla
print(f"Notas cargadas en el sistema: {listaNotas}")
print(f"La media de las notas es: {media}")
print(f"La nota mas baja es: {notaBaja} y la mas alta es: {notaAlta} ")


# Ejercicio 2
# Inicializo lista que va a almacenar los productos ingresados por el usuario
listaProductos = []
# Inicializo variable de rango limite "hasta" de la iteracion
hastaPos = 5
listaProductos.append(input("Ingrese el primer producto: "))
# Utilizo un for para definir el rango de iteracion
for num in range(1,hastaPos):
    # Pido al usuario ingresar los productos
    ## TODO: Averiguar funcion similar a TRIM() para formatear los datos ingresados y no haya espacios adicionales
    listaProductos.append(input("Ingrese el siguiente producto: "))
print(f"\n# Lista de productos: {sorted(listaProductos)} #")
respuesta = int(input(f"\nDesea modificar algun producto?\n" \
                    "   1. Si\n"\
                    "   2. No\n"\
                    "Respuesta: "))
if (respuesta == 1):
    while (respuesta != 3):
        print(f"\n# Lista de productos hasta el momento: {sorted(listaProductos)} #\n")
        respuesta = int(input("Elija una de las siguientes acciones:\n" \
                            "   1. Agregar un producto\n"\
                            "   2. Eliminar un producto\n"\
                            "   3. Salir\n"\
                            "Respuesta: "))
        if (respuesta == 1):
            listaProductos.append(input(f"Ingrese el producto que desea agregar a la lista: "))
        elif (respuesta == 2):
            listaProductos.remove(input(f"Ingrese el producto que desea eliminar de la lista: "))
print(f"\n# Lista de productos final: {sorted(listaProductos)} #")
# Reinicio respuesta
respuesta = 0


# Ejercicio 3
# Importo modulo random para utilizar metodo randint()
import random
# Inicializo lista que va a almacenar los numeros al azar, los numeros pares y los numeros impares
listaRandint = []
listaPares = []
listaImpares = []
# Guardo en lista los 15 numeros al azar del 1 al 10
for i in range(0,15):
    listaRandint.append(random.randint(1,100))
# Recorro la lista de numeros al azar y los guardo en su lista correspondiente
for num in listaRandint:
    if ((num % 2) == 0):
        listaPares.append(num)
    else:
        listaImpares.append(num)
# Muestro en pantalla las listas generadas con su contenido
print(f"Lista con numeros pares : {listaPares}")
print(f"Lista con numeros impares : {listaImpares}")


# Ejercicio 4
# Dada la lista "datos" con valores repetidos:
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datosSinRepetir = []
for num in datos:
    if num not in datosSinRepetir:
        datosSinRepetir.append(num)
print(f"Lista con datos repetidos : {datos}")
print(f"Lista sin datos repetidos : {datosSinRepetir}")


# Ejercicio 5
# Inicializo lista que va a almacenar los nombres de los alumnos
listaAlumnos = []
# Inicializo variable de rango limite "hasta" de la iteracion
HASTAPOS = 8
listaAlumnos.append(input("Ingrese el primer nombre de la lista de estudiantes presentes: "))
# Utilizo un for para definir el rango de iteracion
for num in range(1,HASTAPOS):
    # Pido al usuario ingresar los nombres de los alumnos
    listaAlumnos.append(input("Ingrese el siguiente nombre de la lista: "))
print(f"\n# Lista de alumnos presentes ingresados: {sorted(listaAlumnos)} #")
respuesta = int(input(f"\nDesea realizar una modificacion?\n" \
                    "   1. Si\n"\
                    "   2. No\n"\
                    "Respuesta: "))
if (respuesta == 1):
    while (respuesta != 3):
        print(f"\n# Alumnos ingresados hasta el momento: {sorted(listaAlumnos)} #\n")
        respuesta = int(input("Elija una de las siguientes acciones:\n" \
                            "   1. Agregar un alumno a la lista\n"\
                            "   2. Eliminar un alumno de la lista\n"\
                            "   3. Salir\n"\
                            "Respuesta: "))
        if (respuesta == 1):
            listaAlumnos.append(input(f"Ingrese el alumno que desea agregar a la lista: "))
        elif (respuesta == 2):
            listaAlumnos.remove(input(f"Ingrese el alumno que desea eliminar de la lista: "))
print(f"\n# Lista de alumnos presentes final: {sorted(listaAlumnos)} #")


# Ejercicio 6
# Importo modulo random para utilizar metodo randint()
import random
listaRandint = []
listaRotada = []
# Defino lista con 7 numeros al azar
for i in range(0,7):
    listaRandint.append(random.randint(1,100))
    # Guardo en listaRotada lo mismo que listaRandint
    listaRotada.append(listaRandint[i])
# Saco el ultimo numero de la lista y lo guardo en variable ultimoNum
ultimoNum = listaRotada.pop()
# Agrego el ultimo numero de la lista al principio
listaRotada.insert(0,ultimoNum)
print(f"Lista con datos repetidos : {listaRandint}")
print(f"Lista sin datos repetidos : {listaRotada}")


# Ejercicio 7
# Utilizo el paquete statistics de python para utilizar funciones
from statistics import mean
# Importo modulo random para utilizar metodo randint()
import random
# Inicializo lista con dias de la semana
semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
# Inicializo lista anidada
lista_temperaturas = []
# Inicializo variables de temperatura minima y maxima
maxTemp = -1
minTemp = 41
mayorAmplitud = 0
diaMayorAmplitud = ""
# Recorro cada dia de la semana y genero las temperaturas
for dia in range(len(semana)):
    lista_temperaturas.append([random.randint(0,15),random.randint(16,40)])
    # Calculo la amplitud y la guardo en la variable junto a su dia correspondiente
    amplitudDia = (lista_temperaturas[dia][1] - lista_temperaturas[dia][0])
    if (amplitudDia > mayorAmplitud):
        mayorAmplitud = amplitudDia
        diaMayorAmplitud = semana[dia]
    # Si la temperatura del dia supera la maxima la guardo como temperatura maxima
    if (lista_temperaturas[dia][0] > maxTemp):
        maxTemp = lista_temperaturas[dia][0]
    # Si la temperatura del dia supera la minima la guardo como temperatura minima
    if (lista_temperaturas[dia][1] < minTemp):
        minTemp = lista_temperaturas[dia][1] 
# Defino listas con todas las temperaturas maximas y minimas
maximas = [max[1] for max in lista_temperaturas]
minimas = [min[0] for min in lista_temperaturas]
# Calculo el promedio de las temperaturas y lo guardo en su variable
promedioMax = mean(maximas)
promedioMin = mean(minimas)
# Recorro la lista de temperaturas usando su indice para saber que dia es e imprimir su temperatura minima y maxima
for i, fila in enumerate(lista_temperaturas):
    print(f"Dia: {semana[i]}, minima: {fila[0]}, maxima: {fila[1]} ")
print(f"El promedio de temperaturas maximas es: {round(promedioMax,2)} grados")
print(f"El promedio de temperaturas minimas es: {round(promedioMin,2)} grados")
print(f"El dia con mayor amplitud termica fue el {diaMayorAmplitud} con {mayorAmplitud} puntos")


# Ejercicio 8
# Utilizo el paquete statistics de python para utilizar funciones
from statistics import mean
# Importo modulo random para utilizar metodo randint()
import random
# Inicializo listas con los nombres de los alumnos y con las materias
alumnos = ["Juan", "Pedro", "Cristian", "Maria", "Jorge"]
materias = ["Programacion", "Matematica", "Sistemas Operativos"]
# Inicializo lista que va a contener las notas
notas = []
# Recorro la cantidad de estudiantes que hay y le cargo notas a la lista
for alumno in range(len(alumnos)):
    notas.append([random.randint(1,10),random.randint(1,10),random.randint(1,10)])
# Calculo el promedio de cada nota para cada materia
promedioMaterias = [mean([nota[materia] for nota in notas]) for materia in range(len(materias))]
# Muestro en pantalla a los alumnos con sus notas y sus promedios
print(f"####################")
print(f"#  CALIFICACIONES  #")
print(f"####################\n")
for alumno, nota in enumerate(notas):
    promedioAlumno = mean(notas[alumno])
    print(f" Alumno: {alumnos[alumno]} \n Notas: {notas[alumno]} \n Promedio: {round(promedioAlumno,2)}\n")
# Muestro en pantalla el promedio de notas de cada materia
print(f"##############################################")
print(f"# Promedio de calificaciones de cada materia #")
print(f"##############################################")
for materia in range(len(materias)):
    print(f"           {materias[materia]}: {promedioMaterias[materia]}")
print(f"##############################################")


# Ejercicio 9
# Defino metodo para mostrar matriz tateti
def MostrarMatriz(matriz):
    print("\n   0    1    2")
    for i,fila in enumerate(matriz):
        print(f"{i}{fila}")
# Defino metodo para agregar simbolo a la matriz
def AddSimbolo(fila,columna,simbolo):
    fila = int(input(f"\nIngrese la fila a ubicar el simbolo '{simbolo}': "))
    columna = int(input(f"Ingrese la columna a ubicar el simbolo '{simbolo}': "))
    tateti[fila][columna] = simbolo
# Inicializo el tateti con el formato
tateti=[["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]]
# Inicializo variable de turno
turno = 1
print("Bienvenidos al juego del TA-TE-TI")
# Guardo la accion en variable para consultar si se quiere Jugar o no
accion = int(input("1. Jugar\n2. Salir\n Respuesta: "))
if (accion == 1):
        MostrarMatriz(tateti)
        # Recorro la matrix 3x3 agregando los simbolos que ingresan los jugadores
        for fila in range(len(tateti)):
            for columna in range(len(tateti[fila])):
                print(f"\n# Turno del jugador {turno} #")
                if (turno == 1):
                    AddSimbolo(fila,columna,simbolo="X")
                    MostrarMatriz(tateti)
                    turno += 1
                else:
                    AddSimbolo(fila,columna,simbolo="O")
                    MostrarMatriz(tateti)
                    turno -= 1


# Ejercicio 10
# Importo modulo random para utilizar metodo randint()
import random
# Inicializo listas de productos y dias de la semana
productos = ["Gabinete", "Placa de video", "Procesador", "Placa madre"]
semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
# Inicializo variables a utilizar
diaMayorVentas = ""
itemMasVendido = ""
productosVendidos = []
cantItemMasVendido = 0
cantVendidaDia = 0
cantVendidaDiaMax = 0
# Inicializo un diccionario para acumular las ventas por producto
acumuladoProductos = {producto: 0 for producto in productos}
for dia in semana:
    # Inicializo lista con ventas
    ventas_dia = []
    # Recorro los items de la lista disponible y agrego cantidad de ventas
    for item in productos:
        ventas_dia.append([item,str(random.randint(1,10))])
    # Guardo una lista de cada dia con sus productos y ventas
    productosVendidos.append([dia, ventas_dia])
ventasPorItem = []
## Recorro la lista de productos vendidos para mostrar cuanto se vendio de cada item en el dia indicado
# Muestro el dia iterado en pantalla
for dia, ventas in productosVendidos:
    print(f"\nVentas {dia}:")
    # Muestro la iteracion de cada producto con sus ventas en el dia indicado
    for producto, cantidad in ventas:
        print(f"  {producto} → {cantidad}")
        # Sumo la cantidad vendida en el dia y lo guardo en su variable
        cantVendidaDia += int(cantidad)
        acumuladoProductos[producto] += int(cantidad)
    print(f"Total = {cantVendidaDia}")
    # Si las ventas del dia superan a las ventas maximas tomo ese valor como nuevo maximo
    if cantVendidaDia > cantVendidaDiaMax:
        cantVendidaDiaMax = cantVendidaDia
        # Guardo el dia donde se realizaron mas ventas
        diaMayorVentas = dia
    # Reinicio las ventas del dia para volver a calcularlas
    cantVendidaDia = 0
itemMasVendido = max(acumuladoProductos, key=acumuladoProductos.get)
cantItemMasVendido = acumuladoProductos[itemMasVendido]
print("\n######################################################################")
print(f"  El dia mas productivo fue el {diaMayorVentas} con {cantVendidaDiaMax} ventas")
print(f"  El producto más vendido de la semana fue {itemMasVendido} con {cantItemMasVendido} ventas")
print("######################################################################")
