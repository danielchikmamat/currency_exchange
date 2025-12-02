from currency_models import ExchangeRequest
from utils import seriesId, valid_amount

def test_content(content:ExchangeRequest):
    
    assert content["source"]
    assert content["target"]
    assert content["amount"]

    print(seriesId(content["source"]))
    print(seriesId(content["target"]))


content = {
    "source" : "sek",
    "target" : "usd",
    "amount" : 100
}

test_content(content)