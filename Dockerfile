FROM python:3-slim

USER root

RUN apt-get update \
    && apt-get -y install gcc build-essential \
    && apt-get -y install tesseract-ocr tesseract-ocr-chi-sim libtesseract-dev libleptonica-dev pkg-config \
    && apt-get -y install libglib2.0 libsm6 libxrender1 libxext-dev

RUN pip install --no-cache-dir stagesep2==0.2.4 \
    && apt-get purge -y --auto-remove gcc build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /root/stagesep2
CMD ["bash"]
