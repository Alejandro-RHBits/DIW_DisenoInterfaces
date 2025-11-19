#   1. Crea una función saludar(nombre) que reciba un nombre y devuelva un saludo:

nombre=str("")
peso=int()
altura=float()

def funcion_saludar(nombre):
    print(f"¡¡Hola {nombre}!!")

#   2. Crea una función calcular_imc(peso, altura) que devuelva el IMC usando la fórmula:

def calcular_imc(peso,altura):
    print(f"Tu IMC es de: ", peso/(altura*2))

#   3. Llama a estas funciones con los datos ingresados en el ejercicio 1 y muestra los resultados.

funcion_saludar("Alejandro")
calcular_imc(66, 1.70)