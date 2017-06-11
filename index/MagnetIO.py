from engine import cilipig as cilipig
from engine import cilibar as cilibar
from engine import clpig as clpig
from index import DiskIndex
from index import SysConst

def getMagnet(avNumber):
    engine = clpig
    mag = engine.readMagnet(avNumber)
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

#getMagnetFromTemp()