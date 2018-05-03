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

def readMagnet(avNumber):

    url = "http://www.cilipig.com/word/" + avNumber + ".html"
    print("begin to read: " + url);

    html = urllib.request.urlopen(url).read()
    #print(html)

    content = pq(html).find("div.search-item")

    if len(content) == 0:
        print("nothing to be found: " + url)
        return ""

    resultList = []
    #print(content)
    for el in content:
        el = pq(el)
        #print(el)
        href = el.find("div.item-bar a").eq(0).attr("href")
        #print(href)
        size = el.find("b.yellow-pill").text()
        size = convertToNumber(size)

        resultList.append((href, size))

    resultList.sort(key=lambda item: item[1], reverse=True)
    #print(resultList[0])
    return resultList[0][0]