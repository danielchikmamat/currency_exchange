#get request a client may use
#look up exchange rate

from datetime import date, timedelta
import httpx
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def latest_bank_day():
    print("latest date started")
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