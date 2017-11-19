import index.IndexActor as indexActor
import index.DiskIndex as diskIndex
import index.MagnetIO as magnetIO
import index.ActorDAO as ActorDAO

def saveMovieToDB():
    actors = ActorDAO.getFavorActors()

    allMovies = []

    for actor in actors:
        print("begin to read: " + str(actor))
        newMovies = indexActor.saveActorToDB(url=actor["url"], actor=actor["name"], cache=False)
        allMovies = allMovies + newMovies

    return allMovies


def findMagnetsByDB(actors):
    if len(actors) == 0:
        records = ActorDAO.getFavorActors()
        for record in records:
            actors.append(record["name"])
    print(actors)

    # TODO 改为读数据库
    movies = indexActor.findUndownloadFiles("G://Game//File//", actors)
    mags = []
    try:
        for movie in movies:
            mag = magnetIO.getMagnet(movie)
            if mag:
                mags.append(mag)
                print(mag)
    except(Exception):
        print(Exception)
    finally:
        for mag in mags:
            print(mag)


#print(saveMovieToDB());
# print(indexActor.findUndownloadFiles("G://Game//File//", ["幸田由真"]))
# "古川伊织", "三上悠亚", "高桥圣子", "天使萌", "彩乃奈奈", "一之濑遥", "铃村爱里", "坂口美穗乃","小岛南"
findMagnetsByDB(["河南实里", "菊川三叶"])
