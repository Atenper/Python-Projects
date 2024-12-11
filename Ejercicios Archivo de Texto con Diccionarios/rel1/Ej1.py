import sys

def lectura():
    try:
        a=open("rel1.txt")
    except FileNotFoundError:
        print("Archivo no encontrado")
    contenido = a.read()
    a.close()
    return contenido

def main(args):
    print(lectura())
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))