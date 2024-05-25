###########################################################
###    Script de conexion automatica con Putty y SSH    ###
###                    ---BEAVIX--                      ###   
###                       v3.0.0                        ###
###########################################################

from os.path import exists
from helpers.MenuController import MenuController
from helpers.Data import *
from helpers.loadConfig import *

def makeFile(fileName: str):
    if(not exists(fileName)):
        fp = open(fileName, 'x')
        fp.close()

makeFile('dominios.json')
makeFile('perfiles.json')
makeFile('servidores.json')

data = Data()
menus = MenuController()
menus.setModel(data)
menus.makeMenus()

if(not exists('config.json')):
    fp = open('config.json', 'w')
    fp.write('{"user": "", "pswd":"", "dom":"", "perf":"", "srvr":""}')
    fp.close()

loadConfig(data)

def main():
    while True:
        menus.mainMenu.show()

main()