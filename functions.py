from models import *
from classes import *
from dic import *

def AddPersons(persons):
    i = 0
    p = None
    while i != persons:
        gender = input("Ingrese el genero de la persona Nº"+str(i+1)+" :")
        old = input("Ingrese la edad de la persona Nº"+str(i+1)+" :")
        height = input("Ingrese la altura de la persona Nº"+str(i+1)+" :")
        weight = input("Ingrese el peso de la persona Nº"+str(i+1)+" :")

        if i == 0:
            p = Person((i+1), gender, old, height, weight)
        else:
            p = Person((i+1), gender, old, height, weight, p)

        i = i + 1
    return p

def showList(nodo):
    while nodo:
        print (nodo)
        nodo = nodo.prox

def setRangeOld():
    old = {"old1": 0, "old2": 150}

    aux = input("Desea ingresar rango de edades (y/n):").lower()

    if aux == "y":
        old["old1"] = input("Ingrese el minimo de edad de las persona a valorar:")
        old["old2"] = input("Ingrese el maximo de edad de las persona a valorar:")

    return old

def validatePerson(Personas):
    if Personas:
        return True
    else:
        print("Debe ingresar personas")
        return False

def Results(nodo, old, gender = 0):
    INFRA_PESO  = 0
    PESO_NORMAL = 0
    SOBRE_PESO  = 0
    OBESO       = 0

    q = Queue()
    while nodo:
        if nodo:
            if (int(nodo.old)-1) > int(old["old1"]) and int(nodo.old) < (int(old["old2"]+1)):
                if gender == 0:
                    q.add(nodo)
                else:
                    if str(nodo.gender) == str(gender):
                        q.add(nodo)
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
        print("No existen registros "+gender_a[str(gender)]+" o no se encuentra en el rango de edad establecido")
    else:
        print("Registros totales de personas "+gender_a[str(gender)]+": "+str(q.len()))
        print("Porcentaje de "+gender_b[str(gender)]+" con infra peso: "+str((float(INFRA_PESO)/q.len())*100)+"%")
        print("Porcentaje de "+gender_b[str(gender)]+" con peso normal: "+str((float(PESO_NORMAL)/q.len())*100)+"%")
        print("Porcentaje de "+gender_b[str(gender)]+" con sobre peso: "+str((float(SOBRE_PESO)/q.len())*100)+"%")
        print("Porcentaje de "+gender_b[str(gender)]+" obesas: "+str((float(OBESO)/q.len())*100)+"%")
