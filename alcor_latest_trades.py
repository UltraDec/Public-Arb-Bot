import requests
import time

def get_latest(prev, rate, remaining):
    url = "https://alcor.exchange/api/v2/tickers/loot-warsaken_wax-eosio.token/latest_trades?limit=10"

    response = requests.get(url)

    if response.status_code == 200: #checks if response was success
        data = response.json()
    else:
        print("Error")
        quit()

    returntime = prev
    for item in data:
        if item.get('time') <= prev:
            break
        else:
            if (float(item.get('price')) == float(str(rate))) and (float(item.get('time')) > prev):
                remaining = remaining - item.get('base_volume')
                print(str(item.get('base_volume')) + " LOOT sold")
                if returntime == prev:
                    returntime = item.get('time')

    return {'returntime': returntime, 'remaining': remaining}

