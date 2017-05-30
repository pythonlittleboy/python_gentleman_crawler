from index import MovieDAO
from index import SimilarDAO
from index import SysConst
from util import ImageSimilar
from util import SQueue
from index import DiskIndex
import os

def calcByActor(actor):
    movies = MovieDAO.getMoviesByCondition("actor = '" + actor + "' and vr = 1")
    print(movies)

    allImages = DiskIndex.getAllImages(SysConst.getImageCachePath())

    for movie in movies:
        calcMovie(movie, allImages)


def calcAllVR():
    movies = MovieDAO.getMoviesByCondition("vr = 1")
    #print(movies)
    allImages = DiskIndex.getAllImages(SysConst.getImageCachePath())
    for movie in movies:
        calcMovie(movie, allImages)

def calcMovie(movie, allImages):
    try:
        actor = movie["actor"]
        conn = SysConst.getConnect()
        basePath = SysConst.getImageCachePath() + actor + "//" + movie["av_number"] + ".jpg";

        if not os.path.exists(basePath):
            print("can not find file: " + basePath)
            return

        base = movie["av_number"]
        targetMap = getTargetMap(base, conn)
        print("compare " + actor + "/" + base)
        count = 0
        skipCount = 0

        for image in allImages:
            targetPath = image["fullpath"]
            target = image["filename"][0:-4]
            # exist = SimilarDAO.hasSimilar(base, target, conn)
            if not target in targetMap:
                # print(targetPath)
                count += 1

                if count % 500 == 0:
                    print("calc " + str(count))
                    conn.commit()
                    conn.close()
                    conn = SysConst.getConnect()

                similar = ImageSimilar.calc_similar_by_path(basePath, targetPath)
                obj = {"base": base, "target": target, "similar": similar}
                SimilarDAO.saveSimilar(obj, conn)
            else:
                skipCount += 1
                if skipCount % 2000 == 0:
                    print("skip " + str(skipCount))
    finally:
        conn.commit()
        conn.close()

def getTargetMap(base, conn):
    existTargetMovies = SimilarDAO.getSimilarsByCondition("base = '" + base + "'", conn)
    targetMap = {}
    for movie in existTargetMovies:
        targetMap[movie["target"]] = True
    return targetMap


# deleteSmallImages(SysConst.getImageCachePath())
# calcByActor("铃村爱里")
calcAllVR()