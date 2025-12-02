from pydantic import BaseModel

class ExchangeRequest(BaseModel):
    source: str
    target: str
    amount: float

    