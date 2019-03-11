FROM python:3-slim

USER root

RUN apt-get update \
    && apt-get -y install tesseract-ocr tesseract-ocr-chi-sim \
    && apt-get -y install libglib2.0 libsm6 libxrender1 libxext-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir stagesep2 \
    && mkdir /root/stagesep2

WORKDIR /root/stagesep2
CMD ["bash"]
