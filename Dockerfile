FROM python:3.12-bookworm AS base
ARG COMMIT_HASH=unknown

RUN apt-get update -y
RUN apt-get install -y pipx
RUN pipx install --python python3.12 poetry==1.8.5

WORKDIR /opt/foxy_grpc

RUN touch README.md
COPY source source
COPY pyproject.toml .
COPY poetry.lock .

ENV PATH="/root/.local/bin:${PATH}"
RUN poetry install --without=dev

RUN echo $COMMIT_HASH > /commit_hash
