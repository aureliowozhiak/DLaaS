FROM python:3.11

COPY ./src /app
COPY pyproject.toml poetry.lock* /app/

WORKDIR /app

RUN pip install poetry
RUN poetry install

CMD ["poetry", "run", "python", "-m", "main"]


## Use a official image of Python as base
#FROM python:3.8-slim-buster
#
## Set environment variables
#ENV AIRFLOW_HOME=/opt/airflow
#ENV AIRFLOW__CORE__EXECUTOR=SequentialExecutor
#ENV AIRFLOW__CORE__SQL_ALCHEMY_CONN=sqlite:////opt/airflow/airflow.db
#ENV AIRFLOW__WEBSERVER__SECRET_KEY=secret_key
#ENV AIRFLOW__WEBSERVER__AUTHENTICATE=True
#ENV AIRFLOW__WEBSERVER__AUTH_BACKEND=airflow.contrib.auth.backends.password_auth
#
#
## Install dependencies
#RUN apt-get update && \
#    apt-get install -y --no-install-recommends \
#        freetds-bin \
#        build-essential \
#        libkrb5-dev \
#        libsasl2-dev \
#        libssl-dev \
#        libffi-dev \
#        libpq-dev \
#        git && \
#    apt-get clean && \
#    rm -rf /var/lib/apt/lists/*
#
## Install Apache Airflow
#RUN pip install apache-airflow
#
## Create directories and set permissions
#USER root

#
## Initialize database
#RUN airflow db init && \
#    airflow users create \
#        --username admin \
#        --password admin \
#        --firstname Admin \
#        --lastname User \
#        --role Admin \
#        --email admin@example.com
##
## Expose port 8080 to access Apache Airflow Web UI
#EXPOSE 8080
#
## Start Apache Airflow
#CMD ["airflow", "webserver"]