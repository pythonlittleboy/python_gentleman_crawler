
import os
import urllib.request
import util.httpfetch2 as httpfetch2
from index import SysConst

# SysConst.getImageCachePath()/古川伊织

def getFilePath(actor, avNumber):
    return SysConst.getImageCachePath() + actor + "//" + avNumber + ".jpg"


def checkDirPath(actor):
    path = SysConst.getImageCachePath() + actor;
    exist = os.path.exists(path)
    if not exist:
        os.mkdir(path)

def checkFile(filePath):
    return os.path.exists(filePath)

def saveFileByRequest(url, filePath):
    img = httpfetch2.getImage(url)
    file = open(filePath, "wb")
    file.write(img)
    file.close();

def saveFileByURL(url, filePath):
    urllib.request.urlretrieve(url, filePath)

def saveFile(url, filePath):
    saveFileByRequest(url, filePath)

def saveImage(av):
    actor = av["actor"]
    avNumber = av["av_number"]
    url = av["remote_cover"]
    url = url.replace("www.nh87.cn", "imgs.nh87.cn")
    filePath = getFilePath(actor, avNumber)

    if not(checkFile(filePath)):
        print("begin save file: " + filePath)
        print(url)
        saveFile(url, filePath)
        return True
    else:
        return False

#av = {'av_number': 'IPZ-976', 'remote_cover': 'http://www.nh87.cn/uploads/2017/06/ipz976pl.jpg', 'actor': '樱空桃'}
#saveImage(av)
#checkDirPath("ABC")