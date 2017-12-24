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
    shortName = actor["short_name"]

    cursor = conn.cursor()
    cursor = cursor.execute("SELECT * from t_actors where short_name=?", [shortName])

    if (len(cursor.fetchall()) > 0):
        return True

    cursor.execute(
        "insert into t_actors (name, url, short_name) values (?, ?, ?)",
        [name, url, shortName])

    return False


def getAllActors():
    conn = SysConst.getConnect()
    yesterday = round(time.time() - 24 * 60 * 60)
    lastweek = round(time.time() - 24 * 60 * 60 * 3)
    # print(yesterday)
    cursor = conn.execute("SELECT name, url, short_name from t_actors where "
                          " (favor = 1 and last_read_time < ?) "
                          " or (favor = 0 and last_read_time < ?)"
                          " or last_read_time is null"
                          " order by favor desc, last_read_time desc", [yesterday, lastweek])

    results = []

    for row in cursor:
        url = row[1]

        # domain change to nanrenvip.co
        #url = url.replace("www.nh87.cn", "nanrenvip.net")
        url = url.replace("www.nh87.cn", "nanrenvip.co")
        url = url.replace("nanrenvip.net", "nanrenvip.co")

        one = {"name": row[0], "url": url, "short_name": row[2]}
        results.append(one)

    conn.close()

    return results

def getAllActorsFully():
    conn = SysConst.getConnect()
    # print(yesterday)
    cursor = conn.execute("SELECT name, url, short_name from t_actors "
                          " order by favor desc, last_read_time desc", [])

    results = []
    for row in cursor:
        one = {"name": row[0], "url": row[1], "short_name": row[2]}
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
