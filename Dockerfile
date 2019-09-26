FROM python:3-alpine3.10
ENV PYTHONUNBUFFERED 1
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev 
RUN pip3 install psycopg2
RUN apk add libxml2-dev libxslt-dev
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code
RUN pip3 install -r requirements.txt
ADD . /code