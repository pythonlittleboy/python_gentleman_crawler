from pyquery import PyQuery as pq
from lxml import etree
import urllib

def convertToNumber(num):
    result = 0
    if num.endswith("GB"):
        result = float(num[:-2]) * 1024 * 1024
    elif num.endswith("MB"):
        result = float(num[:-2]) * 1024
    elif num.endswith("B"):
        result = float(num[:-2])
    return result


def read():
    html = urllib.request.urlopen("http://www.clpig.org/torrent/ABP-572.html").read()
    content = pq(html).find("div.btsowlist div.row")

    if content.length == 0:
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
    # print(resultList)
    return resultList[0][0]


read()