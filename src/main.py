import json
from typing import Union

from fastapi import FastAPI

from src.convert import router as convert_router
from src.bank_services import router as bank_router

app = FastAPI()

# Include the convert router
app.include_router(convert_router, prefix="/convert", tags=["Convert"])
app.include_router(bank_router, prefix="/latest-bank-day", 
                   tags=["Latest-bank-day"])

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


