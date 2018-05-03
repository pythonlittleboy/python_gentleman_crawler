from pyquery import PyQuery as pq
import urllib
import time
import random
from util import httpfetch2
from index import WrongMagnetDAO
from util import Log

def convertToNumber(num):
    try:
        num = num.replace(",", "").upper()

        result = 1
        if num.endswith("GB"):
            result = float(num[:-2]) * 1024 * 1024
        elif num.endswith("MB"):
            result = float(num[:-2]) * 1024
        elif num.endswith("KB"):
            result = float(num[:-2]) * 1024
        elif num.endswith("B"):
            result = float(num[:-2])

        #print(str(num) + " " + str(result))
    except BaseException:
        result = 1
    
    return result
    

def getMagnet(url):
    #<a target="_blank" href="http://www.cilizhuzhu.com/magnet/256818E93C1ED71B16F2D6148F070907DD77BF75.html" title="ABP-418">
    #first = "http://www.cilizhuzhu.com/magnet/"
    first = "http://www.cilizhu2.com/magnet/"
    last = ".html"
    return "magnet:?xt=urn:btih:" + url[len(first):-len(last)]


def readMagnet(avNumber, skipMagnet):
    #sleep_download_time = 10
    #time.sleep(sleep_download_time)

    #url = "http://www.clpig.org/torrent/"+avNumber+".html"
    #url = "http://www.cilizhuzhu.org/torrent/" + avNumber + ".html"
    url = "http://www.cilizhu2.com/torrent/" + avNumber + ".html"
    Log.info("begin to read: " + url)

    '''
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/51.0.2704.63 Safari/537.36'}
    req = urllib.request.Request(url=url, headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read()
    res.close()
    #html = urllib.request.urlopen(url).read()
    '''

    html = httpfetch2.getHtml2(url)

    content = pq(html).find("div.btsowlist div.row")

    if len(content) == 0:
        Log.info("nothing to be found: " + url)
        return ""

    wrongMagnets = WrongMagnetDAO.findWrongMagnets(avNumber)

    resultList = []
    specialTitles = ["Thz.la"]
    foundSpecial = False
    specialHref = ""
    #print(content)
    for el in content:
        el = pq(el)
        #print(el)
        href = el.find("a").attr("href")
        title = el.find("a").attr("title")
        #print(href, title)

        if not href:
            break

        magnet = getMagnet(href)
        if magnet in wrongMagnets:
            continue

        for specialTitle in specialTitles:
            if specialTitle in title:
                foundSpecial = True
                specialHref = href

        if not foundSpecial:
            size = el.find("div.col-lg-1").text()
            sizeNumber = convertToNumber(size)
            resultList.append((href, sizeNumber))


    if len(resultList) == 0:
        Log.info("nothing to be found: " + url)
        return ""

    if foundSpecial:
        return getMagnet(specialHref)
    else:
        resultList.sort(key=lambda item: item[1], reverse=True)
        #print(resultList[0])
        return getMagnet(resultList[0][0])

#print(readMagnet("ipz806"))