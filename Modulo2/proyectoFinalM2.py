"""El siguiente es el proyecto de esta segunda unidad:
Ejercicio grupal: Sistema de gestión de hospital veterinario
Contexto

Una clínica veterinaria quiere desarrollar un sistema orientado a objetos para organizar su funcionamiento diario. El sistema debe permitir gestionar personas, mascotas, consultas, tratamientos, pagos y hospitalizaciones.

Los estudiantes deben analizar el problema, identificar las clases, construir el modelo UML y luego implementar una versión funcional en Python.

Objetivo del ejercicio

Diseñar e implementar un sistema en Python que permita modelar el funcionamiento básico de un hospital veterinario, aplicando correctamente relaciones entre clases y principios de POO.

Lo que debe incluir obligatoriamente

1. Clase abstracta
Debe existir una clase abstracta llamada Persona.

De ella deben heredar otras clases.

Atributos sugeridos:
nombre
documento
Método abstracto obligatorio:
mostrar_rol()

2. Herencia

Desde Persona deben heredar al menos estas clases:

Veterinario
Recepcionista
Cliente

Cada una debe implementar mostrar_rol() de forma diferente.

3. Asociación

Debe existir una relación de asociación entre:

Veterinario y Mascota

porque un veterinario puede atender muchas mascotas y una mascota puede ser atendida por distintos veterinarios en diferentes momentos.

Esa relación puede reflejarse en la clase Consulta, donde se conectan ambas clases.

4. Agregación

Debe existir una relación de agregación entre:

Cliente y Mascota

porque un cliente tiene mascotas, pero la mascota puede seguir existiendo aunque el cliente se elimine del sistema.

El cliente debe tener un atributo como:

mascotas = []

y un método:

agregar_mascota()

5. Composición

Debe existir una relación de composición entre:

Consulta y Tratamiento

porque una consulta crea sus tratamientos como parte de sí misma.

La idea es que el tratamiento nazca dentro de la consulta.

La clase Consulta puede tener:

lista de tratamientos
método crear_tratamiento()
6. Polimorfismo

Debe existir una clase abstracta llamada MetodoPago.

De ella deben heredar:

PagoEfectivo
PagoTarjeta
PagoTransferencia

Cada una debe implementar el método:

procesar_pago(monto)

Luego una clase Factura debe usar cualquier objeto de tipo MetodoPago para cobrar una consulta.

Clases mínimas sugeridas

Los estudiantes deben trabajar, como mínimo, con estas clases:

Persona (abstracta)
Veterinario
Recepcionista
Cliente
Mascota
Consulta
Tratamiento
Factura
MetodoPago (abstracta)
PagoEfectivo
PagoTarjeta
PagoTransferencia
Reglas del sistema
Persona

Clase abstracta.

Atributos:
nombre
documento
Método abstracto:
mostrar_rol()
Veterinario

Hereda de Persona.

Atributos:
especialidad
Métodos:
mostrar_rol()
atender_mascota()
Recepcionista

Hereda de Persona.

Métodos:
mostrar_rol()
registrar_cliente()
Cliente

Hereda de Persona.

Atributos:
telefono
lista de mascotas
Métodos:
mostrar_rol()
agregar_mascota()
mostrar_mascotas()
Mascota
Atributos:
nombre
especie
edad
peso
Métodos:
mostrar_info()
Consulta
Atributos:
mascota
veterinario
motivo
diagnostico
tratamientos
Métodos:
crear_tratamiento()
mostrar_resumen()
calcular_costo_consulta()

Aquí se evidencia:

asociación con Mascota
asociación con Veterinario
composición con Tratamiento
Tratamiento
Atributos:
nombre
costo
duracion_dias
Métodos:
mostrar_tratamiento()
MetodoPago

Clase abstracta.

Método abstracto:
procesar_pago(monto)
PagoEfectivo

Hereda de MetodoPago.

PagoTarjeta

Hereda de MetodoPago.

PagoTransferencia

Hereda de MetodoPago.

Cada una debe implementar procesar_pago() de forma distinta.

Factura
Atributos:
consulta
subtotal
impuesto
total
Métodos:
calcular_total()
pagar(metodo_pago)

Aquí se debe aplicar polimorfismo.

Tareas del grupo
Parte 1. Análisis y modelado

Antes de programar, cada grupo debe:

Identificar las clases
Identificar atributos y métodos
Dibujar el diagrama UML a mano o digital
Marcar claramente:
herencia
agregación
composición
asociación
polimorfismo
Parte 2. Implementación en Python

Deben programar el sistema con las clases y relaciones solicitadas.

El código debe permitir como mínimo:

crear un cliente
agregar una o más mascotas al cliente
crear un veterinario
registrar una consulta para una mascota
crear uno o más tratamientos dentro de la consulta
generar una factura
pagar la factura con distintos métodos de pago
Parte 3. Prueba del sistema

Cada grupo debe mostrar una ejecución donde ocurra lo siguiente:

Se crea un cliente
Se registran dos mascotas
Un veterinario atiende una de las mascotas
Se crea una consulta
La consulta genera dos tratamientos
Se calcula el costo total
Se paga con un método de pago
Luego se cambia el método de pago y se prueba nuevamente
Entregables esperados"""

