#Importing the libraries
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

#Reading csv to convert it to dataframe
data = pd.read_csv("btc_data.csv")
Prices = data['Price']

#Making arrays for prices
Prices_array1 = np.array(Prices)
Prices_array2 = np.array(Prices)
Prices_array1 = Prices_array1[1:]
Prices_array2 = Prices_array2[:-1]
DailyReturn = ((Prices_array1 - Prices_array2)/Prices_array2)*100
DailyReturn_padded = np.insert(DailyReturn, 0, 0.0)

#Converting price back to Dataframe
temp_column = pd.DataFrame(DailyReturn_padded)


#Changing price column to differences column in our 'data' 
data['Price'] = temp_column

data = data.rename(columns = {'Date' : 'Date', 'Price': 'Differences'})
data.set_index('Date', inplace = True)

#plotting graph of returns
data.plot()
plt.title("My returns over time")
plt.ylabel('Returns')
plt.show()
