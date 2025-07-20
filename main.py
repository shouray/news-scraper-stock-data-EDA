import json
# from Scraper.scraper import YahooNewsScraper
from Files.data_collection import YahooNewsScraper


scraper = YahooNewsScraper()
news = scraper.fetch_news(limit=50)


# Save raw headlines, which further will be used to scrape the news content.
with open("data/raw/news_title.json", "w") as f:
    json.dump(news, f, indent=2)
print("Raw news saved to data/raw/news_titles.json")