import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def extract_headlines(html):
    soup = BeautifulSoup(html, 'html.parser')
    headlines = [h.get_text() for h in soup.find_all(['h1', 'h2', 'h3'])]
    return headlines
