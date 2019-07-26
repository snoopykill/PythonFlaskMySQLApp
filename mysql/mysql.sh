#!/bin/bash -ex

docker rm -f some-mysql ||:

# docker run -d --name some-mysql \
#     -e MYSQL_ROOT_PASSWORD=jay \
#     -e MYSQL_DATABASE=BucketList \
#     -p 3306:3306 \
#     mysql:5.7


docker run -d --name some-mysql -v `pwd`/data:/docker-entrypoint-initdb.d \
    -e MYSQL_ROOT_PASSWORD=jay \
    -e MYSQL_DATABASE=BucketList \
    -p 3306:3306 \
    mysql:5.7