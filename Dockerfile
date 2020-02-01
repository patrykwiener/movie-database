FROM python:3

#Set environment variables
ENV PYTHONUNBUFFERED 1

#Set work directory
RUN mkdir /code
WORKDIR /code

RUN pip install virtualenv
ENV VIRTUAL_ENV=/usr/src/app/venv
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

#Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /code/