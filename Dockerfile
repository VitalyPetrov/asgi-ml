# MAINTAINER 7pro
FROM python:3.7-slim-buster

ENV PROJECT_ROOT="/opt/asgi-ml/"
ENV PYTHONPATH=${PYTHONPATH}:${PROJECT_ROOT}

WORKDIR ${PROJECT_ROOT}

# ARG PIP_INDEX_URL="http://pypi.org/simple"

COPY requirements/* requirements/

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libgomp1 \
        && \
    pip3 --trusted-host pypi.org --no-cache-dir install -U -r requirements/base.txt && \
    apt-get autoremove -y \
        build-essential \
        && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/*

ADD . ./

EXPOSE 8080

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8080", "src.app:app"]