"""
# Relacion de asosiacion

class Cliente:
    def __init__(self,nombre):
        self.nombre = nombre

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente

c1 = Cliente("Pedro")

p1 = Pedido(c1)
"""
"""
#Relacion de Agregacion: Donde las partes pueden existir sin el todo (Ej: Se puede tener el restaurante sin empleados)

class Empleado:
    def __init__(self,nombre):
        self.nombre = nombre

class Restaurante:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

e = Empleado("Roberto")

r = Restaurante()

r.agregar_empleado(e)
"""        
"""
# Relacion de composición (relación fuerte)
class Plato:
    def _init_(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio

class Pedido:
    def _init_(self):
        self.platos = []

    def agregar_plato(self, nombre, precio):
        plato = Plato(nombre, precio)
        self.platos.append(plato)

#plato = Plato("Bandeja paisa",35000) Esto no se debe hacer porque el plato queda huerfano

pedido = Pedido()
pedido.agregar_plato("Sancocho",30000)
pedido.agregar_plato("Mojarra frita",40000)
"""

