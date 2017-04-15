# encoding:UTF-8
import urllib.request
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq

def getAvNumberPic(html):
    #print("begin to read: " + url);

    #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
    #                         'Chrome/51.0.2704.63 Safari/537.36'}
    #req = urllib.request.Request(url=url, headers=headers)
    #res = urllib.request.urlopen(req)
    #html = res.read()
    #html = html.encode("utf-8")
    #html = urllib.request.urlopen(url).read()
    #print(html);

    content = pq(html).find("div.asdrt span.list_text a").text();
    content = content.split(" ")

    publictimes = pq(html).find("div.asdrt span.list_text div.good").text()
    publictimes = publictimes.split(" ")

    images = pq(html).find("div.asdrt span.list_img a img")
    #print(images);
    #images = images.split(" ");
    pics= [];
    for image in images:
        pics.append("http://www.nh87.cn" + pq(image).attr("data-original"))

    i = 0
    results = []
    while i < len(content):
        one = {}
        one["av_number"] = content[i]
        one["remote_cover"] = pics[i]

        if len(publictimes) > i:
            one["public_time"] = publictimes[i]

        results.append(one)
        i += 1

    return results

# print(getAvNumberPic("http://www.nh87.cn/guchuanyizhi/"));