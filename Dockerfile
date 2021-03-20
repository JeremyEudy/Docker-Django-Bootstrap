FROM python:3.6

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir -p /opt/services/web/src
WORKDIR /opt/services/web/src

COPY . /opt/services/web/src

RUN apt-get update && apt-get install -y fortune

EXPOSE 80
