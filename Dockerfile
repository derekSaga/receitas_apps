FROM python:3.8

WORKDIR /api

COPY . /api

RUN chmod 777 ./scripts/start.sh

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

