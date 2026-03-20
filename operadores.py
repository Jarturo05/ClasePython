
# Calcula cuanto ganan 3 empleados a la semana
nombre1 = input("Ingrese el nombre del primer empleado: ")
nombre2 = input("Ingrese el nombre del segundo empleado: ")
nombre3= input("Ingrese el nombre del tercer empleado: ")

horasEmpleado1 = float(input(f"Cuantas horas trabajo a la semana {nombre1}: "))
valorEmpleado1 = int(input(f"Cuanto gana por hora {nombre1}: "))

sueldoEmpleado1 = horasEmpleado1 * valorEmpleado1

print(f"El empleado {nombre1} gano a la semana: {sueldoEmpleado1:.0f}")

horasEmpleado2 = float(input(f"Cuantas horas trabajo a la semana {nombre2}: "))
valorEmpleado2 = float(input(f"Cuanto gana por hora {nombre2}: "))

sueldoEmpleado2 = horasEmpleado2 * valorEmpleado2

print(f"El empleado {nombre2} gano a la semana: {sueldoEmpleado2:.0f}")

horasEmpleado3 = float(input(f"Cuantas horas trabajo a la semana {nombre3}: "))
valorEmpleado3 = float(input(f"Cuanto gana por hora {nombre3}: "))

sueldoEmpleado3 = horasEmpleado3 * valorEmpleado3

print(f"El empleado {nombre3} gano a la semana {sueldoEmpleado3:.0f}")

"""Calcula cuanto gana 1 empleado a la semana
horasTrabajadas = float(input("Ingrese el numero de horas: "))
valorGanadoporHora = int(input("Cuanto gana por hora: "))

trabajo = horasTrabajadas * valorGanadoporHora

print("El total ganado a la semana es de:", f"{trabajo:.0f}")"""


"""Calcular el area de un traingulo rectangulo
base1 = float(input("Ingrese la base del triangulo rectangulo: "))
altura1 = float(input("Ingrese la altura del triangulo rectangulo: "))

areaTrianguloRectangulo = (base1 * altura1) / 2

print("El area del triangulo rectangulo es: ", areaTrianguloRectangulo)"""

"""Calcular el area de un circulo
diametro1 = float(input("Ingrese el diametro del circulo: "))

radio1 = diametro1/2

areaCirculo = 3.1416 * radio1**2

print("El area del circulo es igual a: ", areaCirculo)"""

"""Calculadora que calcula todas las operaciones aritmeticas
nombre1 = input("Ingrese su nombre: ")

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))

print("Hola " + nombre1 ,"la suma de los numeros es: ", numero1 + numero2)
print("la resta de los numeros es: ", numero1-numero2)
print("la multiplicacion de los numeros es: ", numero1*numero2)
print("la division de los numeros es: ", f"{(numero1/numero2):.2f}")
print("la division entera de los numeros es: ", numero1//numero2)
print("el modulo de los numeros es: ", numero1%numero2)
print("la potencia de los numeros es: ", numero1**numero2)"""




"""a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número: "))
c = str(input("Digite el simbolo que quiere evaluar: "))

suma = a + b """


"""asignacion de varias variables
a, b, c = 1, 2, 3
print(f"Los valores son a={a}, b={b}, c={c}")

asignacion de un dato en diferentes variables
n1 = n2 = n3 = 5
print(f"El numero de n1={n1}, n2={n2}, n3={n3}")

formato profesional
print(f"hola mundo {5+2} esto es una suma")"""
