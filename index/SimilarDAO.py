import time
from index import SysConst

def getConnect():
    return SysConst.getConnect()

def hasSimilar(base, target, conn):
    cursor = conn.cursor()
    cursor = cursor.execute("SELECT * from t_movies_similar where base=? and target=?", [base, target])

    return (len(cursor.fetchall()) > 0)


def getSimilarsByCondition(condition, conn):
    cursor = conn.execute("SELECT base, target, similar from t_movies_similar where " + condition, [])

    results = []
    for row in cursor:
        results.append({"base": row[0], "target": row[1], "similar": row[2]})

    return results

def getSimilarsByBase(base, conn):
    cursor = conn.execute("SELECT base, target, similar from t_movies_similar s "
                          " left join t_movies m on s.target=m.av_number "
                          " where m.local is null and base=? "
                          " order by s.similar desc", [base])

    results = []
    for row in cursor:
        results.append({"base": row[0], "target": row[1], "similar": row[2]})

    return results

def saveSimilar(movie, conn):
    base = movie["base"]
    target = movie["target"]
    similar = movie["similar"]

    cursor = conn.cursor()
    """
    cursor = cursor.execute("SELECT * from t_movies_similar where base=? and target=?", [base, target])

    if (len(cursor.fetchall()) > 0):
        return True
    """

    cursor.execute(
        "insert into t_movies_similar (base, target, similar) values (?, ?, ?)",
        [base, target, similar])

    return False

def getAllBaseMovies(conn):
    cursor = conn.execute("select distinct base from t_movies_similar", [])

    results = []
    for row in cursor:
        results.append({"av_number": row[0]})

    return results