# TODO Добавить разветку PostgreSQL вместе с API
# TODO Poetry -> uv

# Install Python, Update Debian 12 and Install curl
FROM python:3.10.14-slim-bookworm
RUN apt-get update && apt-get upgrade -y && apt-get install --no-install-recommends -y curl

# Env Variables
ENV \
    # Python settings
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    # PIP settings
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # Poetry settings
    POETRY_VERSION=1.8.3 \
    POETRY_CACHE_DIR="/tmp/poetry_cache" \
    POETRY_HOME="/root/.local/bin/poetry" \
    POETRY_VENV_PATH="/root/priscillafx/.venv/bin" \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1

ENV PATH="$POETRY_HOME:$POETRY_VENV_PATH:$PATH"

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=$POETRY_VERSION python3 -

# Copy project files
RUN mkdir /root/priscillafx
WORKDIR /root/priscillafx
COPY . .

# Install dependencies
RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR

# Expose API (FastAPI local port: 50150)
EXPOSE 50151

# Startup API
WORKDIR /root/priscillafx/src/backend
CMD ["poetry", "run", "gunicorn", "--config=gunicorn.py", "main:app"]
