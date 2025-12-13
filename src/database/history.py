#save
#read
from datetime import date

history = {}

def save_exchange(exchange_rate, bank_day,
                   src, target):
    # keys: save src, target, date
    print("saved exchange")

    today = date.today()

    content = {
        "exchange_rate" : exchange_rate,
        "today" : today,
        "bank_day": bank_day,
        "source" : src,
        "target" : target
    }

    key = f"{src}_{target}_{today}"
    
    history[key] = content


def read_history():
    #no parameter means read all
    #with parameter is filtered search
    
    return history


