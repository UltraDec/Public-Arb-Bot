import eospy.keys
import eospy.cleos


def swap(account, wallet,
         input, inputtoken, inputprecision, 
         output, outputtoken, outputprecision):
    #The api endpoint used for pushing the transaction.
    ce = eospy.cleos.Cleos(url='https://wax.greymass.com') # 'https://api.eosdetroit.io:443'

    #The private key used to sign the transaction, replace with your own.
    private_key = YOUR-PRIVATE-KEY-HERE

    key1 = eospy.keys.EOSKey(private_key)

    # Quantity and memo for the transfer
    quantity = f"{float(input):.{inputprecision}f} {inputtoken}"  # Assuming WAX has precision 8    
    
    # output_quantity = f"{float(output):.{outputprecision}f} {outputtoken}"
    # memo = f"swapexactout#408#{wallet}#{output}#0"
    memo = f"swapexactout#408#{wallet}#{float(output):.{outputprecision}f} {outputtoken}#0"


    #The payload, this contains all the data we need to provide to the blockchain.
    payload = [
            
            # The following are the arguments needed by the eosio.token contract.
            {
                'args': {
                    "from": 'YOUR-WALLET-HERE',  # Replace with your wallet address.
                    "to": 'swap.alcor',  # Replace with the destination wallet address.
                    "quantity": quantity,  # The amount in WAX with 8 decimals.
                    "memo": memo, # A memo of your choosing or leave blank.
                },
                "account": account, # The smart contract of the WAX token.
                "name": "transfer",       # The name of the Smart contract action.
                "authorization": [{
                    "actor": 'YOUR-WALLET-HERE', #The address of the person sending the transaction.
                    "permission": "alcor",
                }],
            }
        ]

    # Here we convert the transaction data to binary.
    data=ce.abi_json_to_bin(payload[0]['account'],payload[0]['name'],payload[0]['args'])

    payload[0]['data']=data['binargs']

    payload[0].pop('args')

    trx = {"actions":[payload[0]]}

    # Now we send the transaction to the blockchain
    tx1 = ce.push_transaction(trx, [key1])

    # If the transaction was successful the script will show you the transacion ID.
    print('Successful swap')