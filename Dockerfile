FROM debian:jessie

MAINTAINER gijsmolenaar@gmail.com

RUN apt-get update && \
    apt-get install -y \
        python3-pip \
        python3-dialog \
        python3-requests \
        openvpn \
        dialog \
        && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD . /menu

RUN cd /menu && pip3 install .

CMD /usr/local/bin/anansi-menu.py
