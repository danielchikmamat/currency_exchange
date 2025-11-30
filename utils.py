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