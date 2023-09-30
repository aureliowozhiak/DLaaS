FROM python:3.11

COPY ./src /app

WORKDIR /app

RUN pip install poetry
RUN poetry install

CMD ["poetry", "run", "python", "-m", "main"]