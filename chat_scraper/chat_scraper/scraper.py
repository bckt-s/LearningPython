import requests
from bs4 import BeautifulSoup

def scrape_page(url: str) -> list[str]:
    res = requests.get(url, timeout=10)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")
    rows = []

    for tag in soup.select("hr, h2, h3"):
        rows.append(f"{tag.name},{tag.get_text(strip=True)}")

    return rows