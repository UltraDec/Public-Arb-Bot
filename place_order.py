import eospy.keys
import eospy.cleos


def place_order(account, wallet, rate,
                quantity1, token1, precision1, 
                quantity2, token2, precision2):
    #The api endpoint used for pushing the transaction.
    print("Placing order for " + str(quantity1) + " LOOT at " + str(rate) + "...")
    # ce = eospy.cleos.Cleos(url='https://api.waxsweden.org') 
    ce = eospy.cleos.Cleos(url='https://wax.greymass.com') 

    #The private key used to sign the transaction, replace with your own.
    private_key = YOUR-PRIVATE-KEY-HERE

    key1 = eospy.keys.EOSKey(private_key)

    # Quantity and memo for the transfer
    quantity = f"{float(quantity1):.{precision1}f} {token1}" 
    memo = f"{float(quantity2):.{precision2}f} {token2}"      

    #The payload, this contains all the data we need to provide to the blockchain.
    payload = [
            
            # The following are the arguments needed by the eosio.token contract.
            {
                'args': {
                    "from": wallet,  # Replace with your wallet address.
                    "to": 'alcordexmain',  # Replace with the destination wallet address.
                    "quantity": quantity,  # The amount in WAX with 8 decimals.
                    "memo": memo, # A memo of your choosing or leave blank.
                },
                "account": account, # The smart contract of the WAX token.
                "name": "transfer",       # The name of the Smart contract action.
                "authorization": [{
                    "actor": wallet, #The address of the person sending the transaction.
                    "permission": "alcor",
                }],
            }
        ]

    # Here we convert the transaction data to binary.
    data=ce.abi_json_to_bin(payload[0]['account'],payload[0]['name'],payload[0]['args'])

    payload[0]['data']=data['binargs']

    payload[0].pop('args')

    trx = {"actions":[payload[0]]}
    # Now we send the transaction to the blockchain (optional to view below)
    tx1 = ce.push_transaction(trx, [key1])
    id = tx1['processed']['action_traces'][0]['inline_traces'][2]['act']['data']['sell_order']['id']

    # file = open("transaction.txt", "w")
    # file.write(str(tx1))
    # file.close
    # print(tx1)

    # If the transaction was successful the script will show you the transacion ID.
    print("Order " + str(id) + " successfully placed")
    return id