#Primero se importa la libreria para utilizar el abstracmethod
from abc import ABC, abstractmethod

#Se crea la clase Padre 
class Persona(ABC):
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    @abstractmethod
    def mostrar_rol(self):
        pass

#Se crea la clase Veterinario, cliente y recepcionista que heredan de la clase padre

class Veterinario(Persona):
    def __init__(self, nombre, documento):
        super().__init__(nombre, documento)

    def mostrar_rol(self):
        return f"Veterinario: {self.nombre} "    

#En la clase cliente se asocia con Mascota    
class Cliente(Persona):
    def __init__(self, nombre, documento, telefono):
        super().__init__(nombre, documento)

        self.telefono = telefono
        self.mascotas = []

    def mostrar_rol(self):
        return f"Cliente: {self.nombre}"
        
    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)
    
    def mostrar_mascota(self):
        for mascota in self.mascotas:
            print(mascota.mostrar_info())
            
class Recepcionista(Persona):
    def mostrar_rol(self):
        return f"Recepcionista: {self.nombre}"
    
    def registrar_cliente(self, cliente):
        print(f"{cliente.mostrar_rol()}, Documento: {cliente.documento} Telefono: {cliente.telefono}")

# Se Crea la clase Mascota 
class Mascota:
    def __init__(self, nombre, especie, edad, peso):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

    def mostrar_info(self):
        return f"""
        Nombre: {self.nombre}
        Especie: {self.especie}
        Edad: {self.edad}
        Peso: {self.peso}
        """

#Se crea la clase Tratamiento     
class Tratamiento:
    def __init__(self, nombre, precio, duracion_dias):
        self.nombre = nombre
        self.precio = precio
        self.duracion_dias = duracion_dias
    
    def mostrar_tratamiento(self):
        return f"Tratamiento: {self.nombre}, tiene un precio de: ${self.precio:.0f} con duracion de: {self.duracion_dias} días"

#Se crea la clase consulta que su composicion viene de la clase tratamiento
class Consulta:
    def __init__(self, motivo, diagnostico, veterinario, mascota):
        self.motivo = motivo
        self.diagnostico = diagnostico
        self.veterinario = veterinario
        self.mascota = mascota
        self.tratamientos = []

    def crear_tratamientos(self, tratamiento):
        self.tratamientos.append(tratamiento)

    def mostrar_resumen(self):
            print(f"Se le asigno el {self.veterinario.mostrar_rol()}")
            print(f"El motivo de la consulta para la mascota: {self.mascota.nombre} es {self.motivo} se le diagnostico {self.diagnostico}")

    def mostrar_tratamiento(self):
        for tratamiento in self.tratamientos:
            print(f"{tratamiento.mostrar_tratamiento()}")

    def calcular_tratamiento(self):
        return sum(tratamiento.precio for tratamiento in self.tratamientos)
    
#Se crea la clase abstracta que la heredan los diferentes metodos de pago.
class Metodo_Pago(ABC):
    def __init__(self, monto):
        self.monto = monto
    
    @abstractmethod
    def procesar_pago(self, monto):
        pass

class PagoEfectivo(Metodo_Pago):
    def procesar_pago(self, monto):
        return f"Pago en efectivo por valor de: {monto}"

class PagoTarjeta(Metodo_Pago):
    def procesar_pago(self, monto):
        return f"Pago con Tarjeta por valor de: {monto}"
    
class PagoTransferencia(Metodo_Pago,):
    def procesar_pago(self, monto):
        return f"Pago por transferencia por valor de: {monto}"

#Se crea la clase factura que calcula el valor de los tratamientos calculados en la consulta.
class Factura:
    def __init__(self, consulta, impuestos=0.19):
        self.consulta = consulta
        self.impuestos = impuestos

    def calcular_total(self):
        subtotal = self.consulta.calcular_tratamiento()
        total = subtotal + (subtotal * self.impuestos)
        return f"${total:.0f}"
    
    def pagar(self, metodo_pago: Metodo_Pago):
        total = self.calcular_total()
        return metodo_pago.procesar_pago(total)

#Se ejecuta el main con todas las funciones creadas anteriormente
print("-"*60)
print("         ¡Bienvenido a la Veterinaria!")
#Se crea la recepcionista
print("-"*60)
recepcionista1 = Recepcionista("Paula", 635263)
print(f"{recepcionista1.mostrar_rol()}")

#Se crea el cliente y lo registra la recepcionista
print("-"*60)
cliente1 = Cliente("Laura", 52799099, 3202392337)
print(f"¡Se registro el cliente exitosamente!")
recepcionista1.registrar_cliente(cliente1)

#Se crean las mascotas que luego se agregan a la lista del cliente
print("-"*60)
mascota1= Mascota("Tigre","Gato", 10, 15)
mascota2 = Mascota("Corin", "Gato", 12, 15)
cliente1.agregar_mascota(mascota1)
cliente1.agregar_mascota(mascota2)

#Se imprimen las mascotas registradas
print(f"Las mascotas registradas son: ")
cliente1.mostrar_mascota()

#Se le asigna el Veterinario a la mascota donde se crean los medicamentos y añaden a la consulta
print("-"*100)
veterinario1 = Veterinario("Javier", 1054146026)
consulta1 = Consulta("Vomito constante", "Falta de hidratacion", veterinario1, mascota1)
tratamiento1 = Tratamiento("Kd care", 150000, 30)
tratamiento2 = Tratamiento("Hidratacion por suero", 50000, 30)

consulta1.crear_tratamientos(tratamiento1)
consulta1.crear_tratamientos(tratamiento2)
consulta1.mostrar_resumen()

#se imprimen los medicamentos recetados y el valor
print("-"*100)
print(f"Se le receto el/los tratamientos:")
consulta1.mostrar_tratamiento()

print("-"*100)
#Se calcula la factura
factura1 = Factura(consulta1, impuestos=0.19)
print(f"Total a pagar: {factura1.calcular_total()}")

"""pago1 = PagoTarjeta(factura1.calcular_total())
print(factura1.pagar(pago1))"""
pago2 = PagoEfectivo(factura1.calcular_total())
print(factura1.pagar(pago2))

print("-"*100)
print("Se cambio el Metodo de Pago a Transferencia")
pago3 = PagoTransferencia(factura1.calcular_total())
print(factura1.pagar(pago3))

print("-"*100)
print(f"Pago Exitoso, Feliz Día")  



