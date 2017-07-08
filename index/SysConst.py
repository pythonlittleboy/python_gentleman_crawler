import sqlite3

def getConnect():
    return sqlite3.connect('D://Workspace//pythonWorkspace//python_gentleman_crawler//db//database.db')

def getSimiConnect():
    return sqlite3.connect('D://Workspace//pythonWorkspace//python_gentleman_crawler//db//db-similar.db')

def getRootPath():
    #return "G://Game//File//"
    return "D:\Game\Kodl"

def getVRPath():
    #return "G://Game//File//2Ring//"
    return "D://Game//Kodl//Ring"

def getClassicPath():
    #return "G://Game//File//1Class//"
    return "D://Game//Kodl//Classic"

def getTextPath():
    return "D://Game//Kodl//trash"

def getImageCachePath():
    return "D://Workspace//pythonWorkspace//python_gentleman_crawler//web//static//images//"

def getImageTempPath():
    return "D://Workspace//pythonWorkspace//python_gentleman_crawler//web//static//temp//"

def getVRTrainDataPath():
    return "D://Workspace//pythonWorkspace//python_gentleman_crawler//data//vr//"