#   1. Crea un archivo main.py con el siguiente contenido:
import sys

def main():
    # sys.argv es una lista con los argumentos de la línea de comandos
    # El primer elemento (posición 0) es siempre el nombre del archivo
    print("Argumentos recibidos:", sys.argv)

    # Si hay argumentos adicionales, los mostramos
    if len(sys.argv) > 3:
        nombre = sys.argv[1]
        edad = sys.argv[2]
        ciudad = sys.argv[3]
        mascota = sys.argv[4]

        print(f"Hola, {nombre} 👋, tu edad es de {edad} años, vives en {ciudad} y tu mascota se llama {mascota}")
    else:
        print("No se proporcionó ningún argumento")

if __name__ == "__main__":
    main()