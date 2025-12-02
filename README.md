# currency_exchange

## application specification
- exchange a given amount from the pairs sek,usd,euro
- use the latest available exchange rate upon request
- store and retrieve exchange history

## start application
uvicorn main:app --reload

##run from project root
python3 -m src.main
pytest -s
pytest -s tests/test_convert.py

## request item
write in the url http://127.0.0.1:8000/items/itemi

## post request
### version 1 bad practice
POST http://localhost:8000/convert/usd/sek/0.2

### version 2 best practice
POST http://localhost:8000/convert
Content-Type: application/json

{
  "source": "usd",
  "target": "sek",
  "amount": 0.2
}

## local database to remember previous exchange rates
sqlite3
keep an exchange history
reuse exchange rates to save resources
if new value, we make a new request to external api

## gitignore tips
do not upload idea files which are local configurations