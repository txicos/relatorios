FROM python:3.11

ARG DEPLOY_CMD="uvicorn main:app --port 8080 --reload"

ENV DEPLOY_CMD=${DEPLOY_CMD}

WORKDIR /usr/api

COPY . /usr/api

RUN pip install -r requirements.txt

ENTRYPOINT ["sh","docker-entrypoint.sh"]

CMD ${DEPLOY_CMD}