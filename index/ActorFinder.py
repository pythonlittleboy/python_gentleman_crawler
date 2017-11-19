from index import HtmlIO, ActorDAO
from pyquery import PyQuery as pq
import index.HtmlIO as htmlIO


cache = False

def findActors():
    html = HtmlIO.readHtml("find", "http://nanrenvip.net/find.html", cache)
    
    if not html or len(html) < 100:
        raise Exception("wrong actors page content")
    
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
        href = el.attr("href")

        if href.rfind("/") > -1:
            one["short_name"] = href[0:href.rfind("/")]
        else:
            one["short_name"] = href

        one["name"] = el.text()
        one["url"] = "http://www.nh87.cn/" + href

        actors.append(one)

    return actors


#print(findActors());