FROM python:3

ARG APP_DIR 
ARG SERVICE_NAME=CountryCodesAPI

WORKDIR ${APP_DIR}

COPY /${APP_DIR}/requirements.txt /${APP_DIR}

RUN apt-get update && apt-get install -y netcat-traditional && rm -rf /var/lib/apt/lists/*

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

COPY /${APP_DIR}/. /${APP_DIR}


RUN echo '#!/bin/sh' > /startup.sh && \
    echo 'python '${SERVICE_NAME}'.py' >> /startup.sh && \
    chmod +x /startup.sh

# Use the startup.sh script as the CMD
CMD ["/startup.sh"]
