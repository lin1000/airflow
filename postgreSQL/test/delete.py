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

cur.execute("DELETE from COMPANY;")
conn.commit()
print("Total number of rows deleted :", cur.rowcount)

conn.close()
