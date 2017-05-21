from index import SysConst
import time


def saveActors(actors):
    newActors = []
    conn = SysConst.getConnect()

    for actor in actors:
        exist = saveActor(actor, conn)
        if not exist:
            newActors.append(actor)

    conn.commit()
    conn.close()

    return newActors


def saveActor(actor, conn):
    name = actor["name"]
    url = actor["url"]

    cursor = conn.cursor()
    cursor = cursor.execute("SELECT * from t_actors where name=?", [name])

    if (len(cursor.fetchall()) > 0):
        return True

    cursor.execute(
        "insert into t_actors (name, url) values (?, ?)",
        [name, url])

    return False


def getAllActors():
    conn = SysConst.getConnect()
    yesterday = round(time.time() - 24 * 60 * 60)
    lastmonth = round(time.time() - 24 * 60 * 60 * 5)
    # print(yesterday)
    cursor = conn.execute("SELECT * from t_actors where "
                          " (favor = 1 and last_read_time < ?) "
                          " or (favor = 0 and last_read_time < ?)"
                          " or last_read_time is null"
                          " order by favor desc, last_read_time desc", [yesterday, lastmonth])

    results = []
    for row in cursor:
        one = {"name": row[0], "url": row[1]}
        results.append(one)

    conn.close()

    return results


def updateLastReadTime(name):
    conn = SysConst.getConnect()
    now = round(time.time())

    cursor = conn.cursor()
    cursor.execute(
        "update t_actors set last_read_time = ? where name = ?",
        [now, name])

    conn.commit()
    conn.close()


def getFavorActors():
    conn = SysConst.getConnect()
    yesterday = round(time.time() - 24 * 60 * 60)
    # print(yesterday)
    cursor = conn.execute("SELECT * from t_actors where favor = 1")

    results = []
    for row in cursor:
        one = {"name": row[0], "url": row[1]}
        results.append(one)

    conn.close()

    return results

# print(len(getAllActors()))
# print(time.ctime(round(time.time()) - 24 * 60 * 60))
# updateLastReadTime("三浦惠理子")
#print(getFavorActors())
