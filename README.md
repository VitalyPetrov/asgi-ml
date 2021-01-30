## asgi-ml


Pet-project to be used as a baseline for ML-based microservices development

### Drives specification:

<b>Web:</b> [FastAPI](https://github.com/tiangolo/fastapi) \
<b>ML:</b> scikit-learn, implicit, CatBoost, any-not-heavy-model \
<b>DB engine:</b> SQLAlchemy (with any compatible driver)

### How to launch

1) Make sure a have a Docker CLI executable on your machine:
```
docker --version
```

2) On project root directory:

```
docker build . -t asgi-ml
docker run -p 8080:8080 -t asgi-ml:latest
```

3) You`ll see a message that Uvicorn instance is running on localhost:8080

4) (optional) see api docs at http://0.0.0.0:8080/docs 
