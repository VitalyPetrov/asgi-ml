import pytest
from fastapi.testclient import TestClient

from src.main import app


@pytest.fixture(scope="session")
def client():
    with TestClient(app) as clnt:
        yield clnt
