
# Package for Python Clients

```bash
pip install psycopg2
```

# Docker Commands

```bash
#Cereate an Network
docker network create --driver bridge postgres-network

#initiate an instance of postgresql called lin1000-postgresql on the postgres-network
export pwd_home=`pwd`
docker rm -f lin1000-postgresql 
docker run \
    --name lin1000-postgresql \
    --network postgres-network \
    -p 5432:5432 \
    -v ${pwd_home}/pgdata:/var/lib/postgresql/data \
    -e POSTGRES_PASSWORD=***q(8)*** \
    -d postgres

#Create an user : lin1000
docker run -it --rm --network postgres-network postgres /bin/bash
docker exec -it lin1000-postgresql /bin/bash
> createuser lin1000 -P --createdb -h lin1000-postgresql -U postgres
> createdb testdb
> psql
>> \list
>> \dg 
>> \dp
>> CREATE TABLE COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL,
   JOIN_DATE	  DATE
);

>>CREATE TABLE DEPARTMENT(
   ID INT PRIMARY KEY      NOT NULL,
   DEPT           CHAR(50) NOT NULL,
   EMP_ID         INT      NOT NULL
);

>>INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY,JOIN_DATE) VALUES (1, 'Paul', 32, 'California', 20000.00,'2001-07-13');
>>INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,JOIN_DATE) VALUES (2, 'Allen', 25, 'Texas', '2007-12-13');
>>INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY,JOIN_DATE) VALUES (3, 'Teddy', 23, 'Norway', 20000.00, DEFAULT );
>>INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY,JOIN_DATE) VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00, '2007-12-13' ), (5, 'David', 27, 'Texas', 85000.00, '2007-12-13');
>>With CTE AS
(Select
 ID
, NAME
, AGE
, ADDRESS
, SALARY
FROM COMPANY )
Select * From CTE;
#
```

