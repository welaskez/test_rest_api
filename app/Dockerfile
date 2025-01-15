FROM python:3.11.9-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY app .

CMD ["sh", "-c", "poetry run alembic upgrade head && poetry run gunicorn --workers 5 --bind 0.0.0.0:8000 main:app --worker-class uvicorn.workers.UvicornWorker"]
