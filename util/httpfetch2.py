# coding=utf-8

import requests
import time
from util import Log

COOKIE = "yeuauecookieclassrecord=%2C641%2C161%2C; Hm_lvt_3c484b51b01288268c9a10f4c7f31cdf=1506607357,1506942334,1507017860,1507346769; Hm_lpvt_3c484b51b01288268c9a10f4c7f31cdf=1507347300"

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
        'Host': 'nanrenvip.net',
        'Cache-Control': 'no-cache',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Referer': 'http://www.nh87.cn/jingxiangjulia/',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Pragma': 'no-cache',
        #'Cookie': COOKIE
    }

    errorCount = 0

    while True:
        try:
            if errorCount is 2:
                return None
            time.sleep(2)
            r = requests.get(url, headers=headers, timeout=60)
            r.encoding = 'utf-8'
            return r.text
        except Exception as err:
            errorCount = errorCount + 1
            time.sleep(10)
            #print(err)
            Log.exception(err)




def getImage(url):
    headers = {
        #'Host': 'img1.chaomabaida.com',
        'Cache-Control': 'max-age=0',
        'Accept': 'image/webp,image/*,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 115Browser/7.1.0',
        'Referer': 'http://www.nh87.cn/jingxiangjulia/',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        #'Cookie': COOKIE
    }

    errorCount = 0

    while True:
        try:
            time.sleep(4)
            if errorCount is 2:
                return None
            r = requests.get(url, headers=headers, timeout=60)
            return r.content
        except Exception as err:
            errorCount = errorCount + 1
            #print(err)
            Log.exception(err)


def getHtml2(url):
    headers = {
        'Cache-Control': 'no-cache',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Pragma': 'no-cache'
    }

    errorCount = 0

    while True:
        try:
            if errorCount is 2:
                return None
            time.sleep(2)
            r = requests.get(url, headers=headers, timeout=60)
            r.encoding = 'utf-8'
            return r.text
        except Exception as err:
            errorCount = errorCount + 1
            time.sleep(10)
            #print(err)
            Log.exception(err)