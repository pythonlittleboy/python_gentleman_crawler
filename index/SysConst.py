import sqlite3

def getConnect():
    return sqlite3.connect('D://Workspace//pythonWorkspace//python_gentleman_crawler//db//database.db')