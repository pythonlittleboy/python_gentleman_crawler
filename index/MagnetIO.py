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
    for image in images:
        mags.append(getMagnet(image["filename"][0:-4]))

    return mags


#getMagnetFromTemp()