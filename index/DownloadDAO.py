from index import SysConst


def get_all_download():
    conn = SysConst.getConnect()
    cursor = conn.execute("SELECT av_number from t_download where local != 1 and trash != 1")

    results = []
    for row in cursor:
        results.append(row[0])

    conn.close()

    return results


def mark_download(conn, av):
    cursor = conn.cursor()

    av_number = av["av_number"]
    local = av.get("local")
    classic = av.get("classic")
    vr = av.get("vr")
    trash = av.get("trash")

    cursor.execute("update t_download set local=?,classic=?,vr=?,trash=? where av_number=?",
                   [local, classic, vr, trash, av_number])


if __name__ == '__main__':
    av = {"av_number": "CEMN-004", "local": 0, "classic": 0, "vr": 0, "trash": 1}

    with SysConst.getConnect() as conn:
        mark_download(conn, av)
