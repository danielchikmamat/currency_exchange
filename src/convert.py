from fastapi import APIRouter
from src.currency_models import ExchangeRequest
from src.utils import seriesId, valid_amount, latest_bank_day
import httpx

router = APIRouter()


@router.post("/")
def convert(request: ExchangeRequest):
    #https://api.riksbank.se/swea/v1/CrossRates/{seriedId1}/{seriesId2}/{from}
    #SEKETT, SEKEURPMI, SEKUSDPMI
    print("post request started!")
    source_currency = seriesId(request.source)
    target_currency = seriesId(request.target)
    amount = valid_amount(request.amount)
    bank_day = latest_bank_day()
    print(bank_day)
    url = f"https://api.riksbank.se/swea/v1/CrossRates/{source_currency}/{target_currency}/{bank_day}"
    print(url)
    response = httpx.get(url) #response object
    print(response)
    print(response.json())
    exchange_rate = response.json()[0]["value"]
    return {"source": request.source, "target": request.target,
            "exchanged_amount": amount*exchange_rate,
            "exchange_rate": exchange_rate, "original_amount": amount,
            "latest_bank_day": bank_day}