import os

#Limpia pantalla
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')