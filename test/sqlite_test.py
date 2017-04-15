import sqlite3
import time
import random

conn = sqlite3.connect('../db/database.db')
print("Opened database successfully");

cursor = conn.cursor()
now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
av_number = "test" + str(round(random.randint(1, 5000000)))
# cursor.execute("insert into people values (?, ?)", (who, age))
cursor.execute("insert into t_movies (av_number, actor, remote_cover, create_time) values (?, ?, ?, ?)", [av_number, "a2", "a3", now])
conn.commit()

cursor2 = conn.cursor()
sql = "SELECT * from t_movies where av_number = '" + av_number + "'"
print(sql)
cursor3 = cursor2.execute("SELECT * from t_movies where av_number=?", [av_number])

#cursor = conn.execute(sql)
print (cursor3.fetchall());

conn.close()