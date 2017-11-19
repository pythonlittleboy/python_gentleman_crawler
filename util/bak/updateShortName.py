#print("abc.jpg"[0:-4])
from index import SysConst

"""
str1 = "http://www.nh87.cn/shanbenhuilixiang"
str2 = "shanbenhuilixiang"
if str2.rfind("/") > -1:
    print(str2[0:str2.rfind("/")])
else:
    print(str2)



print(substr1("http://www.nh87.cn/shanbenhuilixiang"))
print(substr1("http://www.nh87.cn/shanbenhuilixiang/"))

"""

def substr1(str1):
    if str1.rfind("/") == (len(str1) - 1):
        last2 = str1.rfind("/", 0, str1.rfind("/")) + 1
        return str1[last2:-1]

    return str1[(str1.rfind("/")+1):]

def updateShortName():
    conn = SysConst.getConnect()
    # print(yesterday)
    cursor = conn.execute("SELECT name, url from t_actors", [])
    results = []
    for row in cursor:
        one = {"name": row[0], "url": row[1]}
        results.append(one)

    cursor = conn.cursor()

    for row in results:
        shortName = substr1(row["url"])
        print(shortName)
        cursor.execute(
            "update t_actors set short_name = ? where name = ?",
            [shortName, row["name"]])
    conn.commit()
    conn.close()
    
if __name__ =='__main__':
    updateShortName()