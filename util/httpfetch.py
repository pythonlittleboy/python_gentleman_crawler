import urllib.request
import socket
import time

def get(url):
    timeout = 20
    socket.setdefaulttimeout(timeout)

    sleep_download_time = 2
    time.sleep(sleep_download_time)

    """
    Host: www.nh87.cn
Connection: keep-alive
Accept: image/webp,image/*,*/*;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 115Browser/7.1.0
Referer: http://www.nh87.cn/jingxiangjulia/
Accept-Encoding: gzip, deflate, sdch
Accept-Language: zh-CN,zh;q=0.8
Cookie: Hm_lvt_f55674d4367f95a13931a2de921dd8ac=1485677791,1487860982; UM_distinctid=15b67a3852fc5-058bdcee22d39a-514f291e-1fa400-15b67a38530251; CNZZDATA1261666818=121300809-1492087598-%7C1492087598; Hm_lvt_196c24ae350e0996212996390aed04b2=1490534460,1490788668,1492091697,1492224007; Hm_lpvt_196c24ae350e0996212996390aed04b2=1492224018; Hm_lvt_4fc8c6a8a6a361779e76a82b679b3960=1490791932,1490793243,1492091936,1492238050; Hm_lpvt_4fc8c6a8a6a361779e76a82b679b3960=
    """

    headers = {
        #'Host': 'www.nh87.cn',
        #'Accept': 'image / webp, image / *, * / *;q = 0.8',
        'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 115Browser/7.1.0',
        #'Referer': 'http://www.nh87.cn/jingxiangjulia/',
        #'Accept-Encoding': 'gzip, deflate, sdch',
        #'Accept-Language': 'zh-CN,zh;q=0.8'
        #'Cookie': 'Hm_lvt_f55674d4367f95a13931a2de921dd8ac=1485677791,1487860982; UM_distinctid=15b67a3852fc5-058bdcee22d39a-514f291e-1fa400-15b67a38530251; CNZZDATA1261666818=121300809-1492087598-%7C1492087598; Hm_lvt_196c24ae350e0996212996390aed04b2=1490534460,1490788668,1492091697,1492224007; Hm_lpvt_196c24ae350e0996212996390aed04b2=1492224018; Hm_lvt_4fc8c6a8a6a361779e76a82b679b3960=1490791932,1490793243,1492091936,1492238050; Hm_lpvt_4fc8c6a8a6a361779e76a82b679b3960='
    }
    
    req = urllib.request.Request(url=url, headers=headers)
    req = urllib.request.urlopen(req)
    html = req.read()
    req.close()

    """
    request = urllib.request.urlopen(url)  # 这里是要读取内容的url
    html = request.read()  # 读取，一般会在这里报异常
    request.close()  # 记得要关闭
    """

    return html