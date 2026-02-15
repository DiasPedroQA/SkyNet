"""Módulo de configuração para testes com pytest"""

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module")
def test_client():
    """Docstring para test_client"""
    client = TestClient(app)
    yield client
