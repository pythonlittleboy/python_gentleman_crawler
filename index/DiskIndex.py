import os
import index.MovieDAO as movieDAO
from pprint import pprint
from index import SysConst
import shutil

def getAllMovies(path):
    movieTypes = set(["avi", "mp4", "mkv", "rmvb", "wmv", "txt"])
    results = []
    for fpath, dirs, fs in os.walk(path):
        for filename in fs:
            fullpath = os.path.join(fpath, filename)
            suffix = filename[-3:]
            if filename[0:1] != "." and len(filename) > 4 and suffix in movieTypes:
                # print(fullpath + " | " + filename)
                result = {"fullpath": fullpath, "filename": filename}
                results.append(result)

    return results


def getAllImages(path):
    movieTypes = set(["jpg"])
    results = []
    for fpath, dirs, fs in os.walk(path):
        for filename in fs:
            fullpath = os.path.join(fpath, filename)
            suffix = filename[-3:]
            if filename[0:1] != "." and len(filename) > 4 and suffix in movieTypes:
                # print(fullpath + " | " + filename)
                result = {"fullpath": fullpath, "filename": filename}
                results.append(result)

    return results


def getMovies(path):
    movieTypes = set(["avi", "mp4", "mkv", "rmvb", "wmv"])
    results = []
    for fpath, dirs, fs in os.walk(path):
        for filename in fs:
            fullpath = os.path.join(fpath, filename)
            suffix = filename[-3:]
            if filename[0:1] != "." and len(filename) > 4 and suffix in movieTypes:
                # print(fullpath + " | " + filename)
                result = {"fullpath": fullpath, "filename": filename}
                results.append(result)

    return results


def getTxts(path):
    movieTypes = set(["txt"])
    results = []
    for fpath, dirs, fs in os.walk(path):
        for filename in fs:
            fullpath = os.path.join(fpath, filename)
            suffix = filename[-3:]
            if filename[0:1] != "." and len(filename) > 4 and suffix in movieTypes:
                # print(fullpath + " | " + filename)
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


def deleteSmallImages(path):
    allImages = getAllImages(path)
    for image in allImages:
        size = os.path.getsize(image["fullpath"])
        if size < 5000:
            print("delete " + image["fullpath"])
            os.remove(image["fullpath"])


def copyImageToTemp(movieNumbers):
    if not os.path.exists(SysConst.getImageTempPath()):
        os.mkdir(SysConst.getImageTempPath())

    allImages = getAllImages(SysConst.getImageCachePath())
    for num in movieNumbers:
        for image in allImages:
            if num in image["fullpath"]:
                shutil.copy(image["fullpath"], SysConst.getImageTempPath() + image["filename"])
                break;

def copyOneImageToTemp(actor, avNumber):
    if not os.path.exists(SysConst.getImageTempPath()):
        os.mkdir(SysConst.getImageTempPath())

    source = SysConst.getImageCachePath() + actor + "//" + avNumber + ".jpg"
    to = SysConst.getImageTempPath() + avNumber + ".jpg"
    shutil.copy(source, to)

# avList = [{"av_number": "ABS-072"}]
# pprint(findLocalMovies(avList=avList, path="G://Game//File//"))

#deleteSmallImages(SysConst.getImageCachePath())
#copyImageToTemp(["ABS-072"])
#copyOneImageToTemp("阿部乃美久", "ARMG-274")