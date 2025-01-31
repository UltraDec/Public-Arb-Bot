import requests

def return_wallet_balance():
    url = "https://lightapi.eosamsterdam.net/api/tokenbalance/wax/YOUR-WALLET-HERE/warsaken/LOOT"
    
    response = requests.get(url)

    if response.status_code == 200: #checks if response was success
        data = response.json()
    else:
        print("Error")
        quit()

    return float(data)

def print_wallet_balance():
    url = "https://lightapi.eosamsterdam.net/api/tokenbalance/wax/YOUR-WALLET-HERE/warsaken/LOOT"
    
    response = requests.get(url)

    if response.status_code == 200: #checks if response was success
        data = response.json()
    else:
        print("Error")
        quit()
    
    print(data)
