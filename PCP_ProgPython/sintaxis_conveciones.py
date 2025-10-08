"""Sirve para DocString"""

print("Hola mundo")

#Hoola
#Type sirve para definir que tipo es nuestra variable o valor
print(type(10))

edad=20

print(type(edad))

edad="Hola"

print(type(edad),type(10))

#Listas

lista1=["Hola",1,"Dos"]

#Las tuplas no se pueden modificar

tupla1=("Hola",2,"tres")

diccionario1 = {
    "nombre":"Paquito",
    "apellido":"Chocolatero",
    "usuario":"chocopaquito",
    "contrasena":"1234"
    }

print(diccionario1["contrasena"])

conjunto2={1,2,3,"Hola","adios"}

print(list(conjunto2)[0])

try:
    # Código que puede lanzar una excepción
    resultado = 10 / 2
except ZeroDivisionError:
    # Código a ejecutar si se produce una excepción del tipo ZeroDivisionError
    print("No se puede dividir por cero.")
except ValueError:
     print("No se puede dividir por algo que no sea un número")
else:
    # Código a ejecutar si no se produce ninguna excepción
    print("La división fue exitosa. El resultado es:", resultado)
finally:
    # Código a ejecutar siempre, independientemente de si se produce una excepción o no
    print("Esta línea se ejecutará siempre.")

def sumar(a, b):
  suma = a + b
  return suma   # Devuelve la suma de a y b

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
print(sumar(numero1, numero2))