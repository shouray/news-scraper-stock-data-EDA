import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud
import json
from datetime import datetime, timedelta
import pandas as pd
import yfinance as yf
import mplfinance as mpf
from datetime import datetime, timedelta


with open("data/raw/news_title.json", "r") as f:
    df = pd.DataFrame(json.load(f))

all_tickers = [t for tickers in df['ticker'] for t in tickers]
top_tickers = Counter(all_tickers).most_common(3)
ticker_list = [t[0] for t in top_tickers]

start_date = datetime.now() - timedelta(days=7)
end_date = datetime.now()

# Download data for the list of tickers
data = yf.download(ticker_list, start=start_date, end=end_date, group_by='ticker')

# Save to CSV, flatten MultiIndex columns for easier reading later
data.columns = ['_'.join(col).strip() if isinstance(col, tuple) else col for col in data.columns.values]
data.to_csv('data/raw/stock_data.csv')
