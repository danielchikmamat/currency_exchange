from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_convert(test_content):
    response = client.post("/convert", json=test_content)
    assert response.status_code == 200
    print(response.json())

content = {
    "source" : "sek",
    "target" : "usd",
    "amount" : 100
}

test_convert(content)


