from index import SysConst
from index.AvNumberPicReader import getAvNumberPic
from index.HtmlIO import readHtml
import index.MovieDAO as movieDAO
import index.DiskIndex as diskIndex
import time
from util import Log

def indexActor(url, actor, cache, files, shortName):
    avList = []

    html = readHtml(shortName, url, cache)
    #Log.info("111")
    results = getAvNumberPic(html)
    Log.info("find av 2: " + str(len(results)))

    for av in results:
        av["actor"] = actor
        av["short_name"] = shortName
        # print(av)
        avList.append(av)

    diskIndex.findLocalMovies(avList, files)

    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    newList = []

    conn = SysConst.getConnect()

    for av in avList:
        exists = movieDAO.saveMovie(av, conn)
        #saveImage(av)
        #movieDAO.updateMovieFile(av)
        #if not exists:
            #print("find movie: " + av["av_number"])

        if not av.get("local_movie") and now > av.get("public_time"):
            newList.append(av)

    conn.commit()
    conn.close()

    return newList

def saveActorToDB(url, actor, cache, shortName):
    avList = []
    html = readHtml(shortName, url, cache)
    results = getAvNumberPic(html)
    Log.info("saveActorToDB find " + actor + " movies: " + str(len(results)))

    for av in results:
        av["actor"] = actor
        av["short_name"] = shortName
        # print(av)
        avList.append(av)

    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    newList = []

    conn = SysConst.getConnect()

    for av in avList:
        exists = movieDAO.saveMovie(av, conn)
        #saveImage(av)
        #movieDAO.updateMovieFile(av)
        if not exists:
            Log.info("find new movie: " + str(av))
            newList.append(av)

        #if now > av.get("public_time"):

    conn.commit()
    conn.close()

    return avList

def findUndownloadFiles(path, actors):
    allNumbers = []

    for actor in actors:
        allNumbers = allNumbers + movieDAO.getAllMoviesByActor(actor)

    allFiles = diskIndex.getAllMovies(path)
    unloadedNumbers = []
    for avNumber in allNumbers:
        name = avNumber.lower()
        first = name[0:name.find('-')]
        second = name[name.find('-') + 1:]
        found = False
        for file in allFiles:
            filename = file["filename"].lower()
            if filename.find(first) > -1 and filename.find(second) > -1:
                found = True
                Log.info("find " + name + " : " + file["fullpath"])
                break;
        else:
            unloadedNumbers.append(name)

    return unloadedNumbers

# allFiles = diskIndex.getAllMovies("G://Game//File//")
# print(indexActor(url="http://www.nh87.cn/guchuanyizhi/", actor="古川伊织", cache=True, files=allFiles))
# print(indexActor(url="http://www.nh87.cn/tianshimeng/", actor="天使萌", cache=True, files=allFiles))
# print(findUndownloadFiles("G://Game//File//"))