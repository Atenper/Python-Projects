def main(args):
    frase=input("Introduce la fraccion: ")
    b=frase.split("/")
    print(b)
    a= int(b[0])/int(b[1])
    print("El resultado de la fraccion es",a)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
