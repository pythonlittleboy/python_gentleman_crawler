from index import SysConst
from index import DiskIndex
from index import MovieDAO

import codecs

def saveVRTraining():
    movies = MovieDAO.getMoviesByCondition("vr = 1")
    path = SysConst.getVRTrainDataPath() + "pos//"

    saveFiles(path, movies)

    movies = MovieDAO.getMoviesByCondition("vr = 0")
    path = SysConst.getVRTrainDataPath() + "neg//"

    saveFiles(path, movies)

def saveFiles(path, movies):
    for movie in movies:
        filePath = path + movie["av_number"] + ".txt"
        file = codecs.open(filePath, "w", "utf-8")
        file.write(movie["title"])
        file.close()

saveVRTraining()