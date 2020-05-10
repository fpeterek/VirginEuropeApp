FROM python:3.8-alpine

MAINTAINER fpeterek@seznam.cz

WORKDIR /fpeterek/virgineurope/

COPY manage.py requirements.txt db.sqlite3 ./
COPY VirginEuropeApp/ VirginEuropeApp/
COPY VirginEurope/ VirginEurope/
COPY templates/ templates/

RUN pip install -r requirements.txt

ENTRYPOINT ./manage.py runserver 0.0.0.0:8000

