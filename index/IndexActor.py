from index.AvNumberPicReader import getAvNumberPic
from index.HtmlIO import readHtml
from index.ImageIO import saveImage
import index.MovieDAO as movieDAO
import index.DiskIndex as diskIndex
import time

def indexActor(url, actor, cache, files):
    avList = [];

    html = readHtml(actor, url, cache)
    results = getAvNumberPic(html)
    print("find av: " + str(len(results)))

    for av in results:
        av["actor"] = actor
        #print(av)
        avList.append(av)

    diskIndex.findLocalMovies(avList, files)

    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    newList = [];
    for av in avList:
        exists = movieDAO.saveMovie(av)
        saveImage(av)

        if exists:
            movieDAO.updateMovieFile(av)

        if not av.get("local_movie") and now > av.get("public_time"):
            newList.append(av)

    return newList


allFiles = diskIndex.getAllMovies("G://Game//File//")
#print(indexActor(url="http://www.nh87.cn/guchuanyizhi/", actor="古川伊织", cache=True, files=allFiles))
print(indexActor(url="http://www.nh87.cn/tianshimeng/", actor="天使萌", cache=True, files=allFiles))