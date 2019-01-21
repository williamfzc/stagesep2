# TODO: NEED TEST
FROM ubuntu:18.04
MAINTAINER williamfzc <fengzc@vip.qq.com>

USER root
ENV HOME /root
WORKDIR /root

RUN add-apt-repository ppa:alex-p/tesseract-ocr \
    && apt-get update \
    && apt-get -y install python3 \
    && apt-get -y install tesseract-ocr \
    && apt-get -y install curl \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install stagesep2
    && curl -o /usr/share/tesseract-ocr/4.0/tessdata/chi_sim.traineddata https://github.com/tesseract-ocr/tessdata/blob/master/chi_sim.traineddata
    && mkdir stagesep

WORKDIR /root/stagesep
CMD ["bash"]
