from .jsonFuncs import *
from .Data import Data

def loadConfig(data:Data):
    file = loadJson('config')
    data.setUser(file["user"])
    data.setPswd(file["pswd"])
    data.setDom(file["dom"])
    data.setPerf(file["perf"])
    data.setServer(file["srvr"])