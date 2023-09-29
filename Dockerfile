FROM python:3.11-slim

RUN apt-get update && apt-get install --no-install-recommends -y nodejs && rm -rf /var/lib/apt/lists/*
RUN pip install poetry
COPY pyproject.toml /app/pyproject.toml
COPY poetry.lock /app/poetry.lock
WORKDIR /app
RUN poetry install --only=main
COPY mexicanbonora /app/mexicanbonora
RUN poetry run python -m mexicanbonora.train

CMD ["poetry","run","python","-OO","-Wd","-m","mexicanbonora"]