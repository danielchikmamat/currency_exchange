from src.currency_models import ExchangeRequest
from src.utils import seriesId

def test_content():
    content = {
    "source" : "sek",
    "target" : "usd",
    "amount" : 100
    }  

    assert content["source"]
    assert content["target"]
    assert content["amount"]

    print(seriesId(content["source"]))
    print(seriesId(content["target"]))
