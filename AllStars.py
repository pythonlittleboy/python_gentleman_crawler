import index.IndexActor as indexActor
import index.DiskIndex as diskIndex
import index.MagnetIO as magnetIO


def run():
    stars = [
        # {"url": "http://www.nh87.cn/guchuanyizhi/", "actor": "古川伊织"},
        # {"url": "http://www.nh87.cn/sanshangyouya/", "actor": "三上悠亚"}
        {"url": "http://www.nh87.cn/tianshimeng/", "actor": "天使萌"}
    ]

    allFiles = diskIndex.getAllMovies("G://Game//File//")

    cache = False
    allMovies = []

    for star in stars:
        newMovies = indexActor.indexActor(url=star["url"], actor=star["actor"], cache=cache, files=allFiles)
        allMovies = allMovies + newMovies

    mags = []
    for movie in allMovies:
        mag = magnetIO.getMagnet(movie["av_number"])
        if mag:
            # print(mag)
            mags.append(mag)

    for mag in mags:
        print(mag)


def saveMovieToDB():
    """
            {"url": "http://www.nh87.cn/guchuanyizhi/", "actor": "古川伊织"},
            {"url": "http://www.nh87.cn/sanshangyouya/", "actor": "三上悠亚"},
            {"url": "http://www.nh87.cn/tianshimeng/", "actor": "天使萌"},
            {"url": "http://www.nh87.cn/lingyuanaimili/", "actor": "铃原爱蜜莉"},
            {"url": "http://www.nh87.cn/gaoqiaoshengzi/", "actor": "高桥圣子"},
            {"url": "http://www.nh87.cn/ximeizhenyou/", "actor": "希美真由"},
            {"url": "http://www.nh87.cn/xidaoaili/", "actor": "希岛爱理"},
            {"url": "http://www.nh87.cn/xiqijiexika/", "actor": "希崎杰西卡"},
            {"url": "http://www.nh87.cn/caimeixunguo/", "actor": "彩美旬果"},
            {"url": "http://www.nh87.cn/tibenjieai/", "actor": "笹本结爱"}
            {"url": "http://www.nh87.cn/youtiancaiyexiang/", "actor": "友田彩也香"},
            {"url": "http://www.nh87.cn/cainainainai/", "actor": "彩乃奈奈"},
            
            """
    stars = [
        {"url": "http://www.nh87.cn/cainainainai/", "actor": "彩乃奈奈"},
        {"url": "http://www.nh87.cn/yizhilaiyao/", "actor": "一之濑遥"},
        {"url": "http://www.nh87.cn/lingcunaili/", "actor": "铃村爱里"},
        {"url": "http://www.nh87.cn/bankoumeisuinai/", "actor": "坂口美穗乃"},
        {"url": "http://www.nh87.cn/xiaodaonan/", "actor": "小岛南"}
    ]

    allMovies = []

    for star in stars:
        newMovies = indexActor.saveActorToDB(url=star["url"], actor=star["actor"], cache=False)
        allMovies = allMovies + newMovies

    return allMovies


def findMagnetsByDB(actors):
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
#"古川伊织", "三上悠亚", "高桥圣子", "天使萌", "彩乃奈奈", "一之濑遥", "铃村爱里", "坂口美穗乃","小岛南"
findMagnetsByDB(["坂口美穗乃"])
