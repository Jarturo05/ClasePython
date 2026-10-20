
#Preguntar al usuario un animal (perro, gato, pez)

animales = input("Ingrese el nombre de un animal: ")

match animales:
    case "perro":
        print("Guau")
    case "gato":
        print("Miau")
    case "pez":
        print("Glu")
    case _:
        print("Palabra no válida")

"""#Condicional match y case

dia = int(input("Ingrese un numero entre 1 y 7: "))

match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")
    case _:
        print("Numero no valido")"""
    
"""#Escribir un programa que solicite un numero entre 1 y 7 imprimir conforme a los dias de la semana
dia = int(input("Ingrese un numero entre 1 y 7: "))

if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miercoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sabado")
elif dia == 7:
    print("Domingo")
else:
    print("Numero no valido")"""

"""Condicional elif
edad = int(input("Ingrese su edad: "))
if edad >= 0 and edad <= 5:
    print("Primera infancia")
elif edad <= 12:
    print("Infancia")
elif edad <= 17:
    print("Adolesencia")
else:
    print("Adultez")"""


"""Escribir un programa que solicite al usuario su edad y determine si es mayor de edad o no
edad = int(input("Escriba su edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")"""

""" Condicionales
sueldo = int(input("Ingrese el sueldo del empleado: "))

if sueldo < 2000000:
    print("Si se cumplió la condición")
    sueldo += 200000
else:
    print("No se cumplió la condición")

print("El sueldo del empleado es: ", sueldo)"""

