import math
from prompt_toolkit import print_formatted_text as print
from prompt_toolkit import HTML
from .clear import *

class Menu:
    tab = 13
    width = 33
    tColor = "ansigreen"
    oColor = "cyan"
    maxTLen = 26
    page = 0

    def __init__(self, title:str, ops:tuple=(), content:str=""):
        self.title = title
        self.ops = ops
        self.content = content

    def __showTitle(self):
        line = " "*self.tab+"-"*self.width+"\n"
        out = "<%s>" % self.tColor
        out += line
        i = 0
        b = 0
        while len(self.title)-i > 0:
            tLen = len(self.title[self.maxTLen*b:self.maxTLen*b+self.maxTLen+1])
            lSpace = 13-math.floor(tLen/2)
            rSpace = 14-math.ceil(tLen/2)
            out += " "*self.tab+"-"*3+" "*lSpace+self.title[self.maxTLen*b:self.maxTLen*b+self.maxTLen+1]+' '*rSpace+"-"*3+"\n"
            i += tLen
            b += 1
        out += line
        out +="</%s>" % self.tColor
        print(HTML(out))
    
    def __showCommands(self):
        opLen = len(self.ops)
        if opLen != 0:
            out = ""
            comm = "<%s>"+" "*self.tab+"[%i]</%s> %s\n"
            i = 1
            hasPrevOp = True if self.page > 0 else False
            if(hasPrevOp):
                commAmnt = 8
                hasNextOp = True if len(self.ops[8+7*(self.page-1):]) > 8 else False
                opRan = 8+7*(self.page-1)
            else:
                commAmnt = 9
                hasNextOp = True if opLen > 9 else False
                opRan = 0
            commAmnt -= 1 if hasNextOp else 0
            for x in self.ops[opRan:opRan+commAmnt]:
                out += comm % (self.oColor, i, self.oColor, x.name)
                i += 1
            if hasNextOp or hasPrevOp:
                out += "\n"
            if hasPrevOp:
                out += comm % (self.oColor, 8, self.oColor, "← Previo")
            if hasNextOp:
                out += comm % (self.oColor, 9, self.oColor, "Siguiente →")
            out += "\n"+comm % ("yellow", 0, "yellow", "Salir")
            print(HTML(out))
    
    def __showContent(self):
        if self.content != "":
            print(HTML(self.content))
    
    def __waitForCommand(self):
        while True:
            choice = input(">>")
            if choice.isnumeric():
                choice = int(choice)
                hasPrevOp = True if self.page > 0 else False
                if(hasPrevOp):
                    hasNextOp = True if len(self.ops[8+7*(self.page-1):]) > 8 else False
                    if hasNextOp:
                        nroOps = len(self.ops[8+7*(self.page-1):8+7*(self.page-1)+7])
                    else:
                        nroOps = len(self.ops[8+7*(self.page-1):8+7*(self.page-1)+8])
                else:
                    hasNextOp = True if len(self.ops) > 9 else False
                    if hasNextOp:
                        nroOps = len(self.ops[:8])
                    else:
                        nroOps = len(self.ops[:9])

                if hasPrevOp and choice == 8:
                    self.setPage(self.page - 1)
                    break
                if hasNextOp and choice == 9:
                    self.setPage(self.page + 1)
                    break
                if choice > nroOps or choice < 0:
                    print('Opción fuera del rango')
                elif choice == 0:
                    exit()
                else:
                    if self.page > 0:
                        self.ops[8+7*(self.page-1)+choice-1].exec()
                        break
                    self.ops[choice-1].exec()
                    break
            else:
                print('Ingrese un número para seleccionar una opción')

    def setPage(self, num):
        self.page = num
        self.show()

    def setContent(self, content:str):
        self.content = content

    def show(self):
        clear()
        self.__showTitle()
        self.__showContent()
        if len(self.ops) != 0:
            self.__showCommands()
            self.__waitForCommand()
        else:
            input("presione enter para continuar ...")