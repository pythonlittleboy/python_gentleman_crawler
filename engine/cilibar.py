from pyquery import PyQuery as pq
import urllib


def convertToNumber(num):
    result = 0
    if num.lower().endswith("gb"):
        result = float(num[:-2]) * 1024 * 1024
    elif num.lower().endswith("mb"):
        result = float(num[:-2]) * 1024
    elif num.lower().endswith("kb"):
        result = float(num[:-2])
    return result


# http://www.ciliba.org/detail/c1a1d8ee4ce6c26d858a72ca0a77956a60f6eff3.html
def getMagnet(url):
    first = "http://www.ciliba.org/detail/"
    last = ".html"
    return "magnet:?xt=urn:btih:" + url[len(first):-len(last)]


def readMagnet(avNumber):
    url = "http://www.ciliba.org/s/" + avNumber + ".html"
    print("begin to read: " + url);

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/51.0.2704.63 Safari/537.36'}
    req = urllib.request.Request(url=url, headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read()
    res.close()

    content = pq(html).find("div.search-item")

    if len(content) == 0:
        print("nothing to be found: " + url)
        return ""

    resultList = []
    #print(content)
    for el in content:
        el = pq(el)
        # print(el)
        href = el.find("div.item-title a").eq(0).attr("href")
        # print(href)
        size = el.find("b.yellow-pill").text()
        size = convertToNumber(size)

        magnet = getMagnet(href)
        resultList.append((magnet, size))

    resultList.sort(key=lambda item: item[1], reverse=True)
    # print(resultList[0][0])
    return resultList[0][0]
