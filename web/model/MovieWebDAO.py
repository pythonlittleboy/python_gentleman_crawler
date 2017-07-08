import time
from index import SysConst


def getConnect():
    return SysConst.getConnect()


def getRecentlyMovies(start, limit):
    conn = getConnect()
    cursor = conn.execute("select av_number, actor, title from t_movies where local = 0 and skip != 1 and trash != 1 order by create_time desc limit ?,? ", [start, limit])

    results = []
    for row in cursor:
        results.append({"av_number": row[0], "actor": row[1], "title": row[2]})

    conn.close()

    return results

def getDownloadMovies(start, limit):
    conn = getConnect()
    cursor = conn.execute("select av_number, actor, title from t_movies where local = 2 order by create_time desc limit ?,? ", [start, limit])

    results = []
    for row in cursor:
        results.append({"av_number": row[0], "actor": row[1], "title": row[2]})

    conn.close()

    return results

def skipMovie(avNumber):
    conn = getConnect()
    cursor = conn.execute("update t_movies set skip=1,local=0 where av_number = ?", [avNumber])
    conn.commit()
    conn.close()

def downloadMovie(avNumber):
    conn = getConnect()
    cursor = conn.execute("update t_movies set local=2 where av_number = ?", [avNumber])
    conn.commit()
    conn.close()
