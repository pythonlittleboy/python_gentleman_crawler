# /usr/bin/env python
# coding=utf-8

# import httplib
# import md5
import urllib
import io
import random
import urllib.request
import hashlib
from hashlib import md5
import json

import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb2312')  #改变标准输出的默认编码
# print(sys.getdefaultencoding())
# print('\u8266')

def md52(str):
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    # print(m.hexdigest())
    return m.hexdigest()


def md5GBK(str1):
    m = hashlib.md5(str1.encode(encoding='utf-8'))
    return m.hexdigest()
    # return m.hexdigest()


print(md52('hello'))
print(md5GBK('你好'))

appid = '20180412000145467'
secretKey = 'F2ekgIAXYQvZlbWNH0Iu'

# httpClient = None
myurl = '/api/trans/vip/translate'
q = '国民的アイドルいきなり即ハメドッキリ4本番いつでも即合体、どこでも即絶頂三上悠亜'
# q = "你好"
# print(q)
# q = b"\u756a\u3044\u3064\u3067\u3082\u5373\u5408\u4f53\u3001\u3069\u3053\u3067\u3082\u5373\u7d76\u9802\u4e09\u4e0a\u60a0\u4e9c"
# print(q.encode("ascii"))
# q = 'hello'
fromLang = 'jp'
toLang = 'zh'
salt = random.randint(32768, 65536)

str(salt)
print(1)
sign = appid + q + str(salt) + secretKey
print(2)
# m1 = md5.new()
# m1.update(sign)
# sign = m1.hexdigest()

# md5_obj = md5()
# md5_obj.update(sign.encode('utf-8', 'ignore'))
# md5_obj.update(sign.encode(encoding='gb2312'))
sign = md5GBK(sign)

query = {
    'appid': appid,
    'q': q,
    'from': fromLang,
    'to': toLang,
    'salt': str(salt),
    'sign': sign
}

query_str = urllib.parse.urlencode(query)
print(query_str)

# myurl = myurl + '?appid=' + appid + '&q=' + q + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
#     salt) + '&sign=' + sign

myurl += "?" + query_str

print(3)
try:
    url = 'http://api.fanyi.baidu.com' + myurl
    print(url)
    req = urllib.request.Request(url=url)
    print(3.1)
    res = urllib.request.urlopen(req)
    print(3.15)
    data = res.read()
    print(3.2)
    obj = json.loads(data, encoding="utf-8")
    print(4)
    print(obj)
    print(obj["trans_result"][0]["dst"])

    # httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
    # httpClient.request('GET', myurl)
    #
    # # response是HTTPResponse对象
    # response = httpClient.getresponse()
    # print(response.read())
except Exception as e:
    print(e)
