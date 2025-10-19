#   1. Crea un archivo calculadora.py que al ejecutarse acepte 3 argumentos, un número, 
#   un operador (+, *, / o -) y otro número.

#   2. Si el número de argumentos es incorrecto o los argumentos no son del tipo que se
#   espera debe mostrar error y una ayuda de cómo se usa

#   3. Usa emojis en las salidas para que sea más vistoso.

import sys
import emoji;

def calculadora():
    #Mostramos los valores escritos al usuario
    print("Argumentos para la calculadora: ", sys.argv)

    #sys.argv es una lista que contiene los argumentos al ejecutar por terminal
    #len cuenta cuantos elementos hay en total, el 0 siempre es el nombre del codigo
    if len(sys.argv) > 3:
        try:

            n1=int(sys.argv[1])
            simbolo=sys.argv[2]
            n2=int(sys.argv[3])

        #Capturamos el error si uno de los operadores no es un número
        except ValueError:
            print(emoji.emojize("\nError :warning:, ambos operadores deben ser números")) #\n para salto de linea
            print("Ejemplo")
            print(emoji.emojize("python calculadora.py 5 + 3 :white_check_mark: \n", language="alias"))
            return

        #Mostramos posibles errores y hacemos las operaciones con los diferentes
        #simbolos.

        #En caso de que no encuentre ninguno de esos operadores en la variable "simbolo"
        #saltará un aviso de "Operador no reconocido"
        if (simbolo not in ["+","-","*","x","/"]):
            print(emoji.emojize(f"\nOperador '{simbolo}' no reconocido :warning:, Usa +,-,*,x,/ \n"))
        elif (simbolo=="+"):
            print(emoji.emojize(f"\nResultado: {n1} {simbolo} {n2} = {n1+n2} :white_check_mark: \n", language="alias"))
        elif (simbolo=="-"):
            print(emoji.emojize(f"\nResultado: {n1} {simbolo} {n2} = {n1-n2} :white_check_mark: \n", language="alias"))
        elif (simbolo=="*" or simbolo=="x"):
            print(emoji.emojize(f"\nResultado: {n1} {simbolo} {n2} = {n1*n2} :white_check_mark: \n", language="alias"))
        elif (simbolo=="/"):
            print(emoji.emojize(f"\nResultado: {n1} {simbolo} {n2} = {n1/n2} :white_check_mark: \n", language="alias"))
    
    #En caso de que se encuentren menos de 3 argumentos en la terminal
    #salta información de como usar la calculadora.
    else:
        print(emoji.emojize("\nComo usar la calculadora: :white_check_mark:"))
        print("calculadora.py <numero1> <operador> <numero2>")
        print("Ejemplos:")
        print(emoji.emojize("python calculadora.py 5 + 3"))
        print(emoji.emojize("python calculadora.py 10 * 4 \n"))

if __name__ == "__main__":
    calculadora()
