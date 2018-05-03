# /usr/bin/env python
# coding=utf-8

import random
import urllib.request
import hashlib
import json

from util import Log


def md5_gbk(str1):
    m = hashlib.md5(str1.encode(encoding='utf-8'))
    return m.hexdigest()


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


def jp_to_cn(jpTxt):
    appid = '20180412000145467'
    secretKey = 'F2ekgIAXYQvZlbWNH0Iu'

    myurl = '/api/trans/vip/translate'
    fromLang = 'jp'
    toLang = 'zh'

    salt = random.randint(32768, 65536)
    str(salt)
    sign = appid + jpTxt + str(salt) + secretKey
    sign = md5_gbk(sign)

    query = {
        'appid': appid,
        'q': jpTxt,
        'from': fromLang,
        'to': toLang,
        'salt': str(salt),
        'sign': sign
    }

    query_str = urllib.parse.urlencode(query)
    myurl += "?" + query_str


    url = 'http://api.fanyi.baidu.com' + myurl
    req = urllib.request.Request(url=url)
    res = urllib.request.urlopen(req)
    data = res.read()
    obj = json.loads(to_str(data), encoding="utf-8")
    return obj["trans_result"][0]["dst"]


if __name__ == '__main__':
    print(jp_to_cn('唾液を絡める濃厚接吻セックス 三上悠亜'))
