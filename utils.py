import platform
import os

def init_menu():
    ##clearConsole()
    print (30 * "-" , "MENU" , 30 * "-")
    print ("1. Ingresar el numero de personas a entrevistar")
    print ("2. Ingresar personas")
    print ("3. Listar personas")
    print ("5. Exit")
    print (67 * "-")

def clearConsole(clear = None):
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')