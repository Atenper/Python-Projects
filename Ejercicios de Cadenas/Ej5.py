def main(args):
    frase=input("Introduce la fraccion: ")
    b=frase.split("/")
    print(b)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
