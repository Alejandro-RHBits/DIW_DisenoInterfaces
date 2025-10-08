#   1. Modifica el ejercicio 1 para que la edad y altura se 
#   pidan en un bucle que repita hasta que se ingrese un número válido.

#   2.Usa try/except para capturar errores si el usuario escribe algo 
#   que no sea un número int o float en cada caso.

numero_correcto=1

print("¡¡Bienvenido Usuario!!")

while(numero_correcto!=0):

    nombre=input("Ingresa tu nombre a continuación: ")
    
    try:

        edad=int(input("Ingresa tu edad: "))
        
        altura=float(input("Ingresa tu altura en metros para finalizar: "))
        
        numero_correcto=int(input("Ingresa un número para salir del bucle: "))

    except ValueError:

        print("Error, lo que escribiste no es un numero, vuelve a intentarlo.")


print(f"Tu nombre es {nombre}, tienes la edad de {edad} años y mides {altura} metros")

