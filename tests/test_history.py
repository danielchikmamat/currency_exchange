from datetime import date, timedelta
from src.database.history import save_exchange, read_history

def test_save():
    save_exchange(
        0.0135, "2025-12-12", "sek", "usd"
    )
    today = date.today()
    history = read_history()
    key = f"sek_usd_{today}"
    assert len(history.items()) == 1
    assert history[key]["exchange_rate"] == 0.0135
    assert history[key]["source"] == "sek"
    assert history[key]["target"] == "usd"


