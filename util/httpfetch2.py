import requests

COOKIE = "Hm_lvt_f55674d4367f95a13931a2de921dd8ac=1485677791,1487860982; UM_distinctid=15b67a3852fc5-058bdcee22d39a-514f291e-1fa400-15b67a38530251; Hm_lvt_196c24ae350e0996212996390aed04b2=1492091697,1492224007,1492433852,1492869286; CNZZDATA1261666818=121300809-1492087598-%7C1494511103; tjfwkey=72082o; Hm_lvt_4fc8c6a8a6a361779e76a82b679b3960=1494249267,1494509188,1495343829,1495808475; Hm_lpvt_4fc8c6a8a6a361779e76a82b679b3960=1495808475; __dsje_cpv_r_4936_cpv_plan_ids=%7C406%7C"

def getHtml(url):
    """
Cache-Control:max-age=0
Connection:keep-alive
Cookie:Hm_lvt_f55674d4367f95a13931a2de921dd8ac=1485677791,1487860982; UM_distinctid=15b67a3852fc5-058bdcee22d39a-514f291e-1fa400-15b67a38530251; CNZZDATA1261666818=121300809-1492087598-%7C1492087598; Hm_lvt_4fc8c6a8a6a361779e76a82b679b3960=1490791932,1490793243,1492091936,1492238050; ACode=d05a006e; Hm_lvt_196c24ae350e0996212996390aed04b2=1490788668,1492091697,1492224007,1492433852; Hm_lpvt_196c24ae350e0996212996390aed04b2=1492433852
If-Modified-Since:Thu, 23 Mar 2017 07:36:21 GMT
If-None-Match:W/"58d37af5-8d5d"
Upgrade-Insecure-Requests:1
    """
    headers = {
        'Host': 'www.nh87.cn',
        'Cache-Control': 'max-age=0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 115Browser/7.1.0',
        'Referer': 'http://www.nh87.cn/jingxiangjulia/',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cookie': COOKIE
    }
    r = requests.get(url, headers=headers, timeout = 500)
    r.encoding = 'utf-8'
    return r.text


def getImage(url):
    headers = {
        'Host': 'www.nh87.cn',
        'Cache-Control': 'max-age=0',
        'Accept': 'image/webp,image/*,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 115Browser/7.1.0',
        'Referer': 'http://www.nh87.cn/jingxiangjulia/',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cookie': COOKIE
    }
    r = requests.get(url, headers=headers)
    return r.content

