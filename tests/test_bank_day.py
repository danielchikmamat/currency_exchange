from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test():
    response = client.get("/latest-bank-day/")
    print(response.json())
    print(response.status_code)

test()
