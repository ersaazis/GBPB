#!/bin/bash
echo Nama Docker :
read name
echo PROXY :
read PROXY
echo SERVER :
read SERVER
echo PORT VNC :
read PORT

docker container create \
-e PROXY = $PROXY \
-e SERVER = $SERVER \
-p $PORT:5900 \
--name $name --cpus=0.9 daftarpb
docker container start $name
docker network connect akun_network $name
