poetry run alembic upgrade head

poetry run gunicorn --workers 5 --bind 0.0.0.0:8000 main:app --worker-class uvicorn.workers.UvicornWorker