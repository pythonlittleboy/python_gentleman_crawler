import os
import urllib.request
import codecs
import util.httpfetch2
import time
from index import SysConst

def readHtml(name, url, cache):
    #filePath = "D://MyDrivers//cache//html//" + name + ".html"
    filePath = SysConst.getHtmlCachePath(name + ".html")

    if cache and os.path.exists(filePath):
        file = codecs.open(filePath, "r+", "utf-8")
        #file = open(filePath,'r+')
        html = file.read()
        file.close()
        return html

    #time.sleep(1)
    html = util.httpfetch2.getHtml(url)
    #print(html)
    #html = str(html).decode('utf8')
    #html = str(html, encoding="utf-8")

    if not html:
        raise Exception("can not get html content: " + name + ".html")

    fo = codecs.open(filePath, "w+", "utf-8")
    #fo = open(filePath,'w+')
    fo.write(html)
    fo.close()

    return html

#print(indexActor(url="http://www.nh87.cn/guchuanyizhi/", actor="古川伊织", cache=False, files=allFiles))
#readHtml("古川伊织", "http://www.nh87.cn/guchuanyizhi/", False)
#filePath = "D://MyDrivers//cache//html//古川伊织.html"
#file = codecs.open(filePath,'r+','utf-8')
#file = open(filePath, 'r+')
#html = file.read()
#file.close()
#print(html)