from models import *
from classes import *
from dic import *
from utils import clearConsole

def AddPersons(persons):
    clearConsole()
    i = 0
    p = None
    while i != persons:

        try:
            gender = int(input("Ingrese el genero de la persona Nº"+str(i+1)+" (1 -> Masculino / 2 -> Femenino):"))
            if gender != 1 and gender != 2 :
                gender = 1

            age = int(input("Ingrese la edad de la persona Nº"+str(i+1)+" :"))
            height = float(input("Ingrese la altura de la persona Nº"+str(i+1)+" :"))
            weight = float(input("Ingrese el peso de la persona Nº"+str(i+1)+" :"))

            if i == 0:
                p = Person((i+1), gender, age, height, weight)
            else:
                p = Person((i+1), gender, age, height, weight, p)

            i = i + 1
        except Exception as e:
            print("Ingrese los datos correctamente")
            print("*El genero debe ser un número entero")
            print("*El edad debe ser un número entero")
            print("*La altura y el peso deben ser un númericas")

    return p

def showList(nodo):
    clearConsole()
    while nodo:
        print (nodo)
        nodo = nodo.prox

def setRangeAge():
    age = {"age1": 0, "age2": 150}

    aux = input("Desea ingresar rango de edades (y/n):").lower()

    if aux == "y":
        try:
            age["age1"] = int(input("Ingrese el minimo de edad de las persona a valorar:"))
            age["age2"] = int(input("Ingrese el maximo de edad de las persona a valorar:"))
        except Exception as e:
            print("Ingrese los datos correctamente")
            print("*Los rango de edades deben ser numeros enteros")

    return age

def validatePerson(Personas):
    if Personas:
        return True
    else:
        print("Debe ingresar personas")
        return False

def Results(nodo, age, gender = 0):
    INFRA_PESO  = 0
    PESO_NORMAL = 0
    SOBRE_PESO  = 0
    OBESO       = 0

    clearConsole()
    q = Queue()
    while nodo:
        if nodo:
            if int(nodo.age) > (int(age["age1"])-1) and int(nodo.age) < (int(age["age2"])+1):
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
        print("Registros totales de personas "+gender_a[str(gender)]+": "+str(q.len())+" entre la edad de "+str(age["age1"])+" y "+str(age["age2"]))
        print("Porcentaje de "+gender_b[str(gender)]+" con infra peso: "+str((float(INFRA_PESO)/q.len())*100)+"%")
        print("Porcentaje de "+gender_b[str(gender)]+" con peso normal: "+str((float(PESO_NORMAL)/q.len())*100)+"%")
        print("Porcentaje de "+gender_b[str(gender)]+" con sobre peso: "+str((float(SOBRE_PESO)/q.len())*100)+"%")
        print("Porcentaje de "+gender_b[str(gender)]+" obesas: "+str((float(OBESO)/q.len())*100)+"%")
