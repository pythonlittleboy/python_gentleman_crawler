# encoding:UTF-8
from pyquery import PyQuery as pq
import index.HtmlIO as htmlIO


def getAvNumberPic(html):
    content = pq(html).find("div.asdrt span.list_text a");
    content = getTexts(content)

    publictimes = pq(html).find("div.asdrt span.list_text div.good")
    publictimes = getTexts(publictimes)

    titles = pq(html).find("div.asdrt span.list_text strong")
    titles = getTexts(titles)

    images = pq(html).find("div.asdrt span.list_img a img")
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

        if len(titles) > i:
            one["title"] = titles[i]

        results.append(one)
        i += 1

    return results

def getTexts(elements):
    texts = []
    for el in elements:
        texts.append(pq(el).text())
    return texts

#html = htmlIO.readHtml("三上悠亚", "http://www.nh87.cn/sanshangyouya/", True)
#print(getAvNumberPic(html));