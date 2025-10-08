import emoji, random

colores=['e']

#FUNCION QUE SALUDA AL USUARIO
def saludo ():
    print("Bienvenido a Mastermind")
    print(emoji.emojize("Podrás usar los colores :red_circle: r, :yellow_circle: y, :white_circle: w, :black_circle: b", language="alias"))


#FUNCION QUE GENERA LOS COLORES ALEATORIOS
def combinacion_aleatoria():
    #colores=[emoji.emojize(':red_circle: r'),emoji.emojize(':yellow_circle: y'),emoji.emojize(':white_circle: w'),emoji.emojize(':white_circle: b')]
    colores=['r','y','w','b']
    listaEleccion=[]
    for i in range(4):
        eleccion=random.choice(colores)
        listaEleccion.append(eleccion)
    
    print(listaEleccion)
    return listaEleccion


#FUNCION QUE PIDE COLORES AL USUARIO
def ingresar_colores():
    colores=['r','y','w','b']
    while True:

        colorselect=list(input("\nIngresa una combinación con las letras mencionadas: "))

        if all(color in colores for color in colorselect) and len(colorselect)==4:
            print("Los colores ingresados fueron: ", colorselect)
            return colorselect
        else:
            print('Las letras utilizadas no son permitidas o no has utilizado 4 letras. Vuelve a intentarlo')
    

#FUNCION QUE COMPRUEBA QUE LOS COLORES DEL USUARIO Y LOS ALEATORIOS SEAN IGUALES O AVISA DE LOS COMUNES
def comprobacion_colores(coloresAleatorios,coloresElegidos):

    while coloresElegidos != coloresAleatorios:

        comunes = []
        coloresAleatorios2 = coloresAleatorios.copy()

        for c in coloresElegidos:
            if c in coloresAleatorios2:
                comunes.append(c)
                coloresAleatorios2.remove(c)  # quitamos para no contar repetidos

        print("Colores que coinciden: ", comunes)

        coloresElegidos=list(input("\nIngresa otra vez los colores: "))
    
    return comunes


saludo()
coloresAleatorios=combinacion_aleatoria()
coloresElegidos=ingresar_colores()

comprobacion_colores(coloresAleatorios, coloresElegidos)

