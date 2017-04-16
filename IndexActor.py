from index.AvNumberPicReader import getAvNumberPic
from index.HtmlIO import readHtml
from index.ImageIO import saveImage
from index.MovieDAO import saveMovie


def indexActor(url, actor, cache):
    avList = [];

    html = readHtml(actor, url, cache)
    results = getAvNumberPic(html)
    print("find av: " + str(len(results)))

    for av in results:
        av["actor"] = actor
        #print(av)
        avList.append(av)

    newList = [];
    for av in avList:
        exists = saveMovie(av)
        saveImage(av)
        if (exists == False):
            print("save image: " + str(av))
            newList.append(av);
            #saveImage(av)

    return newList


#print(indexActor("http://www.nh87.cn/guchuanyizhi/", "古川伊织", False))
print(indexActor(url="http://www.nh87.cn/sanshangyouya/", actor="三上悠亚", cache=True))