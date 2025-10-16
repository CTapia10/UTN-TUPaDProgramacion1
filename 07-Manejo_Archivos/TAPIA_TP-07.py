# Trabajo practico 7 - Manejo de Archivos
# Cristian Tapia - 2025
#=============================================================================#
#======================== Defino el programa principal =======================#
#=============================================================================#

def programa_principal():
    def NombreArchivo():
        # Guardo el nombre del archivo en variable para reutilizarlo o cambiarlo en todas las coincidencias
        nombre_archivo = "productos.txt"
        return nombre_archivo
    
    def DirArchivo():
        # Importo modulo pathlib para usar metodo Path y verificar si existe el archivo
        from pathlib import Path
        # Guardo el directorio del archivo
        directorio_archivo = Path('./07-Manejo_Archivos/'+NombreArchivo())
        return directorio_archivo
    
    # Defino metodo para verificar si existe el archivo
    def ExisteArchivo(archivo):
        return archivo.is_file()
    
    # Defino metodo para pedir precio y devolverlo sin tener errores de entrada
    def PedirPrecio():
        while True:
            precio = input("\nIngrese el precio del producto: ").strip()
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
            nombre = input("\nIngrese el nombre del producto: ").strip().capitalize()
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
            cantidad = input("\nIngrese las unidades que desea agregar: ").strip()
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
    def MostrarProductosLista(archivo):
        if ExisteArchivo(archivo):
            print("="*54)
            for nombre,precio,cantidad in ProductosListaFormato(archivo):
                print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
            print("="*54)
        else:
            print(f"\nError: El archivo '{archivo}' no existe .")

    # Defino metodo para agregar productos al txt sin sobreescribir
    def AgregarProducto(archivo,nombre,precio,cantidad):
            with open(archivo, "a") as productos:
                productos.write(f"\n{nombre},{precio},{cantidad}")
                
    def ProductosListaFormato(archivo):
        # Defino lista con lineas que se van a formatear una vez leidas las del txt
        lineas_formateadas = []
        # Leo archivo productos.txt anteriormente creado
        with open(archivo, "r") as productos:
            lineas = productos.readlines()
            for linea in lineas:
                lineas_formateadas.append(linea.strip().split(","))
            return lineas_formateadas

    def ListaProductosDict(archivo):
        # Lista con diccionario de productos
        lista_productos = []
        for nombre,precio,cantidad in ProductosListaFormato(archivo):
            lista_productos.append({"Producto": nombre ,"Precio" : precio , "Cantidad": cantidad})
        return lista_productos

    def MostrarTablaProductos(archivo):
        if ExisteArchivo(archivo):
            print("\n"+"="*54)
            print(" "*18+"Tabla de productos"+" "*18)
            print("="*54)
            for producto in ListaProductosDict(archivo):
                for clave, valor in producto.items():
                    print(f"{clave}: {valor}")
                print("="*54)
        else:
            print(f"\nError: El archivo '{archivo}' no existe .")
            
    
    # Defino metodo para consultar por un producto en especifico y lo muestro en pantalla
    def MostrarProductoConsulta(archivo, nombre):
        encontrado = False
        for producto in ListaProductosDict(archivo):
            if producto.get("Producto") == nombre:
                encontrado = True
                print("="*54)
                for clave, valor in producto.items():
                    print(f"{clave}: {valor}")
                print("="*54)
                break
        if not encontrado:
            print("\n ⚠️  El producto ingresado no se encuentra dentro del catalogo.\n")
    
#===================================================================================#
#     Solucion de cada ejercicio, descomentar la que se quiere probar (CTRL+K+U)    #
#===================================================================================#
    
    #============================  Ejercicio 1 =================================#
    def CrearTXT():
        # Defino lista lineas con las lineas con productos que va a contener el txt
        lineas = ["Remera,1500,15\n",
                "Pantalon,2000,15\n",
                "Campera,2500,20"]
        # Creo archivo txt con productos
        with open(DirArchivo(), "w") as productos_w:
            productos_w.writelines(lineas)
    
    #============================  Ejercicio 2 =================================#
    # # Muestro productos con el formato adecuado
    # MostrarProductosLista(DirArchivo())
    
    #============================  Ejercicio 3 =================================#
    # # Muestro productos con el formato adecuado
    # MostrarTablaProductos(DirArchivo())
    # # Agrego productos
    # AgregarProducto(DirArchivo(),PedirNombre(),PedirPrecio(),PedirCantidad())
    
    #============================  Ejercicio 4 =================================#
    # MostrarTablaProductos(DirArchivo())

    #============================  Ejercicio 5 =================================#
    # MostrarTablaProductos(DirArchivo())
    # producto_consulta = PedirNombre()
    # MostrarProducto(DirArchivo(),producto_consulta)
    
    #============================  Ejercicio 6 =================================#
    # menu_principal = ["1. Crear o sobreescribir archivo con productos",
    #                 "2. Mostrar tabla de productos",
    #                 "3. Consultar por un producto",
    #                 "4. Agregar un producto",
    #                 "5. Salir"]
    # while True:
    #     # Mostramos las opciones del menu al usuario
    #     print("\n"+"="*54)
    #     print("Bienvenido al catálogo de productos, elija una opción")
    #     print("="*54)
    #     for opcion in menu_principal:
    #         print(opcion)
    #     print("="*54)
    #     # Pedimos al usuario que seleccione una de las opciones
    #     seleccion = input("Opción seleccionada: ").strip()
    #     print("="*54)
    #     match seleccion:
    #         case "1":
    #             CrearTXT()
    #         case "2":
    #             MostrarTablaProductos(DirArchivo())
    #         case "3":
    #             producto_consulta = PedirNombre()
    #             MostrarProductoConsulta(DirArchivo(),producto_consulta)
    #         case "4":
    #             AgregarProducto(DirArchivo(),PedirNombre(),PedirPrecio(),PedirCantidad())
    #         case "5":
    #             print("Saliendo del programa... ¡Hasta luego!\n")
    #             break
    #         # Opcion inválida
    #         case _:
    #             print("⚠️  Opción inválida. Por favor, elija una opción del 1 al 4.\n")
    #             continue            
    
#=========================================================================================#
#                              Ejecuto el programa principal                              #
#=========================================================================================#
programa_principal()
#=========================================================================================#