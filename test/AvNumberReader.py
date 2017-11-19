# encoding:UTF-8
import urllib.request
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq

def getAvNumber(url):
    print("begin to read: " + url);
    html = urllib.request.urlopen(url).read()

    content = pq(html).find("div.asdrt span.list_text a").text();
    content = content.split(" ");

    return content