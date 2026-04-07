

"""
Mini proyecto: Sistema de gestión de productos
Objetivo

Crear un programa orientado a objetos que permita:

Crear productos
Mostrar productos
Buscar productos
Actualizar precio y stock
Vender productos
Eliminar productos
Conceptos que se trabajan
Clases y objetos
Constructor
Encapsulamiento
Getters y setters
Métodos
Listas de objetos

class Producto:
    def _init_(self, codigo, nombre, precio, stock):
        self.__codigo =codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_stock(self):
        return self.__stock
    
    def set_codigo(self, nuevo_codigo):
        self.__codigo = nuevo_codigo

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def set_precio(self, nuevo_precio):
        self.__precio = nuevo_precio

    def set_stock(self, nuevo_stock):
        self.__stock = nuevo_stock
    
    def mostrar_info(self):
        print(f"Código: {self.__codigo}")
        print(f"Nombre: {self.__nombre}")
        print(f"Precio: ${self.__precio}")
        print(f"Stock: {self.__stock} unidades")
        print("-" * 30)

    def vender(self, cantidad):
        if cantidad <= self.__stock:
            self.__stock -= cantidad
            print("Ahora quedan", self.__stock, "unidades en stock.")
            return True
        else:
            return False
        
class SistemaGestionProductos:
    def _init_(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print("Producto agregado exitosamente.")
    
    def mostrar_productos(self):
        print("Lista de productos:")
        print("-" * 30)
        for producto in self.productos:
            producto.mostrar_info()

    def buscar_producto(self, codigo):
        for producto in self.productos:
            if producto.get_codigo() == codigo:
                return producto
        return None
    
    def eliminar_producto(self, codigo):
        producto = self.buscar_producto(codigo)
        if producto:
            self.productos.remove(producto)
            print("Producto eliminado exitosamente.")
        else:
            print("Producto no encontrado.")

    def actualizar_precio(self, codigo, nuevo_precio):
        producto = self.buscar_producto(codigo)
        if producto:
            producto.set_precio(nuevo_precio)
            print("Precio actualizado exitosamente.")
        else:
            print("Producto no encontrado.")

    def actualizar_stock(self, codigo, nuevo_stock):
        producto = self.buscar_producto(codigo)
        if producto:
            producto.set_stock(nuevo_stock)
            print("Stock actualizado exitosamente.")
        else:
            print("Producto no encontrado.")

def menu():
    sistema = SistemaGestionProductos()
    while True:

            print("Sistema de Gestión de Productos")
            print("1. Agregar producto")
            print("2. Mostrar productos")
            print("3. Buscar producto")
            print("4. Actualizar precio")
            print("5. Actualizar stock")
            print("6. Vender producto")
            print("7. Eliminar producto")
            print("8. Salir")

            opcion = input("Seleccione una  opción: ")
            if opcion == "1":
                codigo = input("Ingrese el código del producto: ")
                nombre = input("Ingrese el nombre del producto: ")
                precio = float(input("Ingrese el precio del producto: "))
                stock = int(input("Ingrese el stock del producto: "))
                producto = Producto(codigo, nombre, precio, stock)
                sistema.agregar_producto(producto)  
            elif opcion == "2":
                sistema.mostrar_productos()
            elif opcion == "3":
                codigo = input("Ingrese el código del producto a buscar: ")
                producto = sistema.buscar_producto(codigo)
                if producto:
                    producto.mostrar_info()
                else:
                    print("Producto no encontrado.")
            elif opcion == "4":
                codigo = input("Ingrese el código del producto a actualizar: ")
                nuevo_precio = float(input("Ingrese el nuevo precio: "))
                sistema.actualizar_precio(codigo, nuevo_precio)
            elif opcion == "5":
                codigo = input("Ingrese el código del producto a actualizar: ")
                nuevo_stock = int(input("Ingrese el nuevo stock: "))
                sistema.actualizar_stock(codigo, nuevo_stock)
            elif opcion == "6":
                codigo = input("Ingrese el código del producto a vender: ")
                cantidad = int(input("Ingrese la cantidad a vender: "))
                producto = sistema.buscar_producto(codigo)
                if producto:
                    if producto.vender(cantidad):
                        print("Producto vendido exitosamente.")
                    else:
                        print("Stock insuficiente.")
                else:
                    print("Producto no encontrado.")
            elif opcion == "7":
                codigo = input("Ingrese el código del producto a eliminar: ")
                sistema.eliminar_producto(codigo)
            elif opcion == "8":
                print("Saliendo del sistema. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 8.")

if __name__ == "_main_":    menu()"""
       


"""class Libro:
    def __init__(self, titulo, autor, isbn, precio):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__precio = precio

    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor
    
    def get_isbn(self):
        return self.__isbn
    
    def get_precio(self):
        return self.__precio
    
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_titulo(self, autor):
        self.__autor = autor

    def set_titulo(self, isbn):
        self.__isbn = isbn

    def set_titulo(self, precio):
        if precio > 0:
            self.__precio = precio
        else:
            print("El precio debe ser mayor que 0")
    
    def mostrar_info(self):
        print("Título:", self.get_titulo())
        print("Autor:", self.get_autor())
        print("Título:", self.get_titulo())
        print("Título:", self.get_titulo())"""


"""class Perro:
    def __init__(self, nombre, raza, edad):
        self.__nombre = nombre
        self.__raza = raza
        self.__edad = edad

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_raza(self):
        return self.__raza

    def get_edad(self):
        return self.__edad

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_raza(self, raza):
        self.__raza = raza

    def set_edad(self, edad):
        if edad > 0:
            self.__edad = edad
        else:
            print("La edad debe ser mayor que 0")

    # Método para mostrar información
    def mostrar_info(self):
        print("Nombre:", self.get_nombre())
        print("Raza:", self.get_raza())
        print("Edad:", self.get_edad())
        print("------------------------")


# Clase principal
def main():
    perro1 = Perro("Max", "Labrador", 5)
    perro2 = Perro("Bella", "Golden Retriever", 3)
    perro3 = Perro("Rocky", "Bulldog", 4)

    perro1.mostrar_info()
    perro2.mostrar_info()
    perro3.mostrar_info()
   

    # Ejemplo de uso de setter
    perro1.set_edad(6)
    print("Nueva edad del perro 1:", perro1.get_edad())
    perro1.mostrar_info()

perro4 = Perro("Luna", "Poodle", 2)
perro4.mostrar_info()
main()"""