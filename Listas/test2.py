def main(args):
    lista = [('xilosofia', 5), ('zisica', 8), ('Mates', 4), ('Latin', 9), ('Historia', 8)]
    # Ordenar y filtrar en un solo paso
    lista_ordenada = sorted([x for x in lista if x[1] >= 5], key=lambda x: x[0])
    
    print("Lista ordenada y filtrada:", lista_ordenada)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))