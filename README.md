# news-scraper-stock-data-EDA

This project demonstrates:
https://news-scraper-stock-data-eda-m7kszm926fmjw39ucepxn.streamlit.app/
* Web scraping of financial news from Yahoo Finance
* Extraction of titles, tickers, sources, and news links
* Integration with real stock price data (using yfinance)
* Exploratory Data Analysis (EDA) and visualization of the news and market data
<img width="899" height="443" alt="proj1EDA" src="https://github.com/user-attachments/assets/248123a6-7489-49ae-be6e-8ef81b7c46e3" />
---
Step-by-Step Workflow

1. Data Collection

* data_collection.py
Scrapes Yahoo Finance for financial news. Extracts:
  * Title
  * Tickers mentioned
  * Source of the article
  * Article link
  * Time of publication
Saves results in Articles.json and/or news_title.json.

2. Data Preparation

* news_title.json
Contains structured and cleaned news data as a list of dictionaries, ready for analysis.
* Top Tickers Extraction
In eda_visualization.py, tickers mentioned in the news are counted using Python’s Counter to identify the most frequently mentioned stocks.
* Stock Price Data Download
Using the yfinance library, historical stock price data for the top tickers is downloaded (last 7 days) and saved in stock_data.csv.

3. Exploratory Data Analysis & Visualization

* eda_visualization.py
Performs EDA using pandas and matplotlib:
  * Loads stock data and top tickers
  * Plots closing prices of top mentioned stocks over time
  * Plots daily trading volume for these stocks
  * (Optional: Overlay news events for advanced analysis)

## Key code steps:

### Find top 3 tickers by news mentions

### Plot Closing Prices

### Plot Trading Volume
---

Files Explained

* Articles.json
Raw JSON with all scraped news articles and metadata.
* news_title.json
Cleaned/structured list of articles (title, tickers, source, link, time) for easy loading in analysis scripts.
* stock_data.csv
Historical OHLCV (Open, High, Low, Close, Volume) price data for top tickers, as columns, indexed by date.
* data_collection.py
Python script to scrape Yahoo Finance and output JSON files.
* eda_visualization.py
Jupyter or script file for EDA, visualization, and insights generation.
* numerica_data.py
(Customize: Use for additional number crunching, statistics, or summary table generation.)
* main.py
Entry point; may call the data collection, analysis, or serve as a runner script for the project.
=======
