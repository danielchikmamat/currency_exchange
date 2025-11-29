from typing import Union

from fastapi import FastAPI

import httpx

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/convert/{source}/{target}/{amount}")
def convert(source: str, target: str, amount: float):
    #https://api.riksbank.se/swea/v1/CrossRates/{seriedId1}/{seriesId2}/{from}
    #SEKETT, SEKEURPMI, SEKUSDPMI
    source_currency = seriesId(source)
    target_currency = seriesId(target)
    amount = valid_amount(amount)
    url = f"https://api.riksbank.se/swea/v1/CrossRates/{source_currency}/{target_currency}/2025-11-28"
    response = httpx.get(url) #response object
    print(response)
    print(response.json())
    exchange_rate = response.json()[0]["value"]
    return {"source": source, "target": target, "exchanged_amount": amount*exchange_rate,
            "exchange_rate": exchange_rate, "original_amount": amount}

def seriesId(currency:str):
    if currency.lower() == "sek":
        return "SEKETT"
    if currency.lower() == "usd":
        return "SEKUSDPMI"
    if currency.lower() == "eur":
        return "SEKEURPMI"

    raise Exception(f"Currency {currency} is not supported")

def valid_amount(amount: float):
    if amount < 0:
        raise Exception(f"Amount {amount} is invalid")
    return amount