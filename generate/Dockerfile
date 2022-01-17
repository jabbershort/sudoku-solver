FROM ubuntu:focal

SHELL ["/bin/bash","-c"]
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    wget \
    python3

RUN wget --no-check-certificate https://qqwing.com/qqwing_1.3.4-1_amd64.deb
RUN dpkg --install qqwing_1.3.4-1_amd64.deb

RUN mkdir /data/
ADD generate.py /generate.py
ADD solve.py /solve.py
ADD puzzles/puzzles.json /data/puzzles.json
CMD python3 /generate.py