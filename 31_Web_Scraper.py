import requests
from bs4 import BeautifulSoup

def get_bbc_headlines():
    url = "https://www.bbc.com/news"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = []
    for headline in soup.find_all('h3'):
        text = headline.get_text(strip=True)
        if text and text not in headlines:
            headlines.append(text)

    return headlines

if __name__ == "__main__":
    bbc_headlines = get_bbc_headlines()
    print("BBC News Headlines:\n")
    for idx, title in enumerate(bbc_headlines, 1):
        print(f"{idx}. {title}")
        
