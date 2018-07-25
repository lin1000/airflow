# Package for Python Clients

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





fmi.
https://medium.com/codingthesmartway-com-blog/angular-6-mean-stack-crash-course-part-2-implementing-the-back-end-642567e16bb9