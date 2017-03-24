FROM haimhelman/octarine-python
RUN mkdir -p /usr/src/app/demo_sevice
WORKDIR /usr/src/app/demo_sevice

ADD . /usr/src/app/demo_sevice
ENV OCTARINE_AUTHSERVER="http://172.17.0.1:5000/"
ENV OCTARINE_SERVER="http://172.17.0.1:5001/"
CMD python -u run.py
