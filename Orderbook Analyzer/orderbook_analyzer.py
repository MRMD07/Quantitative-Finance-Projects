orders = [78000, 80000, 10000]
count = int(input("How many orders are placed"))

def new_order():
    temp_new_order = []
    for x in range(1,count+1):
     temp = int(input("Enter price of order"))
     temp_new_order.append(temp)
    return temp_new_order

if count > 0:
    new_orders = new_order()
    orders.extend(new_orders)

#creating dictionary for orderbook and automation for support and resistance levels
Price = int(input("Enter current price of BTC"))
orderbook = {}
resistance = {}
supports = {}
def orders_summary():
  for x in range(0,len(orders)):
    if orders[x] not in orderbook:
      orderbook[orders[x]] = 1
      if Price > orders[x]:
        supports[orders[x]] = 1
      else:
        resistance[orders[x]] = 1
    else:
      orderbook[orders[x]]+=1
      if Price > orders[x]:
        supports[orders[x]] += 1
      else:
        resistance[orders[x]] += 1
      

#asking user whether he wants the raw orderbook(dictionary) or not
choice = input("Do You want to know orders summary and automation for support and resistance levels? 1 FOR YES 0 FOR NO")
if choice == '1':
  orders_summary()
  print("Orderbook is {} Supports are {} Resistance are {}".format(orderbook,supports,resistance))

