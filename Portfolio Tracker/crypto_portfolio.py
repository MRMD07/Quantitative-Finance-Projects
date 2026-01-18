Name = []
Price = []
Holdings = []
count = input("How many coins do you have")
count = int(count)
for x in range(0,count):
    n = input("Enter the name of coin")
    Name.append(n)
    p = input("Enter the price of the coin")
    Price.append(p)
    h = input("Enter the amount of holding")
    Holdings.append(h)

def portfolio_tracker(Name, Price, Holdings):
    total_portfolio_value = 0
    for index, coin in enumerate(Name):
        value = float(Holdings[index]) * float(Price[index])
        total_portfolio_value += value
    return total_portfolio_value
final = portfolio_tracker(Name, Price, Holdings)
print("Total portfolio value is", final)