#!/bin/bash
docker build -t akungenerator akungenerator
docker build -t daftarpb daftarpb
docker network create akun_network
/bin/bash akun.sh
/bin/bash generator.sh