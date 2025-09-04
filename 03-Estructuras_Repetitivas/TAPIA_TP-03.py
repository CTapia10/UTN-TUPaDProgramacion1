# Trabajo practico 3 - Repetitivas 
# Cristian Tapia - 2025

# Ejercicio 1
# Utilizo un for para definir el rango de iteracion para imprimir del 1 al 100
for num in range(1,101):
    #print(str(num),end=" ") # Otra opcion pasando parametros para mostrar resultado en una linea separado por espacios
     print(str(num))


# Ejercicio 2
# Solicito un numero al usuario
num = input("Ingrese un numero: ")
largoNum = len(str(num))
chars=0
for char in num:
     if char not in[",","."]: # Iteracion para contar caracteres y excluir puntos o comas
        chars+=1
print(f"La cantidad de digitos que tiene su numero es: {chars}")
# Forma mas simple sin utilizar iteracion pero contempla signos como digitos:
#   print(f"La cantidad de digitos que tiene su numero es: {largoNum}")


# Ejercicio 3
# Solicito los numeros al usuario
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
suma = 0
for num in range(num1+1,num2): # Excluyo el valor inicial sumandole 1, el segundo valor se excluye solo en la funcion Range()
     suma = suma+num
print(f"La suma total de los numeros entre los dos valores ingresados es: {suma}")


# Ejercicio 4
# Defino el caracter que se utiliza para el corte del bucle
CORTE = 0
suma = 0
numIngresado = int(input("Ingrese un numero entero, en caso de querer frenar la secuencia ingrese un 0: "))
# Solicito los numeros al usuario
while (numIngresado != CORTE):
     # Sumo el numero ingresado de la secuencia
     suma = suma+numIngresado 
     numIngresado = int(input("Ingrese otro numero, en caso de querer frenar la secuencia ingrese un 0: "))
print(f"La suma total de la secuencia de numeros es: {suma}")


# Ejercicio 5
# Importo modulo random para utilizar metodo randint()
import random
# Defino el numero aleatorio que el usuario debe adivinar
numRandom = random.randint(1,10)
# Defino contador de intentos
intentos=0
numIngresado = int(input("Ingrese un numero entero: "))
while (numIngresado != numRandom):
    intentos+=1
    print("Incorrecto, segui intentando")
    numIngresado = int(input("Ingrese otro numero: "))
print(f"Correcto! Adivinaste el numero aleatorio en {intentos} intentos")


# Ejercicio 6
# Utilizo un for para definir el rango de iteracion para imprimir numeros pares del 100 al 0
for num in range(100, -1, -2):
    #print(str(num),end=" ") # Otra opcion pasando parametros para mostrar resultado en una linea separado por espacios
    print(str(num))


# Ejercicio 7
suma = 0
hastaNum = int(input("Ingrese un numero entero positivo para sumar los numeros del medio entre 0 y el indicado: "))
# Solicito los numeros al usuario
for num in range(0,hastaNum+1):
     # Sumo el numero ingresado de la secuencia
     suma = suma+num 
print(f"La suma total de la secuencia de numeros es: {suma}")


# Ejercicio 8
# Defino variables para guardar la cantidad de numeros pares, impares, positivos y negativos
numPares=0
numImpares=0
positivos=0
negativos=0
# #Variable para delimitar el rango de numeros a ingresar
#hastaNum = int(input("Ingrese el hasta del rango para verificar que numeros son pares,impares,positivos y negativos: "))
hastaNum = 5
# Utilizo un for para definir el rango de iteracion
for num in range(1,hastaNum+1):
    numIngresado = int(input("Ingrese un numero: "))
    if (numIngresado >= 0):
        positivos+=1
        if ((numIngresado % 2) == 0):
            numPares+=1
        else:
            numImpares+=1
      
    elif ((numIngresado % 2) == 0):
        numPares+=1
        negativos+=1
    else:
        negativos+=1
        numImpares+=1
print(f"La cantidad de numeros pares es: {numPares}, la cantidad de impares es: {numImpares}, positivos: {positivos} y negativos: {negativos}")


# Ejercicio 9
# Utilizo el paquete statistics de python para utilizar funciones
from statistics import mean
# Inicializo lista que va a almacenar los numeros ingresados por el usuario
listaNumeros = []
# #Variable para delimitar el rango de numeros a ingresar
# hastaNum = int(input("Ingrese el hasta del rango para verificar la media de los numeros: "))
hastaNum = 10
print(f"Ingrese {hastaNum} numeros para calcular su media: ")
listaNumeros.append(int(input("Ingrese el primer numero: ")))
# Utilizo un for para definir el rango de iteracion
for num in range(1,hastaNum):
    listaNumeros.append(int(input("Ingrese el siguiente numero: ")))
media = mean(listaNumeros)
print(f"El resultado de la media es: {media}")


# Ejercicio 10
# Inicializo variable para guardar el numero invertido
numInvertido = ""
numIngresado=input("Ingrese un numero: ") 
largoNum = len(numIngresado)
# Logica para invertir numero
for i in range(largoNum,0,-1):
	numIteracion = numIngresado[i-1]
	numInvertido = numInvertido+numIteracion
print(f"El numero invertido es: {numInvertido}")