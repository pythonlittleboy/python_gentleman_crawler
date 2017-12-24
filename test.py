from util import httpfetch2


if __name__ =='__main__':
    html = httpfetch2.getHtml("http://nanrenvip.co/find.html")
    print(html)