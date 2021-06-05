FROM python:3.9.1-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /webdjango

RUN pip install --upgrade pip
COPY requirements.txt /webdjango/
RUN pip install -r requirements.txt

COPY . /webdjango/