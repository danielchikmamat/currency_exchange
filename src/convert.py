from fastapi import APIRouter
from src.currency_models import ExchangeRequest
from src.bank_services.fetch_data import fetch_data
router = APIRouter()


@router.post("/")
def convert(request: ExchangeRequest):    
    
    result = fetch_data(request)

    print("post request started!")

    exchanged = result["amount"] * result["exchange_rate"] 


    return {"source": result["source"], 
            "target": result["target"],
            "exchanged_amount" : exchanged,
            "exchange_rate": result["exchange_rate"], 
            "original_amount": result["amount"],
            "latest_bank_day": result["exchange_date"]
    }