FROM python:3
MAINTAINER : govindec15@gmail.com


COPY ./src src


CMD ["python","pytest src/pyTest"]




