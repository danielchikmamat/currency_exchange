import json
from typing import Union

from fastapi import FastAPI

import httpx
from pydantic import BaseModel
from datetime import date, timedelta
from currency_models import ExchangeRequest
from utils import seriesId, valid_amount
def _latest_bank_day():

    today = date.today()
    two_weeks_back = today - timedelta(days=14)
    print(today)
    print(two_weeks_back)

    calendar_interval_url = f"https://api.riksbank.se/swea/v1/CalendarDays/{two_weeks_back}/{today}"
    calendar_response = httpx.get(calendar_interval_url)
    calendar_json = calendar_response.json()

    #with open('example.calendar-days.json', 'r') as file:
     #   data = json.load(file)
    #calendar_json = data

    for day in reversed(calendar_json):
        if day["swedishBankday"]:
            return day["calendarDate"]

    raise ValueError("No bank day found")

latest_bank_day = _latest_bank_day()
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


#@app.post("/convert/{source}/{target}/{amount}")
@app.post("/convert")
def convert(request: ExchangeRequest):
    #https://api.riksbank.se/swea/v1/CrossRates/{seriedId1}/{seriesId2}/{from}
    #SEKETT, SEKEURPMI, SEKUSDPMI
    source_currency = seriesId(request.source)
    target_currency = seriesId(request.target)
    amount = valid_amount(request.amount)
    url = f"https://api.riksbank.se/swea/v1/CrossRates/{source_currency}/{target_currency}/{latest_bank_day}"
    response = httpx.get(url) #response object
    print(response)
    print(response.json())
    exchange_rate = response.json()[0]["value"]
    return {"source": request.source, "target": request.target,
            "exchanged_amount": amount*exchange_rate,
            "exchange_rate": exchange_rate, "original_amount": amount,
            "latest_bank_day": latest_bank_day}


