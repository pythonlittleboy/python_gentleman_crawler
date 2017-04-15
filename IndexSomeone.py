from util.AvNumberPicReader import getAvNumberPic
from index.MovieDAO import saveAvNumberPic

def indexActor(url, actor):
    avList = [];

    results = getAvNumberPic(url)

    for np in results:
        av = {}
        av["actor"] = actor
        av["av_number"] = np["name"]
        av["remote_cover"] = np["img"]
        print(av)
        avList.append(av)

    for av in avList:
        saveAvNumberPic(av)

indexActor("http://www.nh87.cn/guchuanyizhi/", "古川伊织")