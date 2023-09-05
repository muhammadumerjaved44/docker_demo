FROM continuumio/miniconda3

# activate conda enviorment
RUN /bin/sh -c conda activate base

#installing some packages in the Dcoker Debian
RUN apt-get update -y && apt-get -y install \
    curl \
    nano \
    git

RUN pip install --upgrade pip


WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt