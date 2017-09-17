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

def countRecentlyMovies():
    conn = getConnect()
    cursor = conn.execute(
        "select count(*) from t_movies where local = 0 and skip != 1 and trash != 1",
        [])

    row = cursor.fetchone()
    conn.close()

    total = row[0]
    return total

def getDownloadMovies(start, limit):
    conn = getConnect()
    cursor = conn.execute("select av_number, actor, title from t_movies where local = 2 order by create_time desc limit ?,? ", [start, limit])

    results = []
    for row in cursor:
        results.append({"av_number": row[0], "actor": row[1], "title": row[2]})

    conn.close()

    return results
def countDownloadMovies():
    conn = getConnect()
    cursor = conn.execute("select count(*) from t_movies where local = 2", [])
    row = cursor.fetchone()
    conn.close()

    total = row[0]
    return total

def getFavorMovies(start, limit):
    conn = getConnect()
    cursor = conn.execute("select av_number, actor, title from t_movies m join t_actors a on m.actor = a.name where a.favor = 1 and m.local = 0 and m.trash = 0 order by create_time desc limit ?,? ", [start, limit])

    results = []
    for row in cursor:
        results.append({"av_number": row[0], "actor": row[1], "title": row[2]})

    conn.close()

    return results

def countFavorMovies():
    conn = getConnect()
    cursor = conn.execute("select count(*) from t_movies m join t_actors a on m.actor = a.name where a.favor = 1 and m.local = 0 and m.trash = 0", [])
    row = cursor.fetchone()
    conn.close()

    total = row[0]
    return total



def getSearchMovies(start, limit, keyword):
    conn = getConnect()

    if not keyword:
        keyword = "%妹%"
    else:
        keyword = "%" + keyword + "%"

    cursor = conn.execute("select av_number, actor, title from t_movies where local = 0 and skip = 0 and trash = 0 and (title like ? or actor like ?) order by create_time desc limit ?,? ", [keyword, keyword, start, limit])

    results = []
    for row in cursor:
        results.append({"av_number": row[0], "actor": row[1], "title": row[2]})

    conn.close()

    return results

def countSearchMovies(keyword):
    conn = getConnect()

    if not keyword:
        keyword = "%妹%"
    else:
        keyword = "%" + keyword + "%"

    cursor = conn.execute(
        "select count(*) from t_movies where local = 0 and skip = 0 and trash = 0 and (title like ? or actor like ?)",
        [keyword, keyword])

    row = cursor.fetchone()
    conn.close()

    total = row[0]
    return total

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


def getForcastMovies(start, limit):
    conn = getConnect()
    cursor = conn.execute("select av_number, actor, title from t_movies where local = 0 and skip != 1 and trash != 1 order by forcast desc limit ?,? ", [start, limit])

    results = []
    for row in cursor:
        results.append({"av_number": row[0], "actor": row[1], "title": row[2]})

    conn.close()

    return results

def countForcastMovies():
    conn = getConnect()
    cursor = conn.execute(
        "select count(*) from t_movies where local = 0 and skip != 1 and trash != 1",
        [])

    row = cursor.fetchone()
    conn.close()

    total = row[0]
    return total