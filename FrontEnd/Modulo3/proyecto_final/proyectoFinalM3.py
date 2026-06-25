#Primero se crea el diccionario vacio para guardar los videojuegos junto con la opcion para crear el login
videojuegos = {}
opcion = 0

login = """
===== TIENDA DE VIDEOJUEGOS =====
1. Agregar videojuego
2. Mostrar inventario
3. Buscar videojuego por código
4. Actualizar precio
5. Registrar venta
6. Mostrar estadísticas
7. Eliminar videojuego
8. Salir
"""
#Se agrega la funcion que permite agregar videojuegos donde se piden datos como codigo(evitando que se repita con otro existente), nombre, plataforma, 
#Precio y cantidad validando que estas dos ultimas sean mayores que 0
def agregar_videojuego (videojuegos):
    codigo_videojuego = input("Escriba el codigo del videojuego(empezando por VG001): ")
    if codigo_videojuego in videojuegos:
        print("El codigo ya existe")
        print(menu)
    else:
        videojuegos[codigo_videojuego] = {}
        nombre_videojuego = input("Escriba el nombre del videojuego: ")
        videojuegos[codigo_videojuego]["nombre"] = nombre_videojuego
        plataforma_videojuego = input("Escriba la plataforma del videojuego: ")
        videojuegos[codigo_videojuego]["plataforma"] = plataforma_videojuego
        while True:
            precio_videojuego = float(input(("Escriba el valor del videojuego: ")))
            if precio_videojuego <= 0:
                print("El valor es invalido, digitelo nuevamente")
            else:
                videojuegos[codigo_videojuego]["precio"] = precio_videojuego
                break
        while True:
            cantidad_videojuego = int(input(("Escriba la cantidad: ")))
            if cantidad_videojuego <= 0:
                print("El dato es invalido, digitelo nuevamente")
            else:
                videojuegos[codigo_videojuego]["cantidad"] = cantidad_videojuego
                break
        
#Funcion para mostrar el inventario actual donde incluye los videojuegos registrados y valida si el diccionario esta vacio
def mostrar_inventario(videojuegos):
    if len(videojuegos) == 0:
        print("No hay videojuegos registrados")
    else:
        print("="*100)
        print("Videojuegos")
        for videojuego, detalles in videojuegos.items():
            print(f"{videojuego, detalles}")

#Funcion para buscar videojuego por codigo donde pide el codigo y valida si existe o si lo encuentra imprima la informacion de dicho juego
def buscar_videojuego(videojuegos):
    codigo_buscar = input("Ingrese el codigo del videojuego: ")
    if codigo_buscar in videojuegos:
        print(f"{codigo_buscar}: {videojuegos[codigo_buscar]}")
    else:
        print("El videojuego no existe")

#Funcion para actualizar el precio del juego validando si existe el codigo y ajustando el precio al juego ya existe
def actualizar_precio(videojuegos):
    codigo_cambio_precio = input("Ingrese el codigo del videojuego: ")
    if codigo_cambio_precio in videojuegos:
        cambio_precio = float(input("Ingrese el valor a cambiar: "))
        videojuegos[codigo_cambio_precio]["precio"] = f"${cambio_precio:.0f}"
        print(f"Se actualizo el precio a ${cambio_precio:.0f}")
        print(f"{videojuegos[codigo_cambio_precio]["nombre"]}: {videojuegos[codigo_cambio_precio]["precio"]}")
    else:
        print("No existe el videojuego")

