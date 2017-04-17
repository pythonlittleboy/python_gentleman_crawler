from pyquery import PyQuery as pq
import urllib
import time
import random

def convertToNumber(num):
    result = 0
    if num.endswith("GB"):
        result = float(num[:-2]) * 1024 * 1024
    elif num.endswith("MB"):
        result = float(num[:-2]) * 1024
    elif num.endswith("B"):
        result = float(num[:-2])
    return result

def getMagnet(url):
    #<a target="_blank" href="http://www.cilizhuzhu.com/magnet/256818E93C1ED71B16F2D6148F070907DD77BF75.html" title="ABP-418">
    first = "http://www.cilizhuzhu.com/magnet/"
    last = ".html"
    return "magnet:?xt=urn:btih:" + url[len(first):-len(last)]


def readMagnet(avNumber):

    url = "http://www.clpig.org/torrent/"+avNumber+".html"
    print("begin to read: " + url);

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/51.0.2704.63 Safari/537.36'}
    req = urllib.request.Request(url=url, headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read()
    res.close()

    #html = urllib.request.urlopen(url).read()

    content = pq(html).find("div.btsowlist div.row")

    if len(content) == 0:
        print("nothing to be found: " + url)
        return ""

    resultList = []
    # print(content)
    for el in content:
        el = pq(el);
        # print(el)
        href = el.find("a").attr("href")
        size = el.find("div.col-lg-1").text()
        size = convertToNumber(size)

        resultList.append((href, size))

    resultList.sort(key=lambda item: item[1], reverse=True)
    # print(resultList[0][0])
    return getMagnet(resultList[0][0])