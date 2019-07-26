from models import *
from classes import *

def AddPersons(persons):
    i = 0
    p = None
    while i != persons:
        gender = input("Ingrese el genero de la persona Nº"+str(i+1)+" :")
        height = input("Ingrese la altura de la persona Nº"+str(i+1)+" :")
        weight = input("Ingrese el peso de la persona Nº"+str(i+1)+" :")

        if i == 0:
            p = Person((i+1), gender, height, weight)
        else:
            p = Person((i+1), gender, height, weight, p)

        i = i + 1
    return p

def showList(nodo):
    """ Recorre todos los nodos a través de sus enlaces,
        mostrando sus contenidos. """

    # cicla mientras nodo no es None
    while nodo:
        # muestra el dato
        print (nodo)
        # ahora nodo apunta a nodo.prox
        nodo = nodo.prox

def Results(nodo):
    """ Recorre todos los nodos a través de sus enlaces,
        mostrando sus contenidos. """

    # cicla mientras nodo no es None
    i = 0
    q = Queue()
    while nodo:
        # muestra el dato
        if nodo:
            if str(nodo.gender) == str(1):
                print("Hombre")
            else:
                print("Mujer")
                q.encolar(nodo)
        # ahora nodo apunta a nodo.prox
        nodo = nodo.prox

    print(q.get()[0].index_mass())
