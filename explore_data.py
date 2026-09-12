import pandas as pd
import matplotlib.pyplot as plt

# Load the data saved earlier
df = pd.read_csv("btc_daily_prices.csv")

# CSV stores dates as text — convert back to real dates
df["date"] = pd.to_datetime(df["date"])

# Quick structure check: columns, types, non-empty counts
print(df.info())

# Count missing values per column — should be 0 if data is clean
print("\nMissing values:\n", df.isnull().sum())

# Min, max, average, and spread of the price column
print("\nSummary stats:\n", df["price"].describe())

# Build and save a line chart of price over time
# Set the size of the chart (width, height in inches)
plt.figure(figsize=(10, 5))

# Plot date along the x-axis, price along the y-axis, connect the dots
plt.plot(df["date"], df["price"])

# Chart title, shown at the top
plt.title("BTC Daily Price - Last 365 Days")

# Label for the x-axis
plt.xlabel("Date")

# Label for the y-axis
plt.ylabel("Price (USD)")

# Auto-adjust spacing so labels don't get cut off at the edges
plt.tight_layout()

# Save the chart as an image file in your project folder
plt.savefig("btc_price_chart.png")

# Open a window to actually display the chart
plt.show()