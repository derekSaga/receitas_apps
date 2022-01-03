FROM python:3.8

WORKDIR /api

COPY . /api
   
RUN pip install --upgrade pip && \
    pip install -r requirements.txt