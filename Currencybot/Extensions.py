import json
import requests
from Config import keys

class Apiexception(Exception):
    pass

class Cryptoconverter:
    @staticmethod
    def converter(base: str, quote: str, amount: str ):
        if base == quote:
            raise Apiexception('Чё плюшки в плюшки переводить будем? Или всё-таки нормальный запрос пришлёшь?')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise Apiexception(f'Чё за валюта такая "{base}"? Не хочу, давай другую валюту, бро!')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise Apiexception(f'Чё за валюта такая "{quote}"? Не хочу, давай другую валюту, бро!')
        try:
            amount = float(amount)
        except ValueError:
            raise Apiexception('Что-то какое-то странное количество , а ну глянь ещё!')


        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        val = json.loads(r.content)[keys[quote]]
        return val
