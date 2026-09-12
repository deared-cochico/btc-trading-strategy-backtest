import pandas as pd
import numpy as np

df = pd.read_csv("btc_backtest_results.csv")

# Tracks the highest value reached so far, at each point in time (never decreases)
def max_drawdown(growth_series):
    running_max = growth_series.cummax()
    # How far below that peak you are right now, as a percentage
    drawdown = (growth_series - running_max) / running_max
    # Worst (most negative) drop across the whole period
    return drawdown.min()

# Reward per unit of risk taken, scaled to a yearly figure.
# Closer to zero/positive = better. More negative = worse.
def sharpe_ratio(returns, periods_per_year=365):
    return (returns.mean() / returns.std()) * np.sqrt(periods_per_year)

# dropna() removes blank rows entirely (rather than filling them in)
# since mean()/std() can't handle blanks, and there's no sensible value to fill in here
strategy_returns = df["strategy_return"].dropna()
buyhold_returns = df["daily_return"].dropna()

print("=== Buy & Hold ===")
print(f"Final value: {df['buy_hold_growth'].iloc[-1]:.2f}")
print(f"Max drawdown: {max_drawdown(df['buy_hold_growth']):.2%}")
print(f"Sharpe ratio: {sharpe_ratio(buyhold_returns):.2f}")

print("\n=== Strategy ===")
print(f"Final value: {df['strategy_growth'].iloc[-1]:.2f}")
print(f"Max drawdown: {max_drawdown(df['strategy_growth']):.2%}")
print(f"Sharpe ratio: {sharpe_ratio(strategy_returns):.2f}")

# Count only rows where the signal actually flipped (real buy/sell moments)
trades = df[df["signal"].diff() != 0]
print(f"\nNumber of trades: {len(trades)}")