# FROM ubuntu:latest

# RUN apt-get update
# RUN apt-get install python3 python3-pip -y

# RUN pip3 install flask
# RUN pip3 install Flask-Migrate
# RUN pip3 install pymysql
# RUN pip3 install flask_SQLalchemy

# RUN mkdir /app


FROM python:3

WORKDIR /app

RUN pip install flask
RUN pip install Flask-Migrate
RUN pip install pymysql
RUN pip install flask_SQLalchemy
RUN pip install pytz

