import json

#Abre y retorna archivo json
def loadJson(fileName)->list:
    f = open(fileName+'.json')
    try:
        arr = json.load(f)
        return arr
    except json.JSONDecodeError:
        return []

def writeJson(fileName, key,value):
    fileCont = loadJson(fileName) #Contenido del archivo 
    fileCont[key] = value
    file = open(fileName+'.json', 'w')
    json.dump(fileCont, file)