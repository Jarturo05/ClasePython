"""# Ejercicio práctico (2 horas)
Sistema de Gestión Básica de Estudiantes
Contexto

Una universidad quiere desarrollar un pequeño programa en Python que permita registrar estudiantes y evaluar su estado académico de forma simple desde la terminal.

Tu tarea será desarrollar un script en Python estructurado con funciones que permita ingresar información de estudiantes, calcular su promedio y mostrar su estado académico.

Requisitos del programa

El programa debe permitir:

1️⃣ Registrar estudiantes
2️⃣ Calcular el promedio de tres notas
3️⃣ Determinar el estado del estudiante
4️⃣ Permitir registrar varios estudiantes usando un menú
5️⃣ Mostrar un resumen final

Reglas del sistema

Para cada estudiante se debe ingresar:

Nombre

Edad

Nota 1

Nota 2

Nota 3

El programa debe calcular:

promedio = (nota1 + nota2 + nota3) / 3

Y determinar el estado académico:

Promedio	Estado
>= 4.0	Aprobado
>= 3.0 y < 4.0	En recuperación
< 3.0	Reprobado
Estructura obligatoria del programa

El programa debe tener al menos estas funciones:

1️⃣ Función para registrar estudiante
def registrar_estudiante():

Debe pedir:

nombre

edad

3 notas

Debe retornar los datos.

2️⃣ Función para calcular promedio
def calcular_promedio(n1, n2, n3):

Debe retornar el promedio.

3️⃣ Función para determinar estado
def evaluar_estado(promedio):

Debe retornar:

"Aprobado"

"En recuperación"

"Reprobado"

4️⃣ Menú principal con bucle

El programa debe mostrar un menú como este:

1. Registrar estudiante
2. Salir

Debe usar un while para permitir registrar varios estudiantes.

Ejemplo de salida esperada
===== SISTEMA DE ESTUDIANTES =====

Ingrese el nombre del estudiante: Ana
Ingrese la edad: 20
Ingrese nota 1: 4.5
Ingrese nota 2: 3.8
Ingrese nota 3: 4.2

Promedio del estudiante: 4.17
Estado académico: Aprobado
Validaciones mínimas

El programa debe validar:

Que las notas estén entre 0 y 5

Que la edad sea mayor que 0

Si los datos no son válidos, debe pedirlos nuevamente.

Parte final (obligatoria)

Al terminar el programa debe mostrar:

Total de estudiantes registrados: X
Promedio general del grupo: X"""

#Se crea las opciones a elegir en el menu

menu = """
    Bienvenido al registro de estudiantes

1. Registrar estudiantes
2. Estudiantes registrados
3. Salir
"""
print(menu)

opcion = 0

#Se crea la funcion registrar_estudiante que permite inicializar el codigo pidiendo datos del estudiante
def registrar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    while True:
        edad = int(input("Ingrese la edad del estudiante: "))
        if edad <=0:
            print("Edad invalida digite nuevamente la edad")
        else:
            break        
    while True:
        nota1 = float(input(f"Ingrese la nota 1 del estudiante (0 a 5): "))
        if nota1 < 0 or nota1 > 5:
            print("Nota invalida debe estar entre 0 y 5")
        else:
            break
    while True:
        nota2 = float(input(f"Ingrese la nota 2 del estudiante (0 a 5): "))
        if nota2 < 0 or nota2 > 5:
            print("Nota invalida debe estar entre 0 y 5")
        else:
            break
    while True:
        nota3 = float(input(f"Ingrese la nota 3 del estudiante (0 a 5): "))
        if nota3 < 0 or nota3 > 5:
            print("Nota invalida debe estar entre 0 y 5")
        else:
            break
    return nombre, edad, nota1, nota2, nota3

#Se crea la funcion promedio que calcula dependiendo de las notas antes pedidas del estudiante
def calcular_promedio(n1, n2, n3):
    promedio = (n1 + n2 + n3) / 3
    return promedio

#Se crea la funcion estado que dependiendo del promedio del estudiante se imprime el estado
def evaluar_estado(promedio):
    if promedio >= 4:
        return "Aprobado"
    elif promedio >= 3 and promedio <= 4:
        return "Recuperacion"
    elif promedio < 3:
        return "Reprobado"
    else:
        return "Dato no valido"

#Se crea la funcion para mostrar en la opcion 2 del programa todos los estudiantes registrados hasta el momento.
#Utilizando el ciclo for para iniciar la lista y ir mostrando los estudiantes antes guardados
def mostrar_todos_los_estudiantes(lista_estudiantes):
    print("\n    Lista de Estudiantes     ")

    if len(lista_estudiantes) == 0:
        print("\n ¡No se han registrado estudiantes!")     

    for i, nombre in enumerate(lista_estudiantes, start=1):  
        print(f"{i}. {nombre}")

contador = 0
prom = 0
estudiantes = []

#Una vez creado los ciclos se inicia el programa en ciclo while para repetir el ciclo por si el usuario se equivoca o termina la accion en una opcion
#Se inician el contador, prom y opcion en 0 para iniciar el ciclo y permitir que dependiendo de las vueltas se ejecuten las respecticas operaciones
while True:
    opcion = int(input("Ingrese la opcion que desea: "))
    if opcion == 1:
        nombre, edad, nota1, nota2, nota3 = registrar_estudiante()
        promedio = calcular_promedio(nota1, nota2, nota3)
        estado = evaluar_estado(promedio)
        print(f"El estudiante {nombre} de edad {edad} años, tiene un promedio de {promedio:.2f} y se encuentra en estado de {estado}.")
        prom = promedio + prom
        contador += 1
        print("--> Regresando al Menú")
        print(menu)
#Se crea la lista estudiante para ir almacenando los datos de los estudiantes con un .append y ejecutar la funcion antes mencionada 
        estudiante = {
            "Nombre": nombre,
            "Edad": edad,
            "Promedio": promedio,
            "Estado": estado
        }

        estudiantes.append(estudiante)       

    elif opcion == 2:
        mostrar_todos_los_estudiantes(estudiantes)
        print("\n ----> Regresando al menu ---->") 
        print(menu)
#Se ejecuta la opcion salir sin antes mostrar el promedio que se basa en una suma del promedio del estudiante y el numero de veces que se ejecute el ciclo
#Luego se divide el promedio y la cantidad de veces dandonos el promedio total de los estudiantes y al finalizar el numero de estudiantes registrados.
    elif opcion == 3:
        if contador > 1:
            print(f"El promedio de los estudiantes registrados es: {prom/contador:.2f}")
            print(f"El número total de estudiantes registrados es: {contador}")
            print("\n Saliendo del menu. ¡Hasta Luego!")
            break
        else:
            print("\n Saliendo del menu. ¡Hasta Luego!")
            break
    else:
        print("Opcion invalida, digite nuevamente.")
        print(menu)

#Fin del codigo


