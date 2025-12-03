from datetime import date, timedelta


def from_today():
    today = date.today()
    one_weeks_back = today - timedelta(days=7)
    return one_weeks_back


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