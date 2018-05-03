import index.MagnetIO as magnetIO
from engine import clpig as clpig

#magnetIO.getMagnetFromDB()
magnetIO.getUndownloadMagnets()

# 拷贝当前没有下载的magnet到t_wrong_magnets
#magnetIO.copyWrongMagnets()

# 测试代码
#print(clpig.readMagnet("RCTD-035", ""))