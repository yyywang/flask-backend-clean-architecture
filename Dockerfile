# syntax=docker/dockerfile:1

FROM python:3.9-slim

ARG APP_ENV

# 修改时区
ENV TZ=Asia/Shanghai DEBIAN_FRONTEND=noninteractive
RUN ln -fs /usr/share/zoneinfo/${TZ} /etc/localtime && echo ${TZ} > /etc/timezone

RUN apt-get update -q \
    && apt-get install --no-install-recommends -qy python3-dev g++ gcc inetutils-ping  \
    libgl1-mesa-glx ffmpeg libsm6 libxext6 -y

WORKDIR /code

RUN pip3 install gunicorn
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

COPY . .

ENV FLASK_APP=uwsgi:application FLASK_ENV=$APP_ENV

CMD ["gunicorn", "-b", "0.0.0.0:5010", "uwsgi.web:application"]
