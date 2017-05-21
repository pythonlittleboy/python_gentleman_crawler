import index.IndexActor as indexActor
import index.DiskIndex as diskIndex
import index.MagnetIO as magnetIO
import index.ActorDAO as ActorDAO
from ml import Forcast

def findMagnetsByRecommender():
    movies = Forcast.forcastToNumbers()
    print(movies)

    mags = []
    try:
        for movie in movies:
            mag = magnetIO.getMagnet(movie)
            if mag:
                mags.append(mag)
                print(mag)
    except(Exception):
        print(str(Exception))
    finally:
        for mag in mags:
            print(mag)


findMagnetsByRecommender()
