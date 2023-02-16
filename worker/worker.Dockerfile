FROM python:3.10-slim-buster

ENV PROJECT_ROOT="/opt/worker/"
ENV PYTHONPATH=${PYTHONPATH}:${PROJECT_ROOT}

WORKDIR ${PROJECT_ROOT}


RUN pip install poetry

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false \
    && poetry install

ADD . ./

CMD ["celery", "-A", "worker", "worker", "--autoscale", "10", "--loglevel=info"]
