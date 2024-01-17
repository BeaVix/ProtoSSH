from subprocess import Popen
from .Menu import Menu
from .Command import Command
from .Data import Data
from .clear import clear
from getpass import getpass
from prompt_toolkit import HTML
from prompt_toolkit import print_formatted_text as print

class MenuController:
    def __init__(self) -> None:
        self.commMenu= Menu("Comando de conexion")

    def setModel(self, model:Data):
        self.model = model
    
    def makeMenus(self):
        model = self.model

        domMenu = Menu("Dominios", self.makeCommands(model.doms, model.setDom))
        defaultDomMenu = Menu("Dominios", self.makeCommands(model.doms, model.setDefaultDom))

        perfMenu = Menu("Perfiles", self.makeCommands(model.perfs, model.setPerf))
        defaultPerfMenu = Menu("Perfiles", self.makeCommands(model.perfs, model.setDefaultPerf))

        srvrComms = []
        defaultSrvrComms = []
        for x in self.model.srvrs:
            serverMenu = Menu("Servidores", self.makeCommands(x["servidores"], model.setServer))
            defaultSrvrMenu = Menu("Servidores", self.makeCommands(x["servidores"], model.setDefaultServer))
            srvrComms.append(Command(x["plataforma"], serverMenu.show))
            defaultSrvrComms.append(Command(x["plataforma"], defaultSrvrMenu.show))
        srvrMenu = Menu("Plataformas", tuple(srvrComms))
        defaultPlatsMenu = Menu("Plataformas", tuple(defaultSrvrComms))

        configMenuOpts = (
            Command("Ingresar usuario predeterminado", self.setDefault, (lambda a: self.model.setDefaultUser(a), "Ingresar usuario")),
            Command("Ingresar dominio predeterminado", defaultDomMenu.show),
            Command("Seleccionar perfil predeterminado", defaultPerfMenu.show),
            Command("Seleccionar servidor predeterminado", defaultPlatsMenu.show)
        )
        configMenu = Menu("Configuración", configMenuOpts)

        opts = (
        Command("Ingresar usuario", self.setDefault, (lambda a: self.model.setUser(a), "Ingresar usuario")), 
        Command("Seleccionar dominio", domMenu.show),
        Command("Seleccionar perfil", perfMenu.show), 
        Command("Seleccionar servidor", srvrMenu.show), 
        Command("Mostrar comando de conexión", self.showComm), 
        Command("Conectar a servidor",self.conSrvr), 
        Command("Configuración", configMenu.show), 
        Command("Info",self.setDefault, (None, "<cyan>ProtoSSH</cyan>\nVersión 3.0.0\nHecho con Python 3.8.10\n<goldenrod>BeaVix</goldenrod>")), 
        )
        self.mainMenu = Menu("ProtoSSH", opts)

    def showComm(self):
        pswd = self.model.pswd
        if pswd != "":
            while True:
                print("Mostrar contraseña? s/n")
                answer = input(">>").lower() 
                if answer == "s":
                    break
                elif answer == "n":
                    pswd = "*"*len(self.model.pswd)
                    break
        tab = " "*self.commMenu.tab
        commData = "%sUsuario: %s\n%sDominio: %s\n%sPerfil: %s\n%sServidor: %s\n%sContraseña: %s\n\n%sComando final: ssh %s\n" % (tab, self.model.user, tab, self.model.dominio, tab, self.model.perfil, tab, self.model.server, tab, pswd, tab, self.model.getCommstr())
        self.commMenu.setContent(commData)
        self.commMenu.show()
        
    def conSrvr(self):
        clear()
        if not self.model.complete:
            print(HTML('<aaa fg="ansiwhite" bg="ansiyellow">Faltan ingresar datos:</aaa>'))
            if self.model.user == "":
                print("Usuario")
            if self.model.dominio == "":
                print("Dominio")
            if self.model.perfil == "":
                print("Perfil")
            if self.model.server == "":
                print("Servidor")
            # if self.model.pswd ==:
            #    print("Contraseña")
            input('')
            return
        Popen('putty -ssh '+self.model.getCommstr())
        input('Presione enter...')

    def setDefault(self, callback, message:str="", hide:bool=False):
        clear()
        if message != "": 
            print(HTML(message))
        val = input(">>") if not hide else getpass(">>")
        if callback:
            callback(val)
    
    def makeCommands(self, arr, callback)->tuple:
        comms = []
        for x in arr:
            comms.append(Command(x, callback, [x]))
        return tuple(comms)