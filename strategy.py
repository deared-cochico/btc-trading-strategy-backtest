import pandas as pd

df = pd.read_csv("btc_with_features.csv")
df["date"] = pd.to_datetime(df["date"])

# Signal: 1 = hold BTC (ma_7 above ma_30, looks like an uptrend)
#         0 = hold cash (ma_7 below ma_30, looks like a downtrend)
df["signal"] = (df["ma_7"] > df["ma_30"]).astype(int)

# Difference from yesterday's signal: 1 = just bought, -1 = just sold, 0 = no change
df["position_change"] = df["signal"].diff()

# Show only the days a trade actually happened
print(df[df["position_change"] != 0][["date", "price", "ma_7", "ma_30", "signal"]])

df.to_csv("btc_with_signals.csv", index=False)
print(f"\nSaved signals to btc_with_signals.csv")