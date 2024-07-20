FROM python:3

WORKDIR /Mobile_Services

COPY /Mobile_Services/requirements.txt /Mobile_Services

RUN apt-get update && apt-get install -y netcat-traditional && rm -rf /var/lib/apt/lists/*

RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY /Mobile_Services/. /Mobile_Services

EXPOSE 5000

CMD [ "python", "./CountryCodesAPI.py" ]
