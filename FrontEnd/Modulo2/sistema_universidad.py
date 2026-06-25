"""Sistema de Universidad
Relación entre clases
Persona es clase padre.
Estudiante y Profesor heredan de Persona → herencia.
Curso tiene estudiantes → agregación.
Curso crea sus evaluaciones → composición."""

from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def mostrar_nombre(self):
        pass

class Estudiante(Persona):
    def mostrar_nombre(self):
        return f"Nombre del estudiante: {self.nombre}"

class Profesor(Persona):
    def mostrar_nombre(self):
        return f"Nombre del Profesor: {self.nombre}"

class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        self.estudiantes = []
            
    def agregar_estudiantes(self, estudiante):
        self.estudiantes.append(estudiante)

    def mostrar_estudiantes(self):
        print(f"Curso: {self.nombre}, Profesor: {self.profesor.nombre}")
        for estudiante in self.estudiantes:
            print(estudiante.mostrar_nombre())

class Evaluaciones:
    def __init__(self, curso, hora, fecha, preguntas):
        self.curso = curso
        self.hora = hora
        self.fecha = fecha
        self.preguntas = preguntas
    
    def mostrar_info_evaluacion(self):
        return f"La evaluacion de {self.curso.nombre} se presentara el: {self.fecha} a las: {self.hora} y contendra un total de: {self.preguntas} preguntas"
    
estudiante1 = Estudiante("Arturo")
estudiante2 = Estudiante("Carlos")
estudiante3 = Estudiante("Juanes")
profesor1 = Profesor("Paredes")
profesor2 = Profesor("Amparo")
curso1 = Curso("Fisica", profesor1)
curso2 = Curso("Sociales", profesor2)

curso1.agregar_estudiantes(estudiante1)
curso2.agregar_estudiantes(estudiante2)
curso2.agregar_estudiantes(estudiante3)

curso1.mostrar_estudiantes()
curso2.mostrar_estudiantes()

evaluacion1 = Evaluaciones(curso1, 8, "09/04/2026", 15)
evaluacion2 = Evaluaciones(curso2, 9, "09/04/2026", 20)
    
print(evaluacion1.mostrar_info_evaluacion())
print(evaluacion2.mostrar_info_evaluacion())