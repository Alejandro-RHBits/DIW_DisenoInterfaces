#   1. Pide al usuario una lista de números separados por coma

print("¡Bienvenido Usuario!")
lista = input("Ingresa cuatro números separados por coma: ")

listaNumeros=list(map(int,lista.split(","))) #Le decimos que es una lista, que cada parte se transforme 
                                             #en entero y que vuelva independiente cada numero separado
                                             #por "," es decir ["1","2"...]

#   3. Calcula y muestra: suma, promedio, máximo y mínimo usando funciones.

def suma(listaNumeros):
    return sum(listaNumeros)

def promedio(listaNumeros):
    return sum(listaNumeros)/len(listaNumeros)

def maximo(listaNumeros):
    return max(listaNumeros)

def minimo(listaNumeros):
    return min(listaNumeros)

#   4. Usa f-strings para mostrar los resultados con formato:

print(f"La suma es {suma(listaNumeros)}, el promedio es {promedio(listaNumeros)}, el máximo {maximo(listaNumeros)}, el mínimo {minimo(listaNumeros)}")