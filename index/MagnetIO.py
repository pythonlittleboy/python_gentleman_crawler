from engine import cilipig as cilipig
from engine import cilibar as cilibar
from engine import clpig as clpig
from index import DiskIndex
from index import SysConst
from index import MovieDAO
from index import WrongMagnetDAO
from util import Log

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
    Log.info("download magnets begins")
    movies = MovieDAO.getNoMagnetMovies()
    mags = []
    try:
        for movie in movies:
            mag = getMagnet(movie["av_number"], None)
            if mag:
                Log.info(mag)
                MovieDAO.updateMovieMagnet2(movie["av_number"], mag)
                mags.append(mag)
                if len(mags) >= 20:
                    break
            else:
                MovieDAO.updateMovieLastReadTime(movie["av_number"])
            
    except Exception as err:
        Log.exception(err)
    finally:
        for mag in mags:
            Log.info(mag)

    Log.info("download magnets end")
    return mags


def getUndownloadMagnets():
    #images = DiskIndex.getAllImages(SysConst.getImageTempPath())
    conn = SysConst.getConnect()
    movies = MovieDAO.getMoviesByCondition("local = 2 and download = 0 and magnet is not null and (read != 1 or read is null) order by create_time limit 20")
    for movie in movies:
        print(movie["magnet"])
        MovieDAO.updateMovieReaded(movie["av_number"], conn)
    
    conn.commit()
    conn.close()



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


def copyWrongMagnets():
    movies = MovieDAO.getMoviesByCondition("local = 2 and download = 0 and magnet is not null")

    conn = SysConst.getConnect()
    try:
        for movie in movies:
            WrongMagnetDAO.saveMagnet(movie, conn)
    except Exception as err:
        print(err)
    finally:
        conn.commit()
        conn.close()