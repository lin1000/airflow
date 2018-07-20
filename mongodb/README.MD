# Package for Python Clients

```bash
pip install pika

# Send a Hello World Message (verified)
python basic/send.py

# Send a Message that represent a complex task with delay (verified)
python basic/send_task.py

# Receive Messages a with different options (verified)
python basic/receive.py
python basic/receive_task.py
python basic/receive_task_detail.py
python basic/receive_basic_ack.py
python basic/receive_no_ack.py

# Send a Message to durable_queue (verified)
python durable_queue/send_task_durable.py

# Receive Messages a with different options (verified)
python durable_queue/receive_task_basic_ack.py
python durable_queue/receive_task_basic_ack_basic_ops.py
```

# Docker Commands


#initiate an instance of mongodb called lin1000-mongodb 

```bash
## Run instance (Verified)
export pwd_home=`pwd`
docker pull mongodb
docker stop lin1000-mongodb
docker start lin1000-mongodb 
docker rm -f lin1000-mongodb
docker run \
    --name lin1000-mongodb \
    -p 27017:27017 \
    -v ${pwd_home}/data/db:/data/db \
    -v ${pwd_home}/data/backup:/data/backup \
    -d \
    mongo --auth

##Create User (Verified)
docker exec -it lin1000-mongodb mongo admin
db.createUser({ user: 'lin1000', pwd: 'password', roles: [ { role: "userAdminAnyDatabase", db: "admin" } ] });
db.auth("lin1000","password")
db.grantRolesToUser('lin1000',[{ role: "root", db: "admin" }])

##Backup the opendata database (created on mongodb by myself) - not succeed WORK IN PROGRESS
docker exec lin1000-mongodb sh -c 'var=`date +%Y%m%d%H%M` mongodump -h localhost --port 27017 -u lin1000 -p password -d opendata -o /data/backup/${var}_test1.dat'

```

## Note on the userAdminAnyDatabase Role
The following is discussion from stak overflow, pretty concise and clear.
https://stackoverflow.com/questions/23943651/mongodb-admin-user-not-authorized
---------------------------------------------------------------------------------
WTF?! lost an hour for a stupid thing like this. Why do they put in documentation userAdminAnyDatabase instead of root? – akostadinov Dec 4 '16 at 12:58
---------------------------------------------------------------------------------
the idea is that you first create a user that is only used for administrating other users (therefore the role starting with "userAdmin") and only then create your normal users. it kind of makes sense, but i didn't get it the first time right too... @akostadinov – TomTasche Jan 5 '17 at 9:14 
---------------------------------------------------------------------------------
For existing use: db.grantRolesToUser('admin',[{ role: "root", db: "admin" }]) – ostati May 22 '17 at 19:53
---------------------------------------------------------------------------------

* RabbitMQ Admin UI (guest / guest) [http://localhost:15672/]


