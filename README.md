# asgi-ml

Distibuted ML-based service prototype.

## Components

**Web:** [FastAPI](https://github.com/tiangolo/fastapi) \
**ML:** [scikit-learn](https://github.com/scikit-learn/scikit-learn) \
**Task Management:** [Celery](https://github.com/celery/celery) \
**Tasks Queue:** [RabbitMQ](https://github.com/rabbitmq/rabbitmq-server) \
**Results backend:** [Redis](https://github.com/redis/redis)

## How to launch

Make sure a have a Docker CLI and docker-compose executable on your machine:

```bash
docker --version
docker-compose --version
```

Create a folder named ``env`` on project root
and put ``values-dev.env`` file on that folder:

```bash
mkdir env
touch env/values-dev.env
```

Fill the `values-dev.env` file with values:

```dotenv
APP_REDIS_HOST="redis"
APP_REDIS_PORT=6379
APP_REDIS_DB=0

APP_RABBITMQ_HOST='rabbitmq'
APP_RABBITMQ_PORT=5672
APP_RABBITMQ_USERNAME="user"
APP_RABBITMQ_PASSWORD="pwd"

APP_ML_N_ESTIMATORS=100
APP_ML_MAX_DEPTH=10
APP_ML_MIN_SAMPLES_ON_LEAF=2
APP_ML_CRITERION="entropy"
APP_ML_TEST_SIZE=0.05
```

Finally build / pull all needed images and run the deployment

```bash
docker-compose build
docker-compose up -d
```

You`ll see a message that Uvicorn instance is running on localhost:8080

You can see API docs at <http://0.0.0.0:8080/docs> endpoint.
