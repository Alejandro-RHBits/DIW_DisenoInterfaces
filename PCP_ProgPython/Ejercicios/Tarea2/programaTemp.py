temperaturas=[]

def menu():
    print("\n-----BIENVENIDO USUARIO-----")
    print("Elige una de las opciones:")
    print("1.Ingresar Temperaturas.")
    print("2.Terminar el programa.")
    opcion=int(input("Ingresa tu elección: "))
    ingresarTemperaturas(opcion)

def ingresarTemperaturas(opcion):
    if opcion==1:
        opcion2="s"
        while opcion2!="n":
            ingresarTemp=int(input("Ingresa las temperaturas: "))
            temperaturas.append(ingresarTemp)
            calculartemperaturas(temperaturas)
            opcion2=input("Quieres ingresar otro dato (s/n): ")
    elif opcion==2:
        print("Adios!!")
    else:
        print("No existe esa opcion. Vuelve a intentarlo\n")
        menu()

def calculartemperaturas(temperaturas):
    tamanoArray=len(temperaturas)
    total=0
    mayor=max(temperaturas)
    print("La maxima temperatura es: ", mayor)
    menor=min(temperaturas)
    print("La menor temperatura es: ", menor)

    for a in range(tamanoArray):
        total=total+temperaturas[a]

    total=total/tamanoArray
    print("La media de temperaturas es: ", total)

menu()