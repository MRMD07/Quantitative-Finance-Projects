from ast import And
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #importing imp libraries


data = pd.read_csv("Karachi 100 Historical Data.csv")

#Making sure data is in correct format e.g remobing ','
data['Price'] = data['Price'].str.replace(',','',regex = False).astype(float)
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values(by = 'Date', ascending= True, inplace = True)
data.reset_index(drop = True, inplace = True)

#Calculating mean
data['Rolling_mean'] = data['Price'].rolling(window = 5).mean()

date = np.array(data['Date'])
price = np.array(data['Price'])

change =(( price[1:]-price[:-1])/price[:-1])*100

start_window = pd.to_datetime('2026-04-06')
end_window = pd.to_datetime('2026-04-17')
window =( data['Date']>= start_window)&( data['Date']<= end_window)

change = np.insert(change, 0, 0)
data['Changes']= change

window_returns = data.loc[window, 'Changes']
stdv = np.std(data['Changes'])

print(stdv)
print(data.loc[window,['Date','Changes']])

# Create a 2-story plotting layout (Top chart for Price, Bottom chart for Changes)
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(11, 7))


# TOP PANEL: KSE-100 Price and Moving Average
ax1.plot(data['Date'], data['Price'], label='KSE-100 Closing Price', color='#1f77b4', linewidth=2)
ax1.plot(data['Date'], data['Rolling_mean'], label='5-Day Moving Average', color='#ff7f0e', linestyle='--')

# Vertical line marking the Monday market reaction right after the weekend talks
ax1.axvline(x=pd.to_datetime('2026-04-13'), color='red', linestyle=':', linewidth=2, label='Post-Talks Market Opening')

ax1.set_title('KSE-100 Macro Response Analysis (April 2026)', fontsize=13, fontweight='bold')
ax1.set_ylabel('Index Points', fontsize=11)
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(loc='upper left')


# Plot daily returns as a distinct line chart
ax2.plot(data['Date'], data['Changes'], label='Daily Return %', color='#2ca02c', linewidth=1.5)

# Draw the horizontal standard deviation boundary lines (Upper and Lower noise limits)
ax2.axhline(y=stdv, color='purple', linestyle=':', alpha=0.7, label=f'Volatility Threshold (±{stdv:.2f}%)')
ax2.axhline(y=-stdv, color='purple', linestyle=':', alpha=0.7)

# Vertical line marking the Monday market reaction on the returns axis too
ax2.axvline(x=pd.to_datetime('2026-04-13'), color='red', linestyle=':', linewidth=2)

ax2.set_ylabel('Daily Change %', fontsize=11)
ax2.set_xlabel('Timeline', fontsize=11)
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(loc='upper left')

# Adjust layout padding so text elements don't overlap
plt.tight_layout()

# Save the plot automatically as a crisp image for your pitch attachment
plt.savefig("kse100_geopolitical_analysis.png", dpi=300)
print("\nSuccess! Chart compiled and saved as 'kse100_geopolitical_analysis.png'")

# Display the dashboard layout on your screen
plt.show()