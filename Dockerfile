FROM ghcr.io/astral-sh/uv:latest AS uv
FROM python:3.13-slim
COPY --from=uv /uv /bin/uv
WORKDIR /app

COPY pyproject.toml uv.lock /app/
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project

COPY . /app

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen

ENV PATH="/app/.venv/bin:$PATH"

CMD ["python3", "app.py"]