import sqlite3

def getHtmlCachePath(name):
    return "/var/services/homes/lijl/dev/python_gentleman_crawler/static/temp/" + name

def getConnect():
    return sqlite3.connect('/var/services/homes/lijl/dev/python_gentleman_crawler/db/database.db')

def getSimiConnect():
    return sqlite3.connect('/var/services/homes/lijl/dev/python_gentleman_crawler/db/db-similar.db')

def getRootPath():
    return "/var/services/web/drivers/etc/kodl"

def getVRPath():
    return "/var/services/web/drivers/etc/kodl/ring"

def getClassicPath():
    return "/var/services/web/drivers/etc/kodl/classic"


def getDownloadPath():
    return "/var/services/web/drivers/etc/kodl/download"

def getTextPath():
    return "/var/services/web/drivers/etc/kodl/trash"
   
def getImageCachePath():
    return "/var/services/homes/lijl/dev/python_gentleman_crawler/static/images/"

def getImageTempPath():
    return "/var/services/homes/lijl/dev/python_gentleman_crawler/static/temp/"

def getVRTrainDataPath():
    return "/var/services/homes/lijl/dev/python_gentleman_crawler/data/vr/"