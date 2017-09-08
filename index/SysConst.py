import sqlite3

def getConnect():
    return sqlite3.connect('D://Workspace//pythonWorkspace//python_gentleman_crawler//db//database.db')

def getSimiConnect():
    return sqlite3.connect('D://Workspace//pythonWorkspace//python_gentleman_crawler//db//db-similar.db')

def getRootPath():
    #return "G://Game//File//"
    return "Z:\drivers\etc\kodl"

def getVRPath():
    #return "G://Game//File//2Ring//"
    return "Z://drivers//etc//kodl//ring"

def getClassicPath():
    #return "G://Game//File//1Class//"
    return "Z://drivers//etc//kodl//classic"

def getTextPath():
    return "Z://drivers//etc//kodl//trash"
   
def getImageCachePath():
    return "D://Workspace//pythonWorkspace//python_gentleman_crawler//static//images//"

def getImageTempPath():
    return "D://Workspace//pythonWorkspace//python_gentleman_crawler//static//temp//"

def getVRTrainDataPath():
    return "D://Workspace//pythonWorkspace//python_gentleman_crawler//data//vr//"