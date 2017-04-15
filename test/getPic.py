import urllib.request

pic_link = "http://images2015.cnblogs.com/news/24442/201703/24442-20170331214657258-1483842641.png"  #图片链接

urllib.request.urlretrieve(pic_link, "d://MyPhotos//test.png")