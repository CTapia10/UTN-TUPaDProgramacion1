## Trabajo practico 5 - Funciones 
## Cristian Tapia - 2025

# Ejercicio 1
# Defino funcion para imprimir hola mundo
def imprimir_hola_mundo():
    print("Hola Mundo")


# Ejercicio 2
# Defino funcion para saludar al usuario
def saludar_usuario(nombre):
    print(f"Hola {nombre}, bienvenido/a!")  


# Ejercicio 3
# Defino funcion para solicitar la informacion personal del usuario
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")  
    

# Ejercicio 4
# Defino funciones para calcular area de un circulo y calcular perimetro del circulo segun el radio ingresado 
def mostrar_area_y_perimetro_circulo(radio):
    import math
    # Obtengo el valor de PI
    pi = math.pi
    radioIngresado = radio
    # Defino funcion para calcular area del circulo
    def calcular_area_circulo():
        area = round((pi * radioIngresado ** 2),2)
        print(f"El area del circulo segun el radio ingresado es: {area}")
    # Defino funcion para calcular el perimetro del circulo
    def calcular_perimetro_circulo():
        perimetro = round((2 * pi * radioIngresado),2)
        print(f"El perimetro del circulo segun el radio ingresado es: {perimetro}")
    # LLamo a las funciones para imprimir los resultados
    calcular_area_circulo()
    calcular_perimetro_circulo()
    

# Ejercicio 5
# Defino funcion segundos a horas
def segundos_a_horas(segundos):
        horas = round((segundos / 3600),2)
        print(f"La cantidad de horas para los segundos ingresados es: {horas}")
        

# Ejercicio 6
# Defino funcion que imprime toda la tabla de multiplicar del numero ingresado
def tabla_multiplicar(numero):
    for i in range(1,11):
        multiplicacion = (i * numero)
        print(f"{i} * {numero} = {multiplicacion} ")


# Ejercicio 7
# Defino funcion que va a realizar las operaciones basicas
def operaciones_basicas(a,b):
    # Realizo las operaciones y las guardo en sus respectivas variables
    suma = (a + b)
    resta = (a - b)
    multiplicacion = (a * b)
    division = round((a / b),2)
    
    # Tupla para guardar resultados para cada operacion
    operacion_y_total = (("Suma", suma), ("Resta", resta), ("Multiplicacion", multiplicacion), ("Division", division))
    # Recorro la tupla por operacion y resultado
    for operacion, resultado in operacion_y_total:
        print(f"El resultado de la operacion {operacion} es {resultado}")


# Ejercicio 8 
# Defino funcion para calcular el imc del usuario
def calcular_imc(peso, altura):
    imc = round(peso / (altura ** 2),2)
    print(f"Su indice de masa corporal es: {imc}")


# Ejercicio 9
# Defino funcion para pasar la temperatura recibida en grados celcius a fahrenheit
def celsius_a_fahrenheit(celsius):
    fahrenheit = round(((celsius * 9/5) + 32),2)
    print(f"La temperatura en Fahrenheit equivalente a {celsius}°C es: {fahrenheit}°F")


# Ejercicio 10
def calcular_promedio(a,b,c):
    promedio = round(((a+b+c)/3),2)
    print(f"El promedio de los numeros ingresados es de: {promedio}")

##############################################################################
## TODO: Documentar bien todo, hacer mas robusto el codigo con validaciones ##
##############################################################################

# Defino el programa principal #
def programa_principal():
    # Llamo a la funcion que imprime hola mundo
     imprimir_hola_mundo()    
    # saludar_usuario(input("Ingrese su nombre: "))
    # informacion_personal(input("Ingrese su nombre: "),input("Ingrese su apellido: "),input("Ingrese su edad: "),input("Ingrese su residencia: "))
    # mostrar_area_y_perimetro_circulo(float(input("Ingrese el radio para calcular area y perimetro de un circulo: ")))
    # segundos_a_horas(int(input("Ingrese la cantidad de segundos para transformar a horas: ")))
    # tabla_multiplicar(int(input(f"Ingrese un numero entero para mostrar su tabla de multiplicar del 1 al 10: ")))
    # operaciones_basicas(int(input("Ingrese el primer numero para realizar operaciones basicas: ")),int(input("Ingrese el segundo numero: ")))
    # calcular_imc(int(input("Ingrese su peso en KG: ")),float(input("Ingrese su altura en metros: ")))
    # celsius_a_fahrenheit(float(input("Ingrese la temperatura en grados Celsius que desea convertir a Fahrenheit: ")))
    # calcular_promedio(int(input("Ingrese el primer numero: ")),int(input("Ingrese el segundo numero: ")),int(input("Ingrese el tercer numero: ")))
# Ejecuto el programa principal #
programa_principal()