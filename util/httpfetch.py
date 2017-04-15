import urllib.request
import socket
import time

def get(url):
    timeout = 20
    socket.setdefaulttimeout(timeout)

    sleep_download_time = 2
    time.sleep(sleep_download_time)

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}

    req = urllib.request.Request(url=url, headers=headers)
    req = urllib.request.urlopen(req)
    html = req.read()
    req.close()
    return html