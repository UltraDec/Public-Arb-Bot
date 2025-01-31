import time
import alcor_price
import place_order
import alcor_swap_waxtoloot
import alcor_latest_trades
import cancel_order
import totalprofit
import getlootbalance

while (getlootbalance.return_wallet_balance() > 0):
    beginning = time.time()
    # Pulls data from orderbook and returns current lowest asking price - 0.00000001
    print("Pulling data from orderbook...")
    rate = alcor_price.lowest_ask("LOOT", "WAX", "loot-warsaken", "wax-eosio.token")
    print("Lowest order successfully acquired")
    rate = rate - 0.00000001
    # Set how much to list
    input = 10000
    output = 10000 * rate


    # Places sell order on Alcor Exchange
    id = place_order.place_order("warsaken", "YOUR-WALLET-HERE", rate, input, "LOOT", "4", output, "WAX@eosio.token", "8")
    prev = beginning # Gets time of last trade involving your order 
    remaining = input # Tracks loot still in order

    # Waits for sell order to be fulfilled
    print("Waiting for order to be filled...")
    while remaining > 0:
        progress = alcor_latest_trades.get_latest(prev, rate, remaining)
        prev = progress['returntime']
        remaining = progress['remaining']
        
        # Checks if lower order has been created 
        ratecurr = alcor_price.lowest_ask("LOOT", "WAX", "loot-warsaken", "wax-eosio.token")
        ratenew = ratecurr - 0.00000001
        outputnew = ratenew * remaining

        if (ratecurr < rate) and (float(outputnew) > float(alcor_price.swaprate(remaining))):
            
            print("Lower order detected, resetting...")
            # Cancels order and resets at lower price
            cancel_order.cancel("YOUR-WALLET-HERE", id)
            id = place_order.place_order("warsaken", "YOUR-WALLET-HERE", ratenew, remaining, "LOOT", "4", outputnew, "WAX@eosio.token", "8")
            print("Waiting for order to be filled...")
            rate = ratenew
            output = outputnew
            
        time.sleep(10)

    print("Order successfully filled")

    swapped = False
    # Checks if swaprate is profitable and if so, performs swap
    while swapped == False:
        print("Checking if current swaprate is profitable...")
        maxsent = alcor_price.swaprate(input)
        if float(maxsent) < float(output):
            print("Swaprate profitable, swapping...")
            alcor_swap_waxtoloot.swap("eosio.token", "YOUR-WALLET-HERE", maxsent, "WAX", "8", input, "LOOT@warsaken", "4")
            swapped = True
        else:
            print("Current swaprate not profitable, trying again in 60s")
            time.sleep(60)

    profit = str(float(output) - float(maxsent))
    totalprofit.addprofit(profit)
    print('Successful run. Profit of at least ' + profit + " WAX")
    totalprofit.printtotal()


