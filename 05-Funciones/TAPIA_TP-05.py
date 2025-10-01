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
def get_area_y_perimetro_circulo(radio):
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


# Defino el programa principal #
def programa_principal():
    # Llamo a la funcion que imprime hola mundo
    # imprimir_hola_mundo()    
    # saludar_usuario(input("Ingrese su nombre: "))
    # informacion_personal(input("Ingrese su nombre: "),input("Ingrese su apellido: "),input("Ingrese su edad: "),input("Ingrese su residencia: "))
    get_area_y_perimetro_circulo(float(input("Ingrese el radio para calcular area y perimetro de un circulo: ")))
# Ejecuto el programa principal #
programa_principal()