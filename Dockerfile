FROM python:3.6-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apk -U add python3-dev py-pip nodejs nodejs-npm openjdk8
RUN pip install pipenv 

COPY . /usr/src/app
RUN pipenv install 
RUN npm install