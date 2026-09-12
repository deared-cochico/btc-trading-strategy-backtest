import requests
import pandas as pd

# CoinGecko API endpoint for Bitcoin price history
url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"

params = {
    "vs_currency": "usd",
    "days": "365",       # last 1 year
    "interval": "daily"
}

response = requests.get(url, params=params)
data = response.json()

# Pull out the price list, ignore volume/market cap
prices = data["prices"]

df = pd.DataFrame(prices, columns=["timestamp", "price"])

# Convert timestamp (ms since 1970) into a readable date
df["date"] = pd.to_datetime(df["timestamp"], unit="ms")

# Keep only the columns we need
df = df[["date", "price"]]

# Save as CSV, index=False skips adding pandas' row-number column to the file
df.to_csv("btc_daily_prices.csv", index=False)

# Quick visual check, show first 5 rows in the terminal
print(df.head())

# Confirm how many rows were saved
print(f"\nSaved {len(df)} rows to btc_daily_prices.csv")