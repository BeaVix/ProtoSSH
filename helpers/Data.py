from .jsonFuncs import *

class Data:
    def __init__(self, user="", dominio="", server="", perfil="", pswd=""):
        self.user = user
        self.dominio = dominio
        self.server = server
        self.perfil = perfil
        self.pswd = pswd
        self.__isComplete()
        self.doms =loadJson("dominios")
        self.perfs = loadJson("perfiles")
        self.srvrs = loadJson("servidores")
    
    def setUser(self, user) -> str:
        self.user = user
        self.__isComplete()
    
    def setDom(self, dom) -> str:
        self.dominio = dom
        self.__isComplete()
    
    def setServer(self, server) -> str:
        self.server = server
        self.__isComplete()
    
    def setPerf(self, perf) -> str:
        self.perfil = perf
        self.__isComplete()
    
    def setPswd(self, pswd) -> str:
        self.pswd = pswd
        self.__isComplete()
    
    def getCommstr(self) -> str:
        return  self.user+"@"+self.dominio+"%"+self.perfil+"%"+self.server+"@cyberark-bastion"

    def setDefaultUser(self, user:str):
        writeJson("config", "user", user)
        self.setUser(user)

    def setDefaultDom(self, dom:str):
        writeJson("config", "dom", dom)
        self.setDom(dom)
    
    def setDefaultPswd(self, pswd:str):
        writeJson("config", "pswd", pswd)
        self.setPswd(pswd)

    def setDefaultPerf(self, perf:str):
        writeJson("config", "perf", perf)
        self.setPerf(perf)
    
    def setDefaultServer(self, srvr:str):
        writeJson("config", "srvr", srvr)
        self.setServer(srvr)

    def __isComplete(self):
        if self.user == "" or self.dominio == "" or self.server == "" or self.perfil == "":
            self.complete = False
        else:
            self.complete = True