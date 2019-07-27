from utils import init_menu
from functions import AddPersons, showList, Results

def main():
    ##Init function 
    Numero_de_personas_a_entrevistar = 0
    Personas = None
    loop=True

    while loop:
        init_menu()
        choice = int(input("Enter your choice [1-5]: "))

        if choice==1:
            Numero_de_personas_a_entrevistar = int(input("Ingrese la cantidad de personas a ingresar: "))
        elif choice==2:
            if Numero_de_personas_a_entrevistar > 0 :
                Personas = AddPersons(Numero_de_personas_a_entrevistar)
            else:
                print("Debe ingresar la cantidad de personas a entrevistar")
        elif choice==3:
            if Personas:
                print(showList(Personas))
            else:
                print("Debe ingresar personas")
        elif choice==4:
            Results(Personas, 2)
        elif choice==5:
            Results(Personas, 1)
        elif choice==6:
            loop=False
        else:
            input("Opcion incorrecta")
main()
