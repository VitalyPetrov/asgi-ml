FROM python:3.10-slim-buster

ENV PROJECT_ROOT="/opt/asgi-ml/"
ENV PYTHONPATH=${PYTHONPATH}:${PROJECT_ROOT}

WORKDIR ${PROJECT_ROOT}


RUN pip install poetry

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false \
    && poetry install

ADD . ./

EXPOSE 8080

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8080", "src.main:app"]
