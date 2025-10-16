# Trabajo practico 7 - Manejo de Archivos
# Cristian Tapia - 2025
#=============================================================================#
#======================== Defino el programa principal =======================#
#=============================================================================#

def programa_principal():
    # Importo modulo pathlib para usar metodo Path y verificar si existe el archivo
    from pathlib import Path
    # Guardo el nombre del archivo en constante para reutilizarlo
    NOMBRE_ARCHIVO = "07-Manejo_Archivos/productos.txt"
    # Guardo el directorio del archivo
    directorio_archivo = Path(NOMBRE_ARCHIVO)
    
    # Defino metodo para verificar si existe el archivo
    def ExisteArchivo(archivo):
        if archivo.is_file():
            return True
        else:
            return False
    
    # Defino metodo para pedir precio y devolverlo sin tener errores de entrada
    def PedirPrecio():
        while True:
            precio = input("Ingrese el precio del producto: ").strip()
            import re
            # Expresion regular para validar si la cadena es numero decimal positivo
            chars_permitidos = re.compile(r"^\d+(\.\d+)?$")
            precio_formato = precio.replace(",", ".")
            if chars_permitidos.match(precio_formato): 
                precio_final = float(precio_formato)
            else:
                print("\n ⚠️  Ingrese un precio valido (numero entero mayor a 0).")
                continue
            break
        if precio_final.is_integer():
            return int(precio_final)
        return precio_final
    
    # Defino metodo para pedir el nombre del producto al usuario
    def PedirNombre():
        while True:
            nombre = input("\nIngrese el nombre del producto: ").strip()
            if not nombre.isalpha():
                print(f"\n⚠️  El nombre no debe estar vacio y debe estar formado por letras.")
                continue
            if len(nombre) < 2:
                print(f"\n⚠️  El nombre es demasiado corto.")
                continue
            return nombre

    # Defino metodo para pedir la cantidad y devolverla sin errores de entrada
    def PedirCantidad():
        while True:
            cantidad = input("Ingrese las unidades que desea agregar: ").strip()
            if not cantidad.isdigit():
                print("\n ⚠️  Ingrese una cantidad valida (numero entero mayor a 0).")
                continue
            # Despues de verificar que no hayan signos especiales transformo a entero
            cantidad = int(cantidad)
            if cantidad <= 0:
                print("\n ⚠️  Ingrese una cantidad valida (numero entero mayor a 0).\n")
                continue
            break
        return cantidad

    # Defino metodo para mostrar productos del archivo
    def MostrarProductos():
        # Defino lista con lineas que se van a formatear una vez leidas las del txt
        lineas_formateadas = []
        # Leo archivo productos.txt anteriormente creado
        if ExisteArchivo(directorio_archivo):
            with open(NOMBRE_ARCHIVO, "r") as productos:
                lineas = productos.readlines()
                for linea in lineas:
                    lineas_formateadas.append(linea.strip().split(","))
            print("="*54)
            for nombre,precio,cantidad in lineas_formateadas:
                print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
            print("="*54)
        else:
            print(f"Error: El archivo '{directorio_archivo}' no existe.")

    # Defino metodo para agregar productos al txt sin sobreescribir
    def AgregarProducto(nombre,precio,cantidad):
            with open(NOMBRE_ARCHIVO, "a") as productos:
                productos.write(f"\n{nombre},{precio},{cantidad}")
#===============================================================================#
# Solucion de cada ejercicio, descomentar la que se quiere probar (CTRL+K+U)    #
#===============================================================================#
    
    #============================  Ejercicio 1 =================================#
    # Defino lista lineas con las lineas con productos que va a contener el txt
    # lineas = ["Remera,1500,15\n",
    #         "Pantalon,2000,15\n",
    #         "Campera,2500,20"]
    # # Creo archivo txt con productos
    # with open("07-Manejo_Archivos/productos.txt", "w") as productos_w:
    #     productos_w.writelines(lineas)
    
    #============================  Ejercicio 2 =================================#
    # Muestro productos con el formato adecuado
    # MostrarProductos()
    
    #============================  Ejercicio 3 =================================#
    # Muestro productos con el formato adecuado
    MostrarProductos()
    # Agrego productos
    AgregarProducto(PedirNombre(),PedirPrecio(),PedirCantidad())
    
    #============================  Ejercicio 4 =================================#
    
    
    #============================  Ejercicio 5 =================================#
    
    
    #============================  Ejercicio 6 =================================#
    
    
#===============================================================================#
#======================== Ejecuto el programa principal ========================#
#===============================================================================#
programa_principal()
#===============================================================================#