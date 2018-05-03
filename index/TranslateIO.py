import time

from index import SysConst
from util import Translator
from util import Log

def getConnect():
    return SysConst.getConnect()


def get_batch_movies():
    conn = getConnect()
    cursor = conn.execute("SELECT av_number, title from t_movies where title_cn is null and length(title) > 0 limit 100")

    results = []
    for row in cursor:
        results.append({"av_number": row[0], "title": row[1]})

    conn.close()
    return results


def update_movie_title_cn(conn, av_number, title_cn):
    cursor = conn.cursor()
    cursor.execute("update t_movies set title_cn=? where av_number=?", [title_cn, av_number])


def run_translate():
    try:
        movies = get_batch_movies()
        size = len(movies)
        if size > 0:
            Log.info("begin translate movies: " + str(size))

            with getConnect() as conn:
                for movie in movies:
                    title_cn = Translator.jp_to_cn(movie['title'])
                    update_movie_title_cn(conn, movie['av_number'], title_cn)

            Log.info("translate end")
        else:
            Log.info("nothing to translate")
    except Exception as e:
        Log.exception(e)


if __name__ == '__main__':
    for i in range(1):
        print(">>>>>>>> " + str(i))
        run_translate()
        time.sleep(2)