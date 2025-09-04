import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "https://www.soccerdonna.de"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_league_url(league_code, comp_code):
    """
    Construct league URL from league_code and comp_code.
    Example:
        WSL + ENG1 -> https://www.soccerdonna.de/en/womens-super-league/startseite/wettbewerb_ENG1.html
    """
    return f"{BASE_URL}/en/{league_code}/startseite/wettbewerb_{comp_code}.html"

def get_club_urls(league_url):
    resp = requests.get(league_url, headers=HEADERS)
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

def get_player_urls(club_url):
    player_urls = []
    resp = requests.get(club_url, headers=HEADERS)
    soup = BeautifulSoup(resp.content, 'html.parser')
    for a in soup.select("table#spieler a.fb"):
        href = a.get("href", "")
        if "/profil/spieler_" in href:
            full_url = BASE_URL + href
            player_urls.append(full_url)
    return player_urls

def scrape_player_profile(player_url, club_name):
    data = {"Club": club_name, "Profile URL": player_url}
    resp = requests.get(player_url, headers=HEADERS)
    soup = BeautifulSoup(resp.content, 'html.parser')

    h1 = soup.select_one(".tabelle_spieler h1")
    data["Name"] = h1.get_text(strip=True) if h1 else None

    for tr in soup.select(".tabelle_grafik .tabelle_spieler tr"):
        tds = tr.select("td")
        if len(tds) == 2:
            key = tds[0].get_text(strip=True).strip(":")
            value = tds[1].get_text(strip=True, separator=" ")
            data[key] = value

    return data

def run_scraper(league_code, comp_code, output_file=None):
    """
    Scrape a league given its league_code and comp_code.
    Example: league_code="womens-super-league", comp_code="ENG1"
    """
    league_url = get_league_url(league_code, comp_code)
    if not output_file:
        output_file = f"{league_code}_{comp_code}_players.xlsx"

    clubs = get_club_urls(league_url)
    print(f"Found {len(clubs)} clubs in {league_code} ({comp_code})")

    all_players = []

    for club_name, club_url in clubs.items():
        print(f"\n🔍 Scraping club: {club_name}")
        player_urls = get_player_urls(club_url)
        print(f"  - Found {len(player_urls)} players")

        for p_url in player_urls:
            print(f"    ↳ {p_url}")
            try:
                player_data = scrape_player_profile(p_url, club_name)
                all_players.append(player_data)
                time.sleep(0.5)
            except Exception as e:
                print(f"Failed to scrape {p_url}: {e}")

    df = pd.DataFrame(all_players)
    df.to_excel(output_file, index=False)
    print(f"\n✅ Done. Data saved to {output_file}")
