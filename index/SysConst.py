import sqlite3

def getConnect():
    return sqlite3.connect('D://Workspace//pythonWorkspace//python_gentleman_crawler//db//database.db')

def getRootPath():
    return "G://Game//File//"

def getVRPath():
    return "G://Game//File//2Ring//"

def getClassicPath():
    return "G://Game//File//1Class//"

def getImageCachePath():
    return "D://MyDrivers//cache//images//"

def getImageTempPath():
    return "D://MyDrivers//cache//temp//"

def getVRTrainDataPath():
    return "D://Workspace//pythonWorkspace//python_gentleman_crawler//data//vr//"