#Funcion para registrar una venta donde se pide codigo y cantidad a vender y creando una factura con los datos del juego vendido
def registrar_venta(videojuegos):
    codigo_videojuego_venta = input("Ingrese el codigo del videojuego a vender: ")    
    cantidad_vendida = int(input("Ingrese las cantidades a vender: "))
    if codigo_videojuego_venta in videojuegos:
        if cantidad_vendida <= videojuegos[codigo_videojuego_venta]["cantidad"]:  
            precio_unitario = videojuegos[codigo_videojuego_venta]["precio"]
            total_cantidad = cantidad_vendida * precio_unitario
            print("-"*50)
            print("     FACTURA DE VENTA VIDEOJUEGO")
            print("-"*50)
            print(f"Juego: {videojuegos[codigo_videojuego_venta]["nombre"]}")            
            print(f"Precio Unitario: ${precio_unitario:.0f}")
            print(f"Unidades: {cantidad_vendida}")
            print(f"Total: ${total_cantidad:.0f}")
            print(f"\n¡Gracias por tu compra, que tengas feliz dia!")
            print("-"*50)
            videojuegos[codigo_videojuego_venta]["cantidad"] -= cantidad_vendida
            print(f"Quedan un total de {videojuegos[codigo_videojuego_venta]["cantidad"]} unidades para el videjuego {videojuegos[codigo_videojuego_venta]["nombre"]}")
        else:
            print("No hay suficientes unidades")
    else:
        print("El codigo del videojuego no existe")

#Funcion para mostrar estadisticas cumpliendo con los parametros
def mostrar_estadisticas(videojuegos):
    #Total videojuegos registrados
    total_videojuegos = len(videojuegos)
    valor_total = 0
    suma_precios = 0

    mas_costoso = None
    mayor_stock = None
    
    for datos in videojuegos.values():
        #Valor Total del Inventario
        valor_total += datos["precio"] * datos["cantidad"]
        #Videojuego mas costoso
        if mas_costoso is None or datos["precio"] > mas_costoso["precio"]:
            mas_costoso = {"nombre": datos["nombre"], "precio": datos["precio"]}
        #Encontrar el de mayor cantidad
        if mayor_stock is None or datos["cantidad"] > mayor_stock["cantidad"]:
            mayor_stock = {"nombre": datos["nombre"], "cantidad": datos["cantidad"]}
        #promedio de precios
        suma_precios += datos["precio"]
        promedio_precios = suma_precios / total_videojuegos
    
    #Estadistica final
    print("-"*50)
    print("     ESTADISTICAS\n")
    print(f"El total de videojuegos registrados: {total_videojuegos}")
    print(f"El valor total del inventario: ${valor_total:.0f}")
    print(f"El videojuego mas costoso: {mas_costoso['nombre']} - Precio: ${mas_costoso['precio']:.0f}")
    print(f"El videojuego con mas cantidad: {mayor_stock['nombre']} - Cantidad: {mayor_stock['cantidad']}")
    print(f"El promedio de precios entre los videojuegos es: ${promedio_precios:.0f}")

#Funcion para eliminar videojuego donde se pide el codigo y se borra el diccionario anidado
def eliminar_videojuego(videojuegos):
    codigo_videojuego_eliminar = input("Ingrese el codigo del videojuego que desea eliminar: ")
    if codigo_videojuego_eliminar in videojuegos:
        nombre_videojuego_eliminar = videojuegos[codigo_videojuego_eliminar]["nombre"]
        del videojuegos[codigo_videojuego_eliminar]
        print(f"El videojuego {nombre_videojuego_eliminar} fue eliminado con exito")
    else:
        print("El videojuego no existe")

#Funcion para ejecutar el menu y permitir ejecutar cada funcion conforme a las opciones proporcionadas por el usuario
def menu():
    while True:
        print(login)
        opcion = int(input("Ingrese la opción: "))
        if opcion == 1:
            agregar_videojuego(videojuegos)
            print("¡Se agrego exitosamente el juego!")         
        elif opcion == 2:
            mostrar_inventario(videojuegos)
        elif opcion == 3:
            buscar_videojuego(videojuegos)
        elif opcion == 4:
            actualizar_precio(videojuegos)
        elif opcion == 5:
            registrar_venta(videojuegos)
        elif opcion == 6:
            mostrar_estadisticas(videojuegos)
        elif opcion == 7:
            eliminar_videojuego(videojuegos)
        elif opcion == 8:
            print("Cerrando el menu, Feliz dia")
            break
        else:
            print("Opcion invalida, intente nuevamente")

#Ejecucion de la funcion menu.
menu()

#Fin del codigo


