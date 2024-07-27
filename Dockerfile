FROM python:3

ARG APP_DIR

WORKDIR ${APP_DIR}



COPY /${APP_DIR}/requirements.txt /${APP_DIR}/

RUN apt-get update && apt-get install -y netcat-traditional && rm -rf /var/lib/apt/lists/*

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

COPY /${APP_DIR}/. /${APP_DIR}

EXPOSE 5000

CMD [ "python", "./${SERVICE_NAME}.py" ]
