## Trabajo practico 5 - Funciones 
## Cristian Tapia - 2025

# Ejercicio 1
# Defino funcion para imprimir hola mundo
def imprimir_hola_mundo():
    print("Hola Mundo")


# Ejercicio 2
# Defino funcion para saludar al usuario
def saludar_usuario(nombre_valido):
    print(f"Hola {nombre_valido}, bienvenido/a!")  


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
    # Defino funcion para calcular area del circulo
    def calcular_area_circulo():
        area = round((pi * radio ** 2),2)
        print(f"El area del circulo segun el radio ingresado es: {area}")
    # Defino funcion para calcular el perimetro del circulo
    def calcular_perimetro_circulo():
        perimetro = round((2 * pi * radio),2)
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
    division = round((a / b),2) if b != 0 else "No se puede dividir por cero"
    
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



#=============================================================================#
#======================== Defino el programa principal =======================#
#=============================================================================#
def programa_principal():
    
    # Funciones para validar datos en especifico
    def validar_edad(edad):
        if not (1 <= edad <= 100):
            return print(f"⚠️  Ingrese una edad entre 1 y 100.")
        else:
            return True
        
    def validar_peso(peso):
        if not (40 <= peso <= 120):
            return print(f"⚠️  Ingrese un peso entre 40 y 120.")
        else:
            return True
        
    def validar_altura(altura):
        if not (1.4 <= altura <= 2.5):
            return print(f"⚠️  Ingrese una altura entre 1.4Mts y 2.5Mts.")
        else:
            return True
    
    def msg_solicitar_datos():
        print("Ingrese correctamente los datos que se le solicitan a continuacion")
        
    def validar_string(id_string):
        while True:
            string = input(f"{id_string}: ").strip()
            if not string.isalpha():
                print(f"⚠️  El campo ingresado '{id_string}' no debe estar vacio y debe estar formado por letras.")
                continue
            if len(string) < 2:
                print(f"⚠️ El campo ingresado '{id_string}' es demasiado corto.")
                continue
            return string

    def validar_num(id_num):
        import re
        # Expresion regular para validar si la cadena es numero decimal positivo
        chars_permitidos = re.compile(r"^\d+(\.\d+)?$")
        # Expresion regular para validar si la cadena es numero decimal positivo o negativo
        
        while True:
            dato = input(f"{id_num}: ").strip()
            dato = dato.replace(",", ".")
            if id_num.lower() == "celcius": 
                chars_permitidos_y_neg = re.compile(r"^-?\d+(\.\d+)?$") 
                if chars_permitidos_y_neg.match(dato): 
                    dato_num = float(dato)
                    return dato_num
                else:
                    print(f"⚠️  Ingrese un número válido para el campo '{id_num}'.")
            elif chars_permitidos.match(dato): 
                dato_num = float(dato)
                match id_num.lower():
                    # Valido la edad
                    case "edad": 
                        if not validar_edad(dato_num):
                            continue
                    # Valido el peso
                    case "peso": 
                        if not validar_peso(dato_num):
                            continue
                    # Valido la altura
                    case "altura":  
                        if not validar_altura(dato_num):
                            continue
                # Si es entero exacto, devolver como int
                if dato_num.is_integer():
                    return int(dato_num)
                return dato_num
            else:
                print(f"⚠️  Ingrese un número válido para el campo '{id_num}'.")

    # Defino funcion para pedir el dato segun el nombre del dato y tipo de dato para realizar validaciones de entrada
    def pedir_dato(nombre_dato,tipo_dato):
        STRING = "STRING"
        NUMERO = "NUMERO"
        # Validaciones para verificar que el dato string ingresado es correcto
        if tipo_dato == STRING:
            return validar_string(nombre_dato)
        # Validaciones para verificar que el dato numero ingresado es correcto
        elif tipo_dato == NUMERO:
            return validar_num(nombre_dato)
        
#=============================================================================#
# Funciones de cada ejercicio, descomentar la que se quiere probar (CTRL+K+U) #
#=============================================================================#
    
    #==================== Funcion Ejercicio 1 =========================#
    # imprimir_hola_mundo()
    
    #==================== Funcion Ejercicio 2 =========================#
    # msg_solicitar_datos()
    # saludar_usuario(pedir_dato("nombre","STRING"))
    
    #==================== Funcion Ejercicio 3 =========================#
    # msg_solicitar_datos()
    # informacion_personal(pedir_dato("Nombre","STRING"),pedir_dato("Apellido","STRING"),pedir_dato("Edad","NUMERO"),pedir_dato("Residencia","STRING"))
    
    #==================== Funcion Ejercicio 4 =========================#
    # print("Ingrese a continuacion el radio del circulo para calcular su area y perimetro")
    # mostrar_area_y_perimetro_circulo(pedir_dato("Radio","NUMERO"))
    
    #==================== Funcion Ejercicio 5 =========================#
    # print("Ingrese a continuacion la cantidad de segundos para conocer su equivalente en horas ")
    # segundos_a_horas(pedir_dato("Segundos","NUMERO"))
    
    #==================== Funcion Ejercicio 6 =========================#
    # print("Ingrese un numero entero para mostrar su tabla de multiplicar del 1 al 10: ")
    # tabla_multiplicar(pedir_dato("Numero","NUMERO"))
    
    #==================== Funcion Ejercicio 7 =========================#
    # print("Ingrese dos numeros para realizar operaciones basicas: ")
    # operaciones_basicas(pedir_dato("Primer numero","NUMERO"), pedir_dato("Segundo numero","NUMERO"))
    
    #==================== Funcion Ejercicio 8 =========================#
    # print("Bienvenido a la calculadora de IMC")
    # print("Esta calculadora esta pensada para calcular peso y altura promedio de un adulto, no contempla")
    # print("Ingrese a continuacion su peso en KG y su altura en METROS ")
    # calcular_imc(pedir_dato("Peso","NUMERO"),pedir_dato("Altura","NUMERO"))
    
    #==================== Funcion Ejercicio 9 =========================#
    # print("Ingrese la temperatura en grados Celsius que desea convertir a Fahrenheit ")
    # celsius_a_fahrenheit(pedir_dato("Celcius","NUMERO"))
    
    #==================== Funcion Ejercicio 10 =========================#
    # print("Ingrese tres numeros para calcular su promedio: ")
    # calcular_promedio(pedir_dato("Primer numero","NUMERO"),pedir_dato("Segundo numero","NUMERO"),pedir_dato("Tercer numero","NUMERO"))
    
#=============================================================================#
#==================== Fin definicion de programa principal ===================#
#=============================================================================#


#=============================================================================#
#======================= Ejecuto el programa principal =======================#
#=============================================================================#
programa_principal()
#=============================================================================#
