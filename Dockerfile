FROM docker.io/python:3.8.5-alpine

RUN mkdir /opt/app
WORKDIR /opt/app

COPY requirements.txt /opt/app/
RUN pip3 --no-cache-dir install -r requirements.txt

COPY app.py /opt/app/

ENTRYPOINT ["python3","app.py"]
