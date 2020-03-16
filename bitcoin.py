from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time
import os


def get_bitcoin_eur_price():
    """
        get last EURO bitcoin
    """
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
    'symbol':'BTC',  
    'convert':'EUR'
    }
    headers = {
    'Accepts': 'application/json',
    #'X-CMC_PRO_API_KEY': '8f042e0d-e8ff-4c12-926b-1f2017b77bde',
    'X-CMC_PRO_API_KEY': os.getenv('apikey')
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        if data['status']['error_code'] !=0:
            print(data['status']['error_message'])
            exit(100)
        return data['data']['BTC']['quote']['EUR']['price']
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def main():
    avg = 0
    loops = 0
    sum = 0
    while True:
        if loops == 5:
            avg = sum/5
            print('Average of last 10 seconds:',avg)
            loops=0
            avg=0
            sum=0

        last_price = get_bitcoin_eur_price()
        print('last price:',last_price)
        sum+=last_price
        loops+=1
        time.sleep(2)


    
if __name__ == "__main__":
    main()
