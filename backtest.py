import pandas as pd

df = pd.read_csv("btc_with_signals.csv")
df["date"] = pd.to_datetime(df["date"])

# Today's strategy return = today's price return, but only counted if
# yesterday's signal said "hold BTC" (shift(1) avoids lookahead bias)
df["strategy_return"] = df["daily_return"] * df["signal"].shift(1)

# Compounding chain: each day's value = yesterday's running value x (1 + today's return).
# cumprod() does this multiplication chain automatically for every row, so we don't
# have to build the running total by hand.
df["buy_hold_growth"] = (1 + df["daily_return"]).cumprod()

# Same compounding chain, but using the strategy's returns instead of raw price returns.
# fillna(0) fills blank rows (e.g. day 1, which has no prior day to shift from) with
# 0% change, so cumprod() doesn't break when it hits a blank value.
df["strategy_growth"] = (1 + df["strategy_return"].fillna(0)).cumprod()

# .iloc[-1] grabs the last row — the final compounded value after all days
final_buy_hold = df["buy_hold_growth"].iloc[-1]
final_strategy = df["strategy_growth"].iloc[-1]

# :.2f rounds the printed number to 2 decimal places
print(f"Buy & Hold final value (per $1): {final_buy_hold:.2f}")
print(f"Strategy final value (per $1): {final_strategy:.2f}")

df.to_csv("btc_backtest_results.csv", index=False)