from fastapi.testclient import TestClient
from main import app
import pytest


client = TestClient(app)


def test_convert_valid():
    content = {
        "source" : "sek",
        "target" : "usd",
        "amount" : 100

    }
    response = client.post("/convert", json=content)
    assert response.status_code == 200

def test_convert_invalid_currency():
    with pytest.raises(Exception) as exc:
        response = client.post("/convert", json={
        "source": "xxx",
        "target": "usd",
        "amount": 100
        })
    

    assert "Currency xxx is not supported" in str(exc.value)

def test_convert_negative_amount():
    with pytest.raises(Exception) as exc:
        response = client.post("/convert", json={
        "source": "sek",
        "target": "usd",
        "amount": -10
        })
    assert "Amount -10.0 is invalid" in str(exc)


def test_convert_missing_field():
    pass