FROM python:3.6-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apk -U add python3-dev py-pip nodejs nodejs-npm openjdk8

COPY . /usr/src/app
RUN pip install -r requirements.txt 
RUN npm install

ENTRYPOINT ["sh", "-c", "python validate.py $URL"]