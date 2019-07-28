from utils import init_menu, clearConsole
from functions import AddPersons, showList, Results, validatePerson, setRangeAge, sederFake

def main():
    Numero_de_personas_a_entrevistar = 0
    Personas = None
    loop = True
    choice = 0
    clearConsole()

    while loop:
        init_menu()
        try:
            choice = int(input("Enter your choice [1-5]: "))
        except Exception as e:
            print("Ingrese los datos correctamente")
            print("*Debe ingresar un valor númerico")

        if choice==1:
            clearConsole()
            try:
                Numero_de_personas_a_entrevistar = int(input("Ingrese la cantidad de personas a ingresar: "))
            except Exception as e:
                print("Ingrese los datos correctamente")
                print("*El número de personas debe ser un valor númerico entero")
        elif choice==2:
            if Numero_de_personas_a_entrevistar > 0 :
                Personas = AddPersons(Numero_de_personas_a_entrevistar)
            else:
                print("Debe ingresar la cantidad de personas a entrevistar")
        elif choice==3:
            if validatePerson: print(showList(Personas))
        elif choice==4:
            if validatePerson: Results(Personas, setRangeAge(), 2)
        elif choice==5:
            if validatePerson: Results(Personas, setRangeAge(), 1)
        elif choice==6:
            if validatePerson: Results(Personas, setRangeAge())
        elif choice==7:
            Personas = sederFake()
        elif choice==8:
            loop=False
        else:
            print("Opcion incorrecta")
main()
