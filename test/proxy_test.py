import requests

if __name__ == '__main__':
    proxies = {"http": "http://127.0.0.1:51551", "https": "http://127.0.0.1:51551"}
    headers = {
        'Cache-Control': 'no-cache',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Pragma': 'no-cache',
    }

    r = requests.get("https://onejav.com/", headers=headers, proxies=proxies, timeout=60)
    r.encoding = 'utf-8'
    print(r.text)