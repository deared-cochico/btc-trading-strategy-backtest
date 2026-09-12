# BTC Trading Strategy Backtest

## Business Question
Would a simple moving-average-based strategy have protected capital better
than just buying and holding BTC over the past year?

## Approach
- Pulled 365 days of daily BTC price data (CoinGecko API)
- Built 7-day and 30-day moving averages to detect trend direction
- Strategy: hold BTC when the 7-day average is above the 30-day average,
  hold cash otherwise
- Backtested against simply buying and holding for the same period

## Findings
- Buy & Hold: ended at $0.68 per $1 invested (-32%), max drawdown -53%
- Strategy: ended at $0.93 per $1 invested (-7%), max drawdown -21%
- Strategy made 16 trades over the year
- Neither approach was profitable, it was a down year for BTC, but the
  strategy significantly reduced losses and downside risk (Sharpe ratio
  -0.18 vs -0.67)

## Recommendation
The moving-average strategy is better suited as a downside-risk reducer
than a profit generator. Future iterations could test different window
lengths, add stop-losses, or combine with volatility filters.