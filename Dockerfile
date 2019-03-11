FROM python:3-slim

USER root

# install dependencies
RUN apt-get update \
    && apt-get -y install tesseract-ocr tesseract-ocr-chi-sim \
    && apt-get -y install libglib2.0 libsm6 libxrender1 libxext-dev \
    && apt-get -y install git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# install from source
WORKDIR /usr/src/app
RUN git clone https://github.com/williamfzc/stagesep2.git \
    && cd stagesep2 \
    && pip install . \
    && cd .. \
    && rm -rf stagesep2 \
    && mkdir /root/stagesep2

WORKDIR /root/stagesep2
CMD ["bash"]
