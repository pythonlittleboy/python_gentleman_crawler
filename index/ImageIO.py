
import os
import urllib.request
import util.httpfetch2 as httpfetch2

# D:\MyDrivers\cache\images\古川伊织

def getFilePath(actor, avNumber):
    return "d://MyDrivers//cache//images//" + actor + "//" + avNumber + ".jpg"

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
    filePath = getFilePath(actor, avNumber)

    if not(checkFile(filePath)):
        print("begin save file: " + filePath)
        saveFile(url, filePath)

#av = {'av_number': 'SNIS-872', 'remote_cover': 'http://www.nh87.cn/uploads/1702/snis872pl-lp.jpg', 'actor': '三上悠亚'}
#saveImage(av)