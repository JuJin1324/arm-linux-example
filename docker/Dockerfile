FROM python:3.8
LABEL maintainer="jujin1324@daum.net"

RUN apt-get update && apt-get install -y gcc-arm-linux-gnueabi g++-arm-linux-gnueabi \
cmake

WORKDIR /home/app

ENTRYPOINT python3 ./docker/docker-entrypoint.py