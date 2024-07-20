FROM python:3

WORKDIR /code

COPY ./Mobile_Services/requirements.txt /code

RUN apt-get update && apt-get install -y netcat-traditional && rm -rf /var/lib/apt/lists/*

RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY ./Mobile_Services /code


EXPOSE 5000

CMD [ "python", "./app.py" ]