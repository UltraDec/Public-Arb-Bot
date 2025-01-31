import eospy.keys
import eospy.cleos


def cancel(wallet, order_id):
    #The api endpoint used for pushing the transaction.
    print("Cancelling order " + str(order_id) + "...")
    ce = eospy.cleos.Cleos(url='https://wax.greymass.com') 
    private_key = YOUR-PRIVATE-KEY-HERE

    key1 = eospy.keys.EOSKey(private_key)


    #The payload, this contains all the data we need to provide to the blockchain.
    payload = [
            
            # The following are the arguments needed by the eosio.token contract.
            {
                'args': {
                    "executor": wallet,  # Replace with your wallet address.
                    "market_id": '173',  # Replace with the destination wallet address.
                    "order_id": order_id,  # The amount in WAX with 8 decimals.
                },
                "account": "alcordexmain", # The smart contract of the WAX token.
                "name": "cancelsell",       # The name of the Smart contract action.
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

    # If the transaction was successful the script will show you the transacion ID.
    print("Order successfully cancelled")