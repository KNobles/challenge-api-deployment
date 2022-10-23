FROM python:3.10.8

COPY ./src app/src
COPY ./requirements.txt /app

RUN pip3 install -r /app/requirements.txt

WORKDIR /app/src

EXPOSE 8000

CMD [ "uvicorn", "app:app", "--host=0.0.0.0", "--reload" ]
