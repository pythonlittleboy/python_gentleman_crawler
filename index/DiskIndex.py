import os
import index.MovieDAO as movieDAO
from pprint import pprint

def getAllMovies(path):
    movieTypes = set(["avi", "mp4", "mkv", "rmvb", "wmv", "txt"])
    results = []
    for fpath, dirs, fs in os.walk(path):
        for filename in fs:
            fullpath = os.path.join(fpath, filename)
            suffix = filename[-3:]
            if filename[0:1] != "." and len(filename) > 4 and suffix in movieTypes:
                #print(fullpath + " | " + filename)
                result = {"fullpath": fullpath, "filename": filename}
                results.append(result)

    return results

def findLocalMovies(avList, allFiles):
    # allFiles = getAllMovies(path)

    for av in avList:
        avNumber = av["av_number"].lower()
        for file in allFiles:
            filename = file["filename"]
            if filename.lower().find(avNumber) > -1:
                av["local_movie"] = file["fullpath"]
                break;

    return avList



#avList = [{"av_number": "ABS-072"}]
#pprint(findLocalMovies(avList=avList, path="G://Game//File//"))