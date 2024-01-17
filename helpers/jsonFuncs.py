import json

#Abre y retorna archivo json
def loadJson(fileName):
    f = open(fileName+'.json')
    arr = json.load(f)
    return arr

def writeJson(fileName, key,value):
    fileCont = loadJson(fileName) #Contenido del archivo 
    fileCont[key] = value
    file = open(fileName+'.json', 'w')
    json.dump(fileCont, file)