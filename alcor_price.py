from bs4 import BeautifulSoup
import requests

def get_orderbook_formatted(name1, name2, token1, token2):
    url = "https://alcor.exchange/api/v2/tickers/" + token1 + "_" + token2 + "/orderbook"

    response = requests.get(url)

    if response.status_code == 200: #checks if response was success
        data = response.json()
    else:
        print("Error")
        quit()

    highest_bid = data.get('bids')[0]
    lowest_ask = data.get('asks')[0]

    highest_bid_rate = highest_bid[0]
    highest_bid_name2 = highest_bid[1] + " " + name2
    highest_bid_name1 = str(round(float(highest_bid[1]) / float(highest_bid[0]), 4)) + " " + name1
    highest_bid_amounts = highest_bid_name1 + "/" + highest_bid_name2

    lowest_ask_rate = lowest_ask[0]
    lowest_ask_name1 = lowest_ask[1] + " " + name1
    lowest_ask_name2 = str(float(lowest_ask[1]) * float(lowest_ask[0])) + " " + name2
    lowest_ask_amounts = lowest_ask_name1 + "/" + lowest_ask_name2


    print('Orderbook data for ' + name1 + "/"+ name2)
    print("Lowest ask: " + lowest_ask_amounts + " at a price of " + lowest_ask_rate)
    print("Highest bid: " + highest_bid_amounts + " at a price of " + highest_bid_rate)

def get_orderbook_data(name1, name2, token1, token2):
    url = "https://alcor.exchange/api/v2/tickers/" + token1 + "_" + token2 + "/orderbook"

    response = requests.get(url)

    if response.status_code == 200: #checks if response was success
        data = response.json()
    else:
        print("Error")
        quit()

    highest_bid = data.get('bids')[0]
    lowest_ask = data.get('asks')[0]

    highest_bid_rate = highest_bid[0]
    highest_bid_name2 = highest_bid[1] + " " + name2
    highest_bid_name1 = str(round(float(highest_bid[1]) / float(highest_bid[0]), 4)) + " " + name1
    highest_bid_amounts = highest_bid_name1 + "/" + highest_bid_name2

    lowest_ask_rate = lowest_ask[0]
    lowest_ask_name1 = lowest_ask[1] + " " + name1
    lowest_ask_name2 = str(float(lowest_ask[1]) * float(lowest_ask[0])) + " " + name2
    lowest_ask_amounts = lowest_ask_name1 + "/" + lowest_ask_name2


    print('Orderbook data for ' + name1 + "/"+ name2)
    print("Lowest ask: " + lowest_ask_amounts + " at a price of " + lowest_ask_rate)
    print("Highest bid: " + highest_bid_amounts + " at a price of " + highest_bid_rate)
    

def pool(name1, name2, poolid):
    url = "https://alcor.exchange/api/v2/swap/pools/" + poolid

    response = requests.get(url)

    if response.status_code == 200: #checks if response was success
        data = response.json()
    else:
        print("Error")
        quit()

    name1quant = data.get('tokenA').get('quantity')
    name2quant = data.get('tokenB').get('quantity')
    # approxrate = name1quant / name2quant

    print("Volume in pool: ")
    print(str(name1quant) + " " + name1)
    print(str(name2quant) + " " + name2)
    # print(approxrate)

def swaprate(amount):
    url = "https://alcor.exchange/api/v2/swapRouter/getRoute?trade_type=EXACT_OUPUT&input=wax-eosio.token&output=loot-warsaken&amount=" + str(amount) + "&slippage=0.50&receiver=alcordexfund&maxHops=1"

    response = requests.get(url)

    if response.status_code == 200: #checks if response was success
        data = response.json()
    else:
        print("Error")
        quit()
    
    maxsent = data.get('maxSent')
    # print("Maxsent: " + maxsent)
    return maxsent

def lowest_ask(name1, name2, token1, token2):
    url = "https://alcor.exchange/api/v2/tickers/" + token1 + "_" + token2 + "/orderbook"

    response = requests.get(url)

    if response.status_code == 200: #checks if response was success
        data = response.json()
    else:
        print("Error")
        quit()

    lowest_ask = data.get('asks')[0]

    lowest_ask_rate = lowest_ask[0]
    lowest_ask_name1 = lowest_ask[1] + " " + name1
    lowest_ask_name2 = str(float(lowest_ask[1]) * float(lowest_ask[0])) + " " + name2
    lowest_ask_amounts = lowest_ask_name1 + "/" + lowest_ask_name2

    lowest_ask_rate = float(lowest_ask_rate)
    return lowest_ask_rate

