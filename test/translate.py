
import goslate

import urllib.request  
proxy_handler = urllib.request.ProxyHandler({'http':'localhost:58570'})  
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()  
#proxy_auth_handler.add_password('realm', '123.123.2123.123', 'user', 'password')  
opener = urllib.request.build_opener(urllib.request.HTTPHandler, proxy_handler)  

gs_with_proxy = goslate.Goslate(opener=opener)
translation = gs_with_proxy.translate("hello world", "de")