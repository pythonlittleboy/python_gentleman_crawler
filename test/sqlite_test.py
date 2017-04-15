import sqlite3

conn = sqlite3.connect('../db/database.db')
print("Opened database successfully");

cursor = conn.execute("SELECT * from t_movies")
for row in cursor:
   print(row)