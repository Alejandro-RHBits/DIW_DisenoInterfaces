#   1. Instala la librería emoji en tu entorno virtual.
#   2. Muestra un mensaje con un emoji usando la librería.

#   Primero usamos el comando "py -m pip install emoji" para instalar la librería

#   Importamos la librería

import emoji;

print(emoji.emojize("¡Bienvenido Usuario! ¿Estás preparado para empezar? :eyes:"))

peso=int()
altura=float()

def calcular_imc_con_emoji(peso, altura):

    imc = peso/(altura*2)
    if imc < 18.5:
        estado = "Bajo peso " + emoji.emojize(":warning:", language="alias")
    elif imc < 25:
        estado = "Normal " + emoji.emojize(":smile:", language="alias")
    else:
        estado = "Sobrepeso " + emoji.emojize(":exclamation:", language="alias")
    return imc, estado

print(calcular_imc_con_emoji(int(input("Ingresa tu peso: ")), (float(input("Ingresa tu altura en metros: ")))))
