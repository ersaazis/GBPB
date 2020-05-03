#!/bin/bash
echo Nama Docker :
read name
echo CPANEL USERNAME :
read CP_USER
echo CPANEL PASSWORD :
read CP_PASS
echo CPANEL SERVER :
read CP_SERVER
echo MAIL SERVER :
read MAIL_SERVER
echo MYSQL SERVER :
read MYSQL_SERVER
echo MYSQL USERNAME :
read MYSQL_USER
echo MYSQL PASSWORD :
read MYSQL_PASS
echo MYSQL DATABASE :
read MYSQL_DB

docker container create \
-e CP_USER = $CP_USER \
-e CP_PASS = $CP_PASS \
-e CP_SERVER = $CP_SERVER \
-e MAIL_SERVER = $MAIL_SERVER \
-e MYSQL_SERVER = $MYSQL_SERVER \
-e MYSQL_USER = $MYSQL_USER \
-e MYSQL_PASS = $MYSQL_PASS \
-e MYSQL_DB = $MYSQL_DB \
--name $name --cpus=0.9 akungenerator
docker container start $name
docker network connect akun_network $name
