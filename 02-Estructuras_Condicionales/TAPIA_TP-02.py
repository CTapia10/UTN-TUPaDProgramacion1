## Trabajo practico 2 - Condicionales 
#  Cristian Tapia - 2025

# Ejercicio 1

# Solicito edad del usuario
edad = int(input("Ingrese su edad: "))
# Verifico si es mayor de edad
if(edad >= 18):
    print("Es mayor de edad")


# Ejercicio 2

# Solicito la nota del usuario
nota = int(input("Ingrese su nota: "))
# Verifico si la nota es mayor o igual a 6
if(nota >= 6):
    print("Aprobado")
else:
    print("Desaprobado")


# Ejercicio 3

# Solicito un numero al usuario
num = int(input("Ingrese un numero: "))
# Verifico si el numero es par o no
while((num % 2) != 0):
    num = int(input("Por favor, ingrese un numero par: "))
else:
    print("Es par")


# Ejercicio 4

# Solicito edad del usuario
edad = int(input("Ingrese su edad: "))
# Defino la categoria del usuario dependiendo su edad
if(edad >= 0 and edad < 12):
    print("Usted es Niño/a")
elif(edad >= 12 and edad < 18):
    print("Usted es Adolescente")
elif(edad >= 18 and edad < 30):
    print("Usted es Adulto/a joven")
elif(edad >= 30):
    print("Usted es Adulto/a")
else:
    print("Ingrese una edad correcta")


# Ejercicio 5

# Solicito la password del usuario
password = input("Ingrese su password: ")
passwordLargo = len(password)
# Condicion para saber si la password es correcta
if(passwordLargo >= 8 and passwordLargo <= 14):
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# Ejercicio 6

# Utilizo el paquete statistics de python para utilizar funciones
from statistics import mode, median, mean
# Importo funcion random para insertar numeros aleatorios en la lista
import random
# Defino lista de 100 numeros aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# 
moda = mode(numeros_aleatorios)
print(f"El resultado de la moda es: {moda}")
mediana = median(numeros_aleatorios)
print(f"El resultado de la mediana es: {mediana}")
media = mean(numeros_aleatorios)
print(f"El resultado de la media es: {media}")

# Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.
if (media > mediana > moda):
    print("Segun el calculo, el resultado es: Sesgo positivo")
# Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda
elif(media < mediana < moda):
    print("Segun el calculo, el resultado es: Sesgo negativo")
# Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Pongo Else porque si comparo con el operador de igualdad no va a mostrar resultado (media == mediana == moda)
else:
    print("Sin sesgo")


# Ejercicio 7

# Solicito una frase o palabra al usuario
frase = input("Ingrese una frase o palabra: ")
fraseLargo = len(frase)
charFinal = frase[fraseLargo-1:]
vocales = "aeiouAEIOU"
# Condicion para saber si el string ingresado termina con vocal
if(charFinal in (vocales) ):
    print(f"{frase}!")
else:
    print(frase)


# Ejercicio 8

# Solicito un numero al usuario
nombre = input("Ingrese su nombre:")
num = int(input("Elija una opcion \n \
                1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO \n \
                2. Si quiere su nombre en minúsculas. Por ejemplo: pedro \n \
                3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. \n \
                "))
# Funcionalidad diferente dependiendo el numero ingresado
if (num == 1):
    print(f"Su nombre es {nombre.upper()}")
elif (num == 2):
    print(f"Su nombre es {nombre.lower()}")
elif (num == 3):
    # Para poner en mayuscula cada letra inicial de varias palabras
    print(f"Su nombre es {nombre.title()}")
    # Para poner solo la primer letra en mayuscula
    #print(f"Su nombre es {nombre.capitalize()}")
else:
    print("Elija una opcion valida")


# Ejercicio 9

# Solicito la magnitud de un terremoto al usuario
magnitud = float(input("Ingrese la magnitud del terremoto: "))
# Muestro categoria segun la escala de Richter
if(magnitud < 3):
    print("Muy leve (imperceptible).")
elif(3 <= magnitud < 4):
    print("Leve (ligeramente perceptible).")
elif(4 <= magnitud < 5):
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif(5 <= magnitud < 6 ):
    print("Fuerte (puede causar daños en estructuras débiles).")
elif(6 <= magnitud < 7):
    print("Muy Fuerte (puede causar daños significativos).")
elif(7 <= magnitud):
    print("Extremo (puede causar graves daños a gran escala).")


# Ejercicio 10
# Importo clase date
from datetime import date
# Solicito al usuario el hemisferio en el que se encuentra (S/N)
hemisferio = input("Ingrese la letra del hemisferio en donde se encuentra actualmente (N/S): ").upper()
# Tambien solicito el dia y el mes actual
dia = int(input("Ingrese el dia actual: "))
mes = int(input("Ingrese el numero correspondiente al mes actual: "))
anio = date.today().year
# Defino y asigno a la variable fecha que hay que comprobar
fecha_a_comprobar = date(anio, mes, dia)
# Defino los periodos a verificar
periodo1 = date(anio-1, 12, 21) <= fecha_a_comprobar <= date(anio, 3, 20)
periodo2 = date(anio, 3, 21) <= fecha_a_comprobar <= date(anio, 6, 20)
periodo3 = date(anio, 6, 21) <= fecha_a_comprobar <= date(anio, 9, 20)
periodo4 = date(anio, 9, 21) <= fecha_a_comprobar <= date(anio, 12, 20)
# Defino variable para saber si es hemisferio norte o sur
esNorte = False
esSur = False
# Asigno a variables el valor dependiendo el hemisferio
if (hemisferio == "N"):
    esNorte = True
elif (hemisferio == "S"):
    esSur = True

# Si esta en el hemisferio norte:
if (esNorte):
    if(periodo1):
        print(f"A la fecha {fecha_a_comprobar}, usted se encuentra en Invierno")
    elif(periodo2):
        print(f"A la fecha {fecha_a_comprobar}, usted se encuentra en Primavera")
    elif(periodo3):
        print(f"A la fecha {fecha_a_comprobar}, usted se encuentra en Verano")
    elif(periodo4):
        print(f"A la fecha {fecha_a_comprobar}, usted se encuentra en Otoño")
# Si esta en el hemisferio sur
elif(esSur):
    if(periodo1):
        print(f"A la fecha {fecha_a_comprobar}, usted se encuentra en Verano")
    elif(periodo2):
        print(f"A la fecha {fecha_a_comprobar}, usted se encuentra en Otoño")
    elif(periodo3):
        print(f"A la fecha {fecha_a_comprobar}, usted se encuentra en Invierno")
    elif(periodo4):
        print(f"A la fecha {fecha_a_comprobar}, usted se encuentra en Primavera")
else:
    print("Ingrese bien los datos")













