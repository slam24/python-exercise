import platform
import os

def init_menu():
    print (30 * "-" , "MENU" , 30 * "-")
    print ("1. Ingresar el numero de personas a entrevistar")
    print ("2. Ingresar personas")
    print ("3. Listar personas")
    print ("4. Resultados de las mujeres")
    print ("5. Resultados de los hombres")
    print ("6. Resultados de todo el grupo")
    print ("7. Exit")
    print (67 * "-")

def clearConsole(clear = None):
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
