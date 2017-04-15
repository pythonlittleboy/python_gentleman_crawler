# encoding:UTF-8
import urllib.request
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq

def getAvNumberPic(url):
    print("begin to read: " + url);
    html = urllib.request.urlopen(url).read()
    #print(html);

    content = pq(html).find("div.asdrt span.list_text a").text();
    content = content.split(" ");

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
        one["name"] = content[i]
        one["img"] = pics[i]
        results.append(one)
        i += 1

    return results

#print(getAvNumberPic("http://www.nh87.cn/guchuanyizhi/"));