FROM ubuntu:16.04

MAINTAINER Jose Gomez Baena

# Variables de entorno para la conexion a la BD
ARG DATABASE_URL
ARG HOST_BD
ARG NAME_BD
ARG PW_BD
ARG TOKENBOT
ARG USER_BD

ENV DATABASE_URL=$DATABASE_URL
ENV HOST_BD=$HOST_BD
ENV NAME_BD=$NAME_BD
ENV PW_BD=$PW_BD
ENV TOKENBOT=$TOKENBOT
ENV USER_BD=$USER_BD

RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get install -y git
RUN git clone https://github.com/josegob/IV-Proyecto.git
RUN pip3 install -r requirements.txt

RUN cd IV-Proyecto/bot-metacritic/ && python3 bot_metacritic.py
