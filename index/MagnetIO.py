from engine import cilipig as cilipig
from engine import cilibar as cilibar
from engine import clpig as clpig
from index import DiskIndex
from index import SysConst
from index import MovieDAO


def getMagnet(avNumber, skipMagnet):
    engine = clpig
    mag = engine.readMagnet(avNumber, skipMagnet)
    if len(mag) > 10:
        return mag
    else:
        return None


def getMagnetFromTemp():
    images = DiskIndex.getAllImages(SysConst.getImageTempPath())
    mags = []
    try:
        for image in images:
            mag = getMagnet(image["filename"][0:-4])
            if mag:
                print(mag)
                mags.append(mag)
    except Exception as err:
        print(err)
    finally:
        for mag in mags:
            print(mag)

    return mags


def getMagnetFromDB():
    #images = DiskIndex.getAllImages(SysConst.getImageTempPath())
    movies = MovieDAO.getMoviesByCondition("local = 2 and magnet is null")
    mags = []
    try:
        for movie in movies:
            mag = getMagnet(movie["av_number"], None)
            if mag:
                print(mag)
                MovieDAO.updateMovieMagnet2(movie["av_number"], mag)
                mags.append(mag)
                if len(mags) > 30:
                    break;
    except Exception as err:
        print(err)
    finally:
        for mag in mags:
            print(mag)

    return mags


def getUndownloadMagnets():
    #images = DiskIndex.getAllImages(SysConst.getImageTempPath())
    movies = MovieDAO.getMoviesByCondition("local = 2 and magnet is not null")
    for movie in movies:
        print(movie["magnet"])


def reloadErrorMagnets():
    movies = MovieDAO.getMoviesByCondition("local = 2 and magnet is not null")
    mags = []
    try:
        for movie in movies:
            mag = getMagnet(movie["av_number"], movie["magnet"])
            if mag:
                print(mag)
                MovieDAO.updateMovieMagnet2(movie["av_number"], mag)
                mags.append(mag)
    except Exception as err:
        print(err)
    finally:
        for mag in mags:
            print(mag)

    return mags