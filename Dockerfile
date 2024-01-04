FROM python:3.11.6-alpine3.18

EXPOSE 8000

WORKDIR /nodb

RUN pip install --upgrade pip
RUN apk add gcc musl-dev libffi-dev
RUN pip install poetry

COPY . /nodb

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --without test


CMD ["poetry", "run", "uvicorn", "nodb_fastapi.main:app", "--host", "0.0.0.0", "--port", "9000"]