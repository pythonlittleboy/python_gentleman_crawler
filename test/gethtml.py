# encoding:UTF-8
import urllib.request

#url = "http://www.ciliba.org/s/MDB-741.html"
url = "http://www.clpig.org/torrent/MDB-742.html"
print("begin to read: " + url);

headers2 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
        'Accept':'text/html;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'gzip',
        'Connection': 'close',
        'Host':'www.ciliba.org',
        'Referer': None  # 注意如果依然不能抓取的话，这里可以设置抓取网站的host
}

#opener = urllib.request.build_opener()
#html = urllib.request.urlopen(url).read()
#opener.addheaders = headers
#data = opener.open(url).read()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '  
                        'Chrome/51.0.2704.63 Safari/537.36'}
req = urllib.request.Request(url=url, headers=headers)
res = urllib.request.urlopen(req)
data = res.read()

print(data)