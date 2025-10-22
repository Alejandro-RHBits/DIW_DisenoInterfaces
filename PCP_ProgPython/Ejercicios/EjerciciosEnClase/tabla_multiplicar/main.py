import sys, Practica1 as f

def main():
    '''
    Dado un número por el usuario, se mostrará su tabla de multiplicar
    '''
    f.pedirNumero()
    f.pintarTablas(f.numeroUsuario)

if __name__ == "_main_":
    main()