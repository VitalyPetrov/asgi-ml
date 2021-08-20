FROM python:3.8-slim-buster

ENV PROJECT_ROOT="/opt/asgi-ml/"
ENV PYTHONPATH=${PYTHONPATH}:${PROJECT_ROOT}
ENV PIP_TRUSTED_HOST="pypi.org"

WORKDIR ${PROJECT_ROOT}

# ARG PIP_INDEX_URL="http://pypi.org/simple"

COPY requirements/* requirements/

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libgomp1 \
        && \
    pip3 --no-cache-dir install -U -r requirements/base.txt && \
    apt-get autoremove -y \
        build-essential \
        && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/*

ADD . ./

EXPOSE 8080

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8080", "src.main:app"]
