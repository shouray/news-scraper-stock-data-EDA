import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

'''
#TO DO:
#1. Add title of the article using scraping.
'''

class YahooNewsScraper:
    def __init__(self):
        self.url = "https://finance.yahoo.com/topic/stock-market-news/"

    def fetch_news(self, limit):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

        response = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # Select news items
        news_items = soup.select('ul[class*="stream-items"] li')[:limit]

        results = []
        for item in news_items:
            title_elem = item.find("h3")
            link_elem = item.find("a", href=True)
            news_source = item.find("div", class_=re.compile(r"publishing"))
            ticker_elem = item.findAll("span", class_=re.compile(r"symbol"))
            # print(news_source)
            if title_elem and link_elem:
                title = title_elem.get_text(strip=True)
                # Use urljoin to properly handle both relative and absolute URLs
                link = urljoin("https://finance.yahoo.com", link_elem["href"])
                source = news_source.get_text(strip=True)
                ticker = [ticker.get_text(strip=True) for ticker in ticker_elem]
                print(ticker)
                results.append({
                    "title": title,
                    "link": link,
                    "source": source.split("•")[0],
                    "time": source.split("•")[1],
                    "ticker": ticker
                })
        # print(results)
        return results

# scraper = YahooNewsScraper()
# print(scraper.fetch_news(1))