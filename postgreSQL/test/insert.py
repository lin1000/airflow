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

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY,JOIN_DATE) \
      VALUES (1, 'Paul', 32, 'California', 20000.00,'2001-01-01' )");

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY,JOIN_DATE) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 ,DEFAULT)");

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY,JOIN_DATE) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00, '2018-01-01' )");

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

conn.commit()
print("Records created successfully")
conn.close()