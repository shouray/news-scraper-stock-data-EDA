
import pandas as pd
import json
from collections import Counter
import matplotlib.pyplot as plt
# Load your CSV file
df = pd.read_csv('data/raw/stock_data.csv', parse_dates=['Date'])
df.set_index('Date', inplace=True)
df.head()


with open("data/raw/news_title.json", "r") as f:
    df_ticker = pd.DataFrame(json.load(f))

all_tickers = [t for tickers in df_ticker['ticker'] for t in tickers]
top_tickers = Counter(all_tickers).most_common(3)
ticker_list = [t[0] for t in top_tickers]

plt.figure(figsize=(12, 6))
for ticker in ticker_list:
    plt.plot(df.index, df[f'{ticker}_Close'], marker='o', label=ticker)

plt.title('Closing Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 4))
for ticker in ticker_list:
    plt.plot(df.index, df[f'{ticker}_Volume'], marker='.', label=ticker)
plt.title('Daily Trading Volume')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.legend()
plt.grid(True)
plt.show()

for ticker in ticker_list:
    returns = df[f'{ticker}_Close'].pct_change()
    plt.plot(df.index, returns, marker='.', label=f'{ticker} Return')
plt.title('Daily Returns')
plt.xlabel('Date')
plt.ylabel('Return')
plt.legend()
plt.grid(True)
plt.show()

