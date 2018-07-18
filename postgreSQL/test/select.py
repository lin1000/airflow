#!/usr/bin/python
import psycopg2

conn = psycopg2.connect(database="testdb", user="postgres", password="q1w2e3r4", host="127.0.0.1", port="5432")
print("Opened database successfully")

cur = conn.cursor()
"""
  Column   |     Type      | Collation | Nullable | Default
-----------+---------------+-----------+----------+---------
 id        | integer       |           | not null |
 name      | text          |           | not null |
 age       | integer       |           | not null |
 address   | character(50) |           |          |
 salary    | real          |           |          |
 join_date | date          |           |          |
"""
cur.execute("SELECT * from COMPANY order by SALARY DESC")
rows = cur.fetchall()
for row in rows:
   print("====================")
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("AGE = ", row[2])
   print("ADDRESS = ", row[3])
   print("SALARY = ", row[4])
   print("JOIN_DATE = ", row[5])

print("Total number of rows : " + str(cur.rowcount))
print("Operation done successfully")
conn.close()
