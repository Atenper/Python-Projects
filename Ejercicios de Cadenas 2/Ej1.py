def buscainterfaz(interfaz,linea):
    a=0
    b=len(interfaz)
    # while b <= len(linea):
    #     if interfaz != linea[a:b]:
    #         a+=1
    #         b+=1
    #     else:
    #         return "Contiene la linea"
    # Metodo facil
    for interfaz in linea:
        return "Contiene la linea"

def main(args):
    linea="iface eth0 inet static"
    interfazabuscar="eth0"
    print(buscainterfaz(interfazabuscar,linea))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
