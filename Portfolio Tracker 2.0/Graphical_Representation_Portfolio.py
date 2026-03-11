import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("btc_data.csv")
data.dropna(inplace=True) #Cleaning data
holdings = float(input("How much btc do you hold?"))
#Fixing dates
data['Date']=pd.to_datetime(data['Date'])
#Setting index to date
data.set_index('Date', inplace=True)

portfolio = data['Price']*holdings

#Plotting graph
portfolio.plot()
plt.title("Portfolio Over Time")
plt.show()
