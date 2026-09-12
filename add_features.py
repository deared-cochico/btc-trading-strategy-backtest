import pandas as pd

# Load the price data saved earlier
df = pd.read_csv("btc_daily_prices.csv")

# CSV stores dates as text, convert back to real dates
df["date"] = pd.to_datetime(df["date"])

# 7-day and 30-day moving averages, sliding window average, recalculated each day
df["ma_7"] = df["price"].rolling(window=7).mean()
df["ma_30"] = df["price"].rolling(window=30).mean()

# Daily % change vs the previous day
df["daily_return"] = df["price"].pct_change()

# Standard deviation = typical distance of values from their average.
# Bigger = more spread out/volatile. Rolling 30-day window of daily returns.
df["volatility_30"] = df["daily_return"].rolling(window=30).std()

# Save as CSV, index=False skips adding pandas' row-number column
df.to_csv("btc_with_features.csv", index=False)

# Show last 10 rows, the end of the data is where all rolling windows are full
print(df.tail(10))

# Confirm how many rows were saved
print(f"\nSaved {len(df)} rows with features to btc_with_features.csv")