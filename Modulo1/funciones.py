"""# No recibe nada y no devuelve nada
def suma1():
    a = int (input("Ingrese el primer número: "))
    b = int (input("Ingrese el segundo número: "))
    resultado = a + b
    print(f"La suma de {a} y {b} es: {resultado}")
suma1()"""

"""# Recibe parametros pero no devulve nada
def suma2(a,b):
    resultado = a + b
    print(f"La suma de {a} y {b} es: {resultado}")
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))

suma2(n1, n2)"""

"""# No recibe parametros pero devuelve un valor
def suma3():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    resultado = a + b
    return resultado
print(suma3())"""

"""# Recibe parametros y devuelve valores
def suma4(a, b):
    resultado = a + b
    return resultado

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))

print(suma4(n1, n2))"""

# Calculadora

menu = """
1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Division entera
6. Potencia
7. Modulo 
8. Salir
"""
print(menu)
opcion = 0

while opcion !=8:
    opcion = int(input("Ingrese la opcion que desea: "))
    if opcion >=1 and opcion <=7:
        numero1 = int(input("Ingrese el primer número: "))
        numero2 = int(input("Ingrese el segundo número: "))
        break
    elif opcion == 8:
        print("Gracias por participar. ¡Hasta Luego!")
        break
    else:
        print(f"Opcion no valida, regresando al menu")
        print(menu)      
       
def suma(a, b):
    resultado = a + b
    print(f"La suma de {a} y {b} es: {resultado}")

def resta(a, b):
    resultado = a - b
    print(f"La resta de {a} y {b} es: {resultado}")

def multiplicacion(a, b):
    resultado = a * b
    print(f"La multiplicación de {a} y {b} es: {resultado}")

def division(a, b):
    resultado = a / b
    print(f"La división de {a} y {b} es: {resultado}")

def divisionEntera(a, b):
    resultado = a // b
    print(f"La división entera de {a} y {b} es: {resultado}")

def potencia(a, b):
    resultado = a ** b
    print(f"La potencia de {a} y {b} es: {resultado}")

def modulo(a, b):
    resultado = a % b
    print(f"El modulo de {a} y {b} es: {resultado}")

match opcion:
    case 1:
        print(suma(numero1, numero2))
    case 2:
        print(resta(numero1, numero2))
    case 3:
        print(multiplicacion(numero1, numero2))
    case 4:
        print(division(numero1, numero2))
    case 5:
        print(divisionEntera(numero1, numero2))
    case 6:
        print(potencia(numero1, numero2))
    case 7:
        print(modulo(numero1, numero2))

print("Fin del ejercicio")




