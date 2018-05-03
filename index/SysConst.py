import sqlite3


def getHtmlCachePath(name):
    return "" + name


def getConnect():
    return sqlite3.connect('database.db')


def getSimiConnect():
    return sqlite3.connect('')


def getRootPath():
    return ""


def getVRPath():
    return ""


def getClassicPath():
    return ""


def getDownloadPath():
    return ""


def getTextPath():
    return ""


def getImageCachePath():
    return ""


def getImageTempPath():
    return ""


def getVRTrainDataPath():
    return ""
