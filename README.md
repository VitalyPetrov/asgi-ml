## asgi-ml


Pet-project to be used as a baseline for ML-based microservices development

### Drives specification:

<b>Web:</b> [FastAPI](https://github.com/tiangolo/fastapi) \
<b>Cache:</b> [aiocache](https://github.com/aio-libs/aiocache) \
<b>ML:</b> scikit-learn, implicit, any-not-heavy-model \
<b>DB engine (not implemented yet):</b> SQLAlchemy (with any compatible driver) 

### How to launch

1) Make sure a have a Docker CLI and docker-compose executable on your machine:
```shell
docker --version
docker-compose --version
```

2) Create a folder named ``env`` on project root
and put ``values-dev.env`` file on that folder:
```shell
mkdir env
touch env/values-dev.env
```

Fill `values-dev.env` with the following values:
```dotenv
APP_REDIS_HOST="redis"
APP_REDIS_PORT=6379
APP_REDIS_DB=0
APP_REDIS_PASSWORD="secret"

APP_ML_NUM_TREES=100
APP_ML_MAX_DEPTH=10
APP_ML_SAMPLES_ON_LEAF=2
APP_ML_LOSS_FUNCTION="entropy"
APP_ML_TEST_SIZE=0.05

APP_API_PREFIX=""
```

3) On project root directory:

```shell
docker build -t asgi-ml .
docker-compose up -d
```
You`ll see a message that Uvicorn instance is running on localhost:8080

4) (optional) see api docs at http://0.0.0.0:8080/docs 
