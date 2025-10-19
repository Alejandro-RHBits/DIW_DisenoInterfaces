#   1.Pide al usuario su nombre, edad y altura en metros.

print("¡¡Bienvenido Usuario!!")
nombre=input("Ingresa tu nombre a continuación: ")
edad=int(input("Ingresa tu edad: "))
altura=float(input("Ingresa tu altura en metros para finalizar: "))

#   2.Muestra un mensaje usando f-string con los datos ingresados.

print(f"Tu nombre es {nombre}, tienes la edad de {edad} años y mides {altura} metros")

#   3.Muestra el tipo de dato de cada variable.

print("La variable nombre es de tipo: ", type(nombre).__name__)
print("La variable edad es de tipo: ", type(edad).__name__)
print("La variable altura es de tipo: ", type(altura).__name__)
