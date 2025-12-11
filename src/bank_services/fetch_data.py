from src.utils import seriesId, valid_amount, from_today
from src.currency_models import ExchangeRequest
import httpx

def fetch_data(request: ExchangeRequest):
    source_currency = seriesId(request.source)
    target_currency = seriesId(request.target)
    amount = valid_amount(request.amount)
    bank_day = from_today()
    url = f"https://api.riksbank.se/swea/v1/CrossRates/{source_currency}/{target_currency}/{bank_day}"

    response = httpx.get(url) #response object
    exchange_rate = response.json()[-1]["value"]
    exchange_date = response.json()[-1]["date"]

    return {
        "source" : source_currency,
        "target" : target_currency,
        "amount" : amount,
        "exchange_rate" : exchange_rate,
        "exchange_date" : exchange_date,

    }