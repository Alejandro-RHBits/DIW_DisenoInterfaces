'''
Definir variable para número
Pedir usuario introduzca un número (3)
Validar que el usuario solo introduce valor del 1 al 18
Imprimir el número multiplicado por un rango de 1 a 10 y mostrar resultado

'''

try:
    
    num_usuario=int(input("¿Qué tabla de multiplicar quieres?: "))

except ValueError:

    while num_usuario < 0 or num_usuario >10:
        num_usuario=int(input("Ingresa una tabla entre el 1 y el 10: "))
