# currency_exchange
 

## start application
uvicorn main:app --reload

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


## gitignore tips
do not upload idea files which are local configurations