{% if cookiecutter.include_docker == "y" -%}
FROM docker.io/library/python:{{ cookiecutter.python_version }}-slim-bookworm AS builder

# This approximately follows this guide: https://hynek.me/articles/docker-uv/
# Which creates a standalone environment with the dependencies.
# - Silence uv complaining about not being able to use hard links,
# - tell uv to byte-compile packages for faster application startups,
# - prevent uv from accidentally downloading isolated Python builds,
# - pick a Python (use `/usr/bin/python3.13` on uv 0.5.0 and later),
# - and finally declare `/usr/src/app` as the target for `uv sync`.
ENV PYTHONUNBUFFERED=True \
    UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_DOWNLOADS=never \
    UV_PROJECT_ENVIRONMENT=/usr/src/app/.venv

COPY --from=ghcr.io/astral-sh/uv:0.8.12 /uv /uvx /bin/

# Set working directory
WORKDIR /usr/src/app

# Synchronize dependencies.
# This layer is cached until uv.lock or pyproject.toml change.
RUN --mount=type=cache,target=/root/.cache \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync \
        --frozen \
        --all-extras \
        --no-install-project \
        --no-dev \
        --no-editable


COPY . /usr/src/app

RUN --mount=type=cache,target=/root/.cache \
    uv sync --frozen \
        --all-extras \
        --no-editable \
        --no-dev \
        --python=$UV_PROJECT_ENVIRONMENT

# Stage 2: Final runtime image
FROM docker.io/library/python:{{ cookiecutter.python_version }}-slim-bookworm

# Create non-root user
RUN groupadd -r app && \
    useradd -r -d /usr/src/app -g app -N app

USER app
WORKDIR /usr/src/app

# Copy the application code
COPY --from=builder --chown=app:app /usr/src/app/.venv /usr/src/app/.venv
COPY --from=builder --chown=app:app /usr/src/app /usr/src/app

# make sure we use the virtualenv python by default
ENV PATH="/usr/src/app/.venv/bin:$PATH"

# Smoke test that the application can, in fact, be imported.
RUN python -V && \
    python -Im site

ENTRYPOINT [{{ cookiecutter.cli_name }}]
{%- endif %}
