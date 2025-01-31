def addprofit(profit):
    file = open("TotalProfit.txt", "a+") 
    file.seek(0)
    CurrentProfit = file.read()
    file.truncate(0)
    try:
        CurrentProfit = int(CurrentProfit)
    except ValueError:
            CurrentProfit = 0
    CurrentProfit = CurrentProfit + profit
    file.write(str(CurrentProfit))
    file.close

def printtotal():
    file = open("TotalProfit.txt", "a+") 
    file.seek(0)
    CurrentProfit = file.read()
    print("Total Profit of at least " + str(CurrentProfit) + " WAX")
    file.close