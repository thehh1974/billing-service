FROM python:3.6
RUN mkdir -p /usr/src/app/demo_sevice
WORKDIR /usr/src/app/demo_sevice

ADD . /usr/src/app/demo_sevice
CMD python -u run.py
