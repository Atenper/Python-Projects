#!/usr/bin/python3
import sys
import re
import argparse
def correocheck(correo):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patron,correo))
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("correos", nargs='+')
    args = parser.parse_args()
    for correo in args.correos:
        if correocheck(correo):
            print(f"{correo} es un correo valido")
        else:
            print ("cagaste")