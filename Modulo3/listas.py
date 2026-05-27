#? Clase 1
frutas = ["naranja", "papaya", "fresas", "pera", "fresas"]

#Para revisar la longitud de la lista
"""print(len(frutas))

#Para verificar si hay una variable dentro de la lista
print("naranja" in frutas)

#Insertar o agregar un valor en el lugar que se quiera
frutas.insert(2, "Kiwi")
print(frutas)

#Para sobrescribir en una varibale
frutas[2] = "aguacate"
print(frutas)

frutas.insert(3, "banano")
print(frutas)

#Para organizar si se maneja cadena de caracteres en orden alfabetico y si es en numeros del menor a mayor
frutas.sort()
print(frutas)"""

#?  Clase 2

#Para imprimir desde x valor hasta x valor en el segundo valor cuenta desde 1 y si se quiere desde x en adelante se deja vacio despues de los :
"""print(frutas[2:4])"""

#Para recorrer toda la lista y sumar los caracteres de cada valor
"""suma = 0
for elemento in frutas:
    suma += len(elemento)

print(suma)"""

#Para recorrer la lista con ciclo while
"""x = 0
while x < len(frutas):
    print(frutas[x])
    x += 1

print("Ya termino el ciclo")

i = 0
while i < len(frutas):
    if frutas[i] == "fresas":
        print(f"Encontre una manzana en la posicion {i}")
    i += 1"""

notas = []
x = 0
while x >= 0:
    calificaciones = int(input("Ingrese notas de 1 a 10 (-1 para finalizar): "))
    if calificaciones >= 1 and calificaciones <=10:
        notas.append(calificaciones)
    elif -1:
        promedio = (sum(notas)) / len(notas) 
        print(promedio)
        break
    else:
        print("Nota invalida")
    x += 1
        


 


