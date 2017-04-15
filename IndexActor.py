from util.AvNumberPicReader import getAvNumberPic
from index.MovieDAO import saveAvNumberPic
from index.ImageIO import saveImage
from index.HtmlIO import readHtml

def indexActor(url, actor, cache):
    avList = [];

    html = readHtml(actor, url, cache)
    results = getAvNumberPic(html)

    for av in results:
        av["actor"] = actor
        # print(av)
        avList.append(av)

    newList = [];
    for av in avList:
        exists = saveAvNumberPic(av)
        if (exists == False):
            print("save image: " + str(av))
            newList.append(av);
            saveImage(av)

    return newList


#print(indexActor("http://www.nh87.cn/guchuanyizhi/", "古川伊织", False))
print(indexActor("http://www.nh87.cn/sanshangyouya/", "三上悠亚", False))