
import os
import urllib.request
import util.httpfetch as httpfetch

# D:\MyDrivers\images\古川伊织

"""
import socket  
import time  
timeout = 20    
socket.setdefaulttimeout(timeout) #这里对整个socket层设置超时时间。后续文件中如果再使用到socket，不必再设置  
sleep_download_time = 10  
time.sleep(sleep_download_time) #这里时间自己设定  
request = urllib.request.urlopen(url)#这里是要读取内容的url  
content = request.read()#读取，一般会在这里报异常  
request.close()#记得要关闭  
"""

def getFilePath(actor, avNumber):
    return "d://MyDrivers//cache//images//" + actor + "//" + avNumber + ".jpg"

def checkFile(filePath):
    return os.path.exists(filePath)

def saveFileByRequest(url, filePath):
    """
    timeout = 20
    socket.setdefaulttimeout(timeout)

    sleep_download_time = 10
    time.sleep(sleep_download_time)

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    req = urllib.request.Request(url=url, headers=headers)
    res = urllib.request.urlopen(req)
    img = res.read()
    res.close()
    """
    img = httpfetch.get(url)
    file = open(filePath, "wb")
    file.write(img)
    file.close();

def saveFileByURL(url, filePath):
    urllib.request.urlretrieve(url, filePath)

def saveFile(url, filePath):
    saveFileByURL(url, filePath)

def saveImage(av):
    actor = av["actor"]
    avNumber = av["av_number"]
    url = av["remote_cover"]
    filePath = getFilePath(actor, avNumber)

    if not(checkFile(filePath)):
        saveFile(url, filePath)
        print ("save file: " + filePath)

# print(checkFile("古川伊织", "test"))
# print(checkFile("古川伊织", "test2"))
# av = {'av_number': 'STAR-758', 'remote_cover': 'http://www.nh87.cn/uploads/1702/1star758pl.jpg', 'public_time': '2017-03-02', 'actor': '古川伊织'}
av = {'av_number': 'STAR-425', 'remote_cover': 'http://www.nh87.cn/uploads/allimg/1512/1star00425pl.jpg', 'public_time': '2013-04-11', 'actor': '古川伊织'}
saveImage(av)