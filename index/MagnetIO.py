from engine import cilipig as cilipig
from engine import cilibar as cilibar
from engine import clpig as clpig

def getMagnet(avNumber):
    engine = clpig
    mag = engine.readMagnet(avNumber)
    if len(mag) > 10:
        return mag
    else:
        return None