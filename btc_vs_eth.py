import requests
import pandas as pd
# import data
btc = requests.get("https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=365")
eth = requests.get("https://api.coingecko.com/api/v3/coins/ethereum/market_chart?vs_currency=usd&days=365")
print(btc.status_code)
eth_r = eth.json()
btc_r = btc.json()
btc_data = btc_r['prices']
eth_data = eth_r['prices']
print(btc_data[0])
# Convert lists to DataFrames
df_btc = pd.DataFrame(btc_data, columns=['Date', 'BTC_Price'])
df_eth = pd.DataFrame(eth_data, columns=['Date', 'Market_Price'])
# Convert timestamp to readable date
df_btc['Date'] = pd.to_datetime(df_btc['Date'], unit='ms')
df_eth['Date'] = pd.to_datetime(df_eth['Date'], unit='ms')

# Set the Date as the index
# This moves the date from a regular column to the "row label" position
df_btc.set_index('Date', inplace=True)
df_eth.set_index('Date', inplace=True)

# Rename the columns
# If we don't do this, both columns might be named "Price" and we'll get confused later
df_btc.columns = ['BTC_Price']
df_eth.columns = ['Market_Price']

# Zip them together
# axis=1 means "side-by-side" (columns). axis=0 would be "top-to-bottom" (rows).
df = pd.concat([df_btc, df_eth], axis=1)

# Drop any rows where one coin has data but the other doesn't
df.dropna(inplace=True)

# --- VERIFY THE MERGE ---
print("Merge Successful!")
print(df.head()) 

# Calculate the % change from yesterday to today
df['BTC_Returns'] = df['BTC_Price'].pct_change()
df['Market_Returns'] = df['Market_Price'].pct_change()

df.dropna(inplace=True)

# print to confirm you see decimals like 0.01, -0.02
print(df[['BTC_Returns', 'Market_Returns']].head())
import matplotlib.pyplot as plt
import scipy.stats as stats  # Needed for the regression line

# Calculate the Linear Regression
# x = Eth, y = Bitcoin
slope, intercept, r_value, p_value, std_err = stats.linregress(df['Market_Returns'], df['BTC_Returns'])
beta = slope # The slope IS the Beta

print(f"Beta Calculated: {beta:.2f}")

# Create the Scatter Plot
plt.figure(figsize=(10, 6))

# Plot the dots
plt.scatter(df['Market_Returns'], df['BTC_Returns'], alpha=0.5, label='Daily Returns')

# Plot the line
x_line = df['Market_Returns']
y_line = slope * x_line + intercept
plt.plot(x_line, y_line, color='red', label=f'Regression Line (Beta={beta:.2f})')
plt.title(f'Bitcoin vs. Market (Beta: {beta:.2f})')
plt.xlabel('Market Returns (ETH)')
plt.ylabel('Bitcoin Returns')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

# Show the graph
plt.show()