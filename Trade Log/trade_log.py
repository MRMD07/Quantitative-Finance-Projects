trade_list = [("BTC" , "BUY" , 100000, 0.5)] #dummy trade
#function to add new trades
def new_trade(num):
    new_entries = []
    for count in range(1,num+1):
        pair = input("Which pair")
        direction = input("BUY or SELL")
        Price = float(input("At which price?"))
        amount = float(input("How much amount"))
        trade = (pair, direction, Price, amount)
        new_entries.append(trade)
    return new_entries

def vol_calculator(trade_list): #function for calculating volume
    volume = 0
    for i in range(len(trade_list)):
        volume = volume + (trade_list[i][2] * trade_list[i][3])
    return volume


num = int(input("How many trades have you taken")) # asking user if he has any new trade
if num > 0:
    x = new_trade(num)
    trade_list.extend(x) #updating the trade list
    
choice = input("Do you want to calculate volume? Enter 1 for Yes 0 for No") # asking user if he want to calculate volume or not
if choice == '1':
    volume = vol_calculator(trade_list)
    print(volume)




