#   1. Crea una función presentar_persona(nombre="Usuario", edad=None, *aficiones).
#   2. Prueba la función con diferentes números de aficiones.
#   3. Dale un valor por defecto al parámetro nombre para cuando no se pase ninguno.

#Modifiqué el orden para que el nombre pueda ser un valor por defecto
def presentar_personas(edad=None, *aficiones, nombre="Alejandro"):
    print(f"{nombre} tiene {edad} años y le gusta {aficiones}")


presentar_personas(19, "cantar","bailar","dibujar", "escribir", "correr", "pintar", "musica", nombre="Pepe")
presentar_personas(12, "comer","dormir","leer","hablar", "cantar")
presentar_personas(20,"dormir", nombre="Cris")
