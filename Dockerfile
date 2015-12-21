FROM debian:jessie

MAINTAINER gijsmolenaar@gmail.com

RUN apt-get update && \
    apt-get install -y \
        python-pip \
        openvpn \
        && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install --upgrade pip

RUN pip install urwid requests

ADD . /tmp/menu

RUN cd /tmp/menu && pip install -e .

CMD /usr/local/bin/cif-fetchconfig.py
