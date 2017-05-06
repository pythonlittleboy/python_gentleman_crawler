from index import HtmlIO, ActorDAO
from pyquery import PyQuery as pq
import index.HtmlIO as htmlIO


cache = True

def findActors():
    html = HtmlIO.readHtml("find", "http://www.nh87.cn/find.html", cache)
    actors =  getActors(html)
    newActors = ActorDAO.saveActors(actors)

    return newActors


def getActors(html):
    #print(html)
    actors = [];
    elements = pq(html).find("div.tab-content li a")

    for e in elements:
        el = pq(e)
        one = {}
        one["name"] = el.text()
        one["url"] = "http://www.nh87.cn/" + el.attr("href")
        actors.append(one)

    return actors


#print(findActors());