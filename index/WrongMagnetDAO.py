import sqlite3
import time
from pprint import pprint
from index import SysConst

def getConnect():
    return SysConst.getConnect()


def saveMagnet(av, conn):
   
    avNumber = av["av_number"]
    magnet = av["magnet"]
    createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    #print(avNumber, magnet, createTime)

    conn.execute(
        "insert into t_wrong_magnets (av_number, magnet, create_time) values (?, ?, ?)",
        [avNumber, magnet, createTime])

    return True


def findWrongMagnets(avNumber):
    conn = SysConst.getConnect()

    cursor = conn.execute("SELECT magnet, create_time from t_wrong_magnets where av_number = ?", [avNumber])

    results = []
    for row in cursor:
        results.append(row[0])

    conn.close()

    return results
