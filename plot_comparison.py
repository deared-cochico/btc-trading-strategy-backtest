import pandas as pd
import matplotlib.pyplot as plt

# opens and loads the csv
df = pd.read_csv("btc_backtest_results.csv")

# csv stores dates as text, so convert back to real dates every time we reload
df["date"] = pd.to_datetime(df["date"])

# size of the chart
plt.figure(figsize=(10, 5))

# draws a line connecting date vs buy_hold_growth, and another for strategy_growth
plt.plot(df["date"], df["buy_hold_growth"], label="Buy & Hold")
plt.plot(df["date"], df["strategy_growth"], label="Strategy")

# the title above the graph
plt.title("Growth of $1: Buy & Hold vs Strategy")

# the labels on x-axis and y-axis
plt.xlabel("Date")
plt.ylabel("Value of $1")

# automatically gives a small box with each line's color and label
plt.legend()

# auto-adjusts spacing so labels/titles don't get cut off at the edges when saved
plt.tight_layout()

# save the chart to a png
plt.savefig("comparison_chart.png")

# this opens the graph
plt.show()