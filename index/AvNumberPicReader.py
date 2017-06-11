# encoding:UTF-8
from pyquery import PyQuery as pq
import index.HtmlIO as htmlIO


def getAvNumberPic(html):
    #print(html)
    content = pq(html).find("div.asdrt .list_text a b");
    content = getTexts(content)

    publictimes = pq(html).find("div.asdrt .list_text date")
    publictimes = getTexts(publictimes)

    titles = pq(html).find("div.asdrt .list_text p")
    titles = getTexts(titles)

    images = pq(html).find("div.asdrt .list_img a img")
    pics= [];
    for image in images:
        #pic = "http://www.nh87.cn" + pq(image).attr("data-original")
        pic = pq(image).attr("data-original")

        if not pic.startswith("http://imgs.nh87.cn"):
            pic = "http://imgs.nh87.cn" + pic

        pic = pic.replace("small-", "")
        pic = pic.replace("-small", "")
        pics.append(pic)

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

        #print(one)
        results.append(one)
        i += 1

    return results

def getTexts(elements):
    texts = []
    for el in elements:
        texts.append(pq(el).text())
    return texts

#html = htmlIO.readHtml("三上悠亚", "http://www.nh87.cn/sanshangyouya/", False)
#print(getAvNumberPic(html));