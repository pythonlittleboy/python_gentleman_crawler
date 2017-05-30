import index.MagnetIO as magnetIO
from ml import PredictByImage
from ml import Forcast
from index import DiskIndex

def recommenderByTitle():
    movies = Forcast.forcastToNumbers()
    print(movies)
    DiskIndex.copyImageToTemp(movies)
    """
    if findMag:
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
    """

def recommenderByImage():
    movies = PredictByImage.predict()
    print(movies)
    DiskIndex.copyImageToTemp(movies)


#recommenderByTitle()
recommenderByImage()
#magnetIO.getMagnetFromTemp()
