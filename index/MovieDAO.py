import sqlite3
import time
from pprint import pprint
from index import SysConst

def getConnect():
    return SysConst.getConnect()


def saveMovie(av, conn):
    #conn = SysConst.getConnect()

    avNumber = av["av_number"]
    remoteCover = av["remote_cover"]
    actor = av["actor"];
    publicTime = av.get("public_time", None)
    title = av.get("title")

    cursor = conn.cursor()
    cursor = cursor.execute("SELECT * from t_movies where av_number=?", [avNumber])

    if (len(cursor.fetchall()) > 0):
        return True

    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    cursor.execute(
        "insert into t_movies (av_number, actor, title, remote_cover, create_time, public_time) values (?, ?, ?, ?, ?, ?)",
        [avNumber, actor, title, remoteCover, now, publicTime])
    #conn.commit()
    #conn.close()

    return False


def updateMovieFile(conn, av):
    cursor = conn.cursor()

    avNumber = av["av_number"]
    local = av.get("local")
    classic = av.get("classic")
    vr = av.get("vr")
    trash = av.get("trash")
    cursor.execute("update t_movies set local=?,classic=?,vr=?,trash=? where av_number=?",
                   [local, classic, vr, trash, avNumber])


def getAllMovies():
    conn = getConnect()
    cursor = conn.execute("SELECT av_number from t_movies")

    results = []
    for row in cursor:
        results.append(row[0])

    conn.close()

    return results


def getAllMoviesByActor(actor):
    conn = getConnect()
    cursor = conn.execute("SELECT * from t_movies where actor=?", [actor])

    results = []
    for row in cursor:
        results.append(row[0])

    conn.close()

    return results

def getNoMagnetMovies():
    conn = getConnect()

    lastweek = round(time.time() - 24 * 60 * 60 * 6)
    cursor = conn.execute("SELECT av_number, actor, title, remote_cover, magnet "
                    " from t_movies "
                    " where local = 2 and magnet is null and last_read_time < ? "
                    " order by last_read_time asc ", [lastweek])

    results = []
    for row in cursor:
        results.append({"av_number": row[0], "actor": row[1], "title": row[2], "remote_cover": row[3], "magnet": row[4]})

    conn.close()

    return results

def getMoviesByCondition(condition):
    conn = getConnect()
    cursor = conn.execute("SELECT av_number, actor, title, remote_cover, magnet from t_movies where " + condition, [])

    results = []
    for row in cursor:
        results.append({"av_number": row[0], "actor": row[1], "title": row[2], "remote_cover": row[3], "magnet": row[4]})

    conn.close()

    return results

def updateMovieMagnet(avNumber, magnet, conn):
    cursor = conn.cursor()
    cursor.execute("update t_movies set magnet=? where av_number=?",
                   [magnet, avNumber])


def updateMovieMagnet2(avNumber, magnet):
    #print(avNumber + ": " + magnet)
    conn = SysConst.getConnect()
    conn.execute("update t_movies set magnet=? where av_number=?",
                   [magnet, avNumber])
    conn.commit()
    conn.close()

def updateMovieLastReadTime(avNumber):
    conn = SysConst.getConnect()
    now = round(time.time())

    cursor = conn.cursor()
    cursor.execute(
        "update t_movies set last_read_time = ? where av_number = ?",
        [now, avNumber])

    conn.commit()
    conn.close()

def updateMovieVRForcast(avNumber, forcast, conn):
    cursor = conn.cursor()
    cursor.execute(
        "update t_movies set forcast = ? where av_number = ?",
        [forcast, avNumber])

def getMovieByAvNumber(avNumber, conn):
    cursor = conn.execute("SELECT av_number, actor, title, remote_cover, magnet from t_movies where av_number=?", [avNumber])

    results = []
    for row in cursor:
        return {"av_number": row[0], "actor": row[1], "title": row[2], "remote_cover": row[3], "magnet": row[4]}

    return False

def deleteMovie(avNumber):
    conn = getConnect()
    conn.execute("delete from t_movies where av_number=?", [avNumber])
    conn.close()
    print("deleted " + avNumber)