from models import *
from classes import *
from dic import *

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

def Results(nodo, gender):
    """ Recorre todos los nodos a través de sus enlaces,
        mostrando sus contenidos. """
    INFRA_PESO  = 0
    PESO_NORMAL = 0
    SOBRE_PESO  = 0
    OBESO       = 0

    q = Queue()
    while nodo:
        # muestra el dato
        if nodo:
            if str(nodo.gender) == str(gender):
                q.encolar(nodo)
        # ahora nodo apunta a nodo.prox
        nodo = nodo.prox

    for person in q.get():
        if person.index_mass() < 18.50:
            INFRA_PESO += 1
        elif person.index_mass() > 18.50 and person.index_mass() < 24.99:
            PESO_NORMAL += 1
        elif person.index_mass() >= 25 and person.index_mass() < 30:
            SOBRE_PESO += 1
        else:
            OBESO += 1

    if q.len() == 0:
        print("No existen registros del genero "+gender_a[str(gender)])
    else:
        print("Registros totales de personas del genero "+gender_a[str(gender)]+": "+str(q.len()))
        print("Porcentaje de "+gender_b[str(gender)]+" con infra peso: "+str((float(INFRA_PESO)/q.len())*100)+"%")
        print("Porcentaje de "+gender_b[str(gender)]+" con peso normal: "+str((float(PESO_NORMAL)/q.len())*100)+"%")
        print("Porcentaje de "+gender_b[str(gender)]+" con sobre peso: "+str((float(SOBRE_PESO)/q.len())*100)+"%")
        print("Porcentaje de "+gender_b[str(gender)]+" obesas: "+str((float(OBESO)/q.len())*100)+"%")

    """print("toal        : ", q.len() * 100 * ".")
    print("infra peso  : ", int(float(INFRA_PESO/q.len()) * 100) * ".")
    print("peso normal : ", int(float(PESO_NORMAL/q.len()) * 100) * ".")
    print("sobre peso  : ", int(float(SOBRE_PESO/q.len()) * 100) * ".")
    print("obeso       : ", int(float(OBESO/q.len()) * 100) * ".")"""



