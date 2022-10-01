FROM python:3.8-slim-bullseye

USER root

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir /opt/app

WORKDIR /opt/app

COPY app/ .

COPY requirements.txt .

RUN pip install -r requirements.txt

USER nobody

CMD ["python","bot.py"]