import os
import urllib.request

def readHtml(name, url, cache):
    filePath = "D://MyDrivers//cache//html//" + name + ".html"

    if cache and os.path.exists(filePath):
        file = open(filePath)
        html = file.read()
        file.close()
        return html

    #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
    #                         'Chrome/51.0.2704.63 Safari/537.36'}
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    req = urllib.request.Request(url=url, headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read()

    fo = open(filePath, "wb")
    fo.write(html)
    fo.close()

    return