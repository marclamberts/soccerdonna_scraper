import argparse
from .scraper import run_scraper

def main():
    parser = argparse.ArgumentParser(description="Scrape Soccerdonna league data")
    parser.add_argument("league_url", help="URL of the league on Soccerdonna")
    parser.add_argument("-o", "--output", default="league_players.xlsx", help="Output Excel file")
    args = parser.parse_args()

    run_scraper(args.league_url, args.output)
