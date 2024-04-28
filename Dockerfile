FROM tiangolo/uvicorn-gunicorn:python3.10

LABEL maintainer="John Yost <hokiegeek2@gmail.com>"

RUN pip install fastapi

COPY ./app /app

ENTRYPOINT uvicorn main:app --reload --host 0.0.0.0
