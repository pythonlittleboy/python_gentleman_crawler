import time

import AvNumberReader;
from engine import cilipig as cilipig
from engine import cilibar as cilibar

# search engine: cilipig clpig cilibar
engine = cilibar
# av idol home page
homePage = "http://www.nh87.cn/xingtianyouzhen/"
# max magnet number
maxNumber = 100

start_time = time.time()
numbers = AvNumberReader.getAvNumber(homePage)

result = []
count = 1;
for num in numbers:
    mag = engine.readMagnet(num)
    if len(mag) > 10:
        count += 1
        result.append(mag)
    if count > maxNumber:
        break

for mag in result:
    if len(mag) > 10:
        print(mag)

print('%d second'% (time.time()-start_time))