#Primero se importa la libreria para utilizar el abstracmethod
from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    @abstractmethod
    def mostrar_rol(self):
        pass

class Veterinario(Persona):
    def mostrar_rol(self):
        print("Veterinario")
    
    def mostrar_especialidad(self):
        print(f"El veterinario {self.nombre} se especializa en animales")
    
class Cliente(Persona):
    def __init__(self, nombre, documento, telefono):
        super().__init__(nombre, documento)

        self.telefono = telefono
        self.mascotas = []

    def mostrar_rol(self):
        print("Cliente")
        
    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)
            
class Recepcionista(Persona):
    def mostrar_rol(self):
        print("Recepcionista")
    
    def registrar_cliente(self):
        print(f"Cliente: {self.nombre}, Documento: {cliente.documento} Telefono: {cliente.telefono}")

class Mascota:
    def __init__(self, nombre, especie, edad, peso):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

    def mostrar_info(self):
        print (f"""
        Nombre: {self.nombre}
        Especie: {self.especie}
        Edad: {self.edad}
        Peso: {self.peso}
        """)
    
class Tratamiento:
    def __init__(self, nombre, precio, duracion_dias):
        self.nombre = nombre
        self.precio = precio
        self.duracion_dias = duracion_dias
    
    def mostrar_tratamiento(self):
        return f"El tratamiento: {self.nombre} tiene un precio de : {self.precio} con duracion de: {self.duracion_dias} días"

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
        for tratamiento in self.tratamientos:
            print(f"El motivo de la consulta para la mascota: {self.mascota.nombre} es: {self.motivo} donde el veterinario: {self.veterinario.nombre} le diagnostico: {self.diagnostico} y le receto: {tratamiento.mostrar_tratamiento()}")

    def calcular_tratamiento(self):
        return sum(tratamiento.precio for tratamiento in self.tratamientos)
    
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
    
class PagoTransferencia(Metodo_Pago):
    def procesar_pago(self, monto, entidad):
        return f"Pago por transferencia a la entidad: {entidad} por valor de: {monto}"
    
class Factura:
    def __init__(self, consulta, impuestos=0.19):
        self.consulta = consulta
        self.impuestos = impuestos

    def calcular_total(self):
        subtotal = self.consulta.calcular_tratamiento()
        total = subtotal + (subtotal * self.impuestos)
        return f"{total:.2f}"
    
    def pagar(self, metodo_pago: Metodo_Pago):
        total = self.calcular_total()
        return metodo_pago.procesar_pago(total)

veterinario1 = Veterinario("Javier", 1054146026)
cliente1 = Cliente("Laura", 52799099, 3202392337)
recepcionista1 = Recepcionista("Paula", 635263)


mascota1= Mascota("Tigre","Gato", 10, 15)
mascota2 = Mascota("Corin", "Gato", 12, 15)

cliente1.agregar_mascota(mascota1)
cliente1.agregar_mascota(mascota2)

mascota1.mostrar_info()
mascota2.mostrar_info()

consulta1 = Consulta("Vomito constante", "Falta de hidratacion", veterinario1, mascota1)

tratamiento1 = Tratamiento("Kd care", 150000, 30)
tratamiento2 = Tratamiento("Hidratacion por suero", 50000, 30)

consulta1.crear_tratamientos(tratamiento1)
consulta1.crear_tratamientos(tratamiento2)

consulta1.mostrar_resumen()

factura1 = Factura(consulta1, impuestos=0.19)
print(f"Total a pagar: {factura1.calcular_total()}")

pago1 = PagoTarjeta(factura1.calcular_total())
print(factura1.pagar(pago1))








    



