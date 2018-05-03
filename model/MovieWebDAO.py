import time
from index import SysConst


def getConnect():
    return SysConst.getConnect()


def getRecentlyMovies(start, limit):
    conn = getConnect()
    cursor = conn.execute("select av_number, actor, title, short_name, title_cn from t_movies m "
                          " where not exists (select av_number from t_download d where d.av_number=m.av_number)  "
                          " order by create_time desc limit ?,? ", [start, limit])

    results = []
    for row in cursor:
        results.append({"av_number": row[0], "actor": row[1], "title": row[2], "short_name": row[3], "title_cn": row[4]})

    conn.close()

    return results

def countRecentlyMovies():
    conn = getConnect()
    cursor = conn.execute(
        "select count(*) from t_movies m "
        " where not exists (select av_number from t_download d where d.av_number=m.av_number)",
        [])

    row = cursor.fetchone()
    conn.close()

    total = row[0]
    return total


def getDownloadMovies(start, limit):
    conn = getConnect()
    cursor = conn.execute("select av_number, actor, title, short_name, title_cn from t_movies m"
                          " where exists (select av_number from t_download d "
                          "     where d.av_number=m.av_number and d.local=2 ) "
                          " order by create_time desc limit ?,? ", [start, limit])

    results = []
    for row in cursor:
        results.append({"av_number": row[0], "actor": row[1], "title": row[2], "short_name": row[3], "title_cn": row[4]})

    conn.close()

    return results


def countDownloadMovies():
    conn = getConnect()
    cursor = conn.execute("select count(*) from t_movies m"
                          " where exists (select av_number from t_download d "
                          "     where d.av_number=m.av_number and d.local=2 ) ", [])
    row = cursor.fetchone()
    conn.close()

    total = row[0]
    return total


def getFavorMovies(start, limit):
    conn = getConnect()
    cursor = conn.execute("select av_number, actor, title, m.short_name, title_cn from t_movies m "
                          " join t_actors a on m.actor = a.name "
                          " where a.favor = 1 "
                          " and not exists (select av_number from t_download d where d.av_number=m.av_number) "
                          " order by create_time desc limit ?,? ", [start, limit])

    results = []
    for row in cursor:
        results.append({"av_number": row[0], "actor": row[1], "title": row[2], "short_name": row[3], "title_cn": row[4]})

    conn.close()

    return results


def countFavorMovies():
    conn = getConnect()
    cursor = conn.execute("select count(*) from t_movies m "
                          " join t_actors a on m.actor = a.name"
                          " where a.favor = 1 "
                          " and not exists (select av_number from t_download d where d.av_number=m.av_number)", [])
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

    cursor = conn.execute("select av_number, actor, title, short_name, title_cn from t_movies m"
                          " where not exists (select av_number from t_download d where d.av_number=m.av_number)"
                          " and (m.title like ? or m.actor like ? or m.av_number like ?) "
                          " order by forcast desc limit ?,? ", [keyword, keyword, keyword, start, limit])

    results = []
    for row in cursor:
        results.append({"av_number": row[0], "actor": row[1], "title": row[2], "short_name": row[3], "title_cn": row[4]})

    conn.close()

    return results


def countSearchMovies(keyword):
    conn = getConnect()

    if not keyword:
        keyword = "%妹%"
    else:
        keyword = "%" + keyword + "%"

    cursor = conn.execute(
        "select count(*) from t_movies m"
        " where not exists (select av_number from t_download d where d.av_number=m.av_number) "
        " and (m.title like ? or m.actor like ? or m.av_number like ?)",
        [keyword, keyword, keyword])

    row = cursor.fetchone()
    conn.close()

    total = row[0]
    return total


def skipMovie(avNumber):
    conn = getConnect()
    # cursor = conn.execute("update t_movies set skip=1,local=0 where av_number = ?", [avNumber])

    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    conn.execute("insert into t_download(av_number, create_time, local, skip) values(?, ?, 0, 1);", [avNumber, now])

    conn.commit()
    conn.close()


def downloadMovie(avNumber):
    conn = getConnect()
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # cursor = conn.execute("update t_movies set local=2 where av_number = ?", [avNumber])

    conn.execute("insert into t_download(av_number, create_time, local) values(?, ?, 2);", [avNumber, now])

    conn.commit()
    conn.close()


def getForcastMovies(start, limit):
    conn = getConnect()
    cursor = conn.execute("select av_number, actor, title, short_name, title_cn from t_movies m"
                          " where not exists (select av_number from t_download d where d.av_number=m.av_number) "
                          " order by forcast desc limit ?,? ", [start, limit])

    results = []
    for row in cursor:
        results.append({"av_number": row[0], "actor": row[1], "title": row[2], "short_name": row[3], "title_cn": row[4]})

    conn.close()

    return results


def countForcastMovies():
    conn = getConnect()
    cursor = conn.execute(
        "select count(*) from t_movies m"
        " where not exists (select av_number from t_download d where d.av_number=m.av_number)",
        [])

    row = cursor.fetchone()
    conn.close()

    total = row[0]
    return total
