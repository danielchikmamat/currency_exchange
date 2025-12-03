from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_convert_valid():
    content = {
        "source" : "sek",
        "target" : "usd",
        "amount" : 100

    }
    response = client.post("/convert", json=content)
    print(content)
    print(response.json())
    print(response.status_code)
    assert response.status_code == 200
    