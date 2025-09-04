import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "https://www.soccerdonna.de"
WSL_URL = f"{BASE_URL}/en/kvindeliga/startseite/wettbewerb_3FL.html"
HEADERS = {"User-Agent": "Mozilla/5.0"}

# Step 1: Get club URLs
def get_club_urls():
    resp = requests.get(WSL_URL, headers=HEADERS)
    soup = BeautifulSoup(resp.content, 'html.parser')
    club_links = {}

    for row in soup.select("table.standard_tabelle tr.hell"):
        a = row.select_one("td:nth-of-type(2) a")
        if a:
            name = a.get_text(strip=True)
            href = a.get("href", "")
            if "/verein_" in href:
                full_url = BASE_URL + href
                club_links[name] = full_url
    return club_links

# Step 2: Get player URLs
def get_player_urls(club_url):
    player_urls = []
    resp = requests.get(club_url, headers=HEADERS)
    soup
