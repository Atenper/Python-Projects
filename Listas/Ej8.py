def createAlumno(lista):
    a=int(input("Cuantos alumnos hay"))
    for i in range(0,a):
        alumno=input("Dame el nombre del alumno")
        lista.append(alumno)
        createAsignatura(lista,alumno)

def createAsignatura(lista,alumno):
    r=int(input("Cuantas asignaturas tiene "+ alumno))
    media=0
    for i in range(0,r):
        a=input("Nombre de la asignatura: ")
        b=float(input("Nota: "))
        media += b
        tupla=[a,b]
        lista.append((tupla))
    media=media/r
    print("La media es "+str(media))
    lista.append(media)

def imprimeLista(lista):
    print(lista)
def main(args):
    lista=list()
    createAlumno(lista)
    imprimeLista(lista)

    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))