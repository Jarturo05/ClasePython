#Lambda: Las funiones funcionales funcionan de igual manera pero se con "lambda" es menos codigo
def suma4(n1, n2):
    resultado = n1 + n2
    return resultado

suma5 = lambda n1, n2: n1 + n2
print(suma4(5, 10))
print(suma5(5, 10))

es_mayor = lambda edad: "mayor de edad" if edad >= 18 else "Menor de edad"
print(es_mayor(17))

#Map: Se usa para lo que esta dentro de una lista se le asigne a una variable y resulva un enuncionado donde lo ponga en otra lista
numeros = [1, 2, 3, 4, 5]
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)

nombres = ["Alica", "Bob", "Charlie"]
nombres_mayusculas = list(map(lambda x: x.upper(), nombres))
print(nombres_mayusculas)

precios = [10, 20, 30, 40, 50]
precios_con_iva = list(map(lambda x: x * 1.19, precios))
print(precios_con_iva)

#Filter: Se llama y dentro se pone la funcion lambda para que resuelva ejericios, se usa como condicional o filtro como un for
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)




