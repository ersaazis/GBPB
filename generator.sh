#!/bin/bash
echo Nama Docker :
read name
echo PROXY :
read PROXY
echo SERVER :
read SERVER

docker container create 
-e PROXY = $PROXY \
-e SERVER = $SERVER \
--name $name --cpus=0.9 daftarpb
docker container start $name
docker network connect akun_network $name
