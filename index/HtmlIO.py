import os
import urllib.request
import codecs

def readHtml(name, url, cache):
    filePath = "D://MyDrivers//cache//html//" + name + ".html"

    if cache and os.path.exists(filePath):
        #file = open(filePath, "w", "utf-8")
        file = codecs.open(filePath,'r+','utf-8')
        html = file.read()
        file.close()
        return html

    #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
    #                         'Chrome/51.0.2704.63 Safari/537.36'}
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2526.80 Safari/537.36'}
    req = urllib.request.Request(url=url, headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read()
    req.close()

    #fo = open(filePath, "wb", "utf-8")
    fo = codecs.open(filePath,'w','utf-8')
    fo.write(html)
    fo.close()

    return