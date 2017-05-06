from engine import cilipig as cilipig
from engine import cilibar as cilibar
from engine import clpig as clpig

engine = clpig

# 打开文件
fo = open("numbers.txt", "r")
print("文件名为: ", fo.name)

result = []
try:
    for line in fo:
        num = line.strip()
        mag = engine.readMagnet(num)
        print(mag)
        if len(mag) > 10:
            result.append(mag)
finally:
    fo.close()

for mag in result:
    print(mag)
