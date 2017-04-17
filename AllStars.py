import index.IndexActor as indexActor
import index.DiskIndex as diskIndex
import index.MagnetIO as magnetIO

def run():
    stars = [
        #{"url": "http://www.nh87.cn/guchuanyizhi/", "actor": "古川伊织"},
        #{"url": "http://www.nh87.cn/sanshangyouya/", "actor": "三上悠亚"}
        {"url": "http://www.nh87.cn/tianshimeng/", "actor": "天使萌"}
    ]

    allFiles =  diskIndex.getAllMovies("G://Game//File//")

    cache = True
    allMovies = []

    for star in stars:
        newMovies = indexActor.indexActor(url=star["url"], actor=star["actor"], cache=cache, files=allFiles)
        allMovies = allMovies + newMovies

    mags = []
    for movie in allMovies:
        mag = magnetIO.getMagnet(movie["av_number"])
        if mag:
            #print(mag)
            mags.append(mag)

    for mag in mags:
        print(mag)

run();