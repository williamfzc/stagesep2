FROM ubuntu:18.04
MAINTAINER williamfzc <fengzc@vip.qq.com>

USER root
ENV HOME /root
WORKDIR /root

RUN apt-get update \
    && apt-get -y install python3 python3-pip \
    && apt-get -y install tesseract-ocr tesseract-ocr-chi-sim \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install stagesep2 \
    && mkdir stagesep

WORKDIR /root/stagesep
CMD ["bash"]
