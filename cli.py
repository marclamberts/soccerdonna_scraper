import argparse
from .scraper import run_scraper

def main():
    parser = argparse.ArgumentParser(description="Scrape Soccerdonna league data by league code and comp code")
    parser.add_argument("league_code", help="League code, e.g., womens-super-league")
    parser.add_argument("comp_code", help="Competition code, e.g., ENG1")
    parser.add_argument("-o", "--output", default=None, help="Output Excel file name")
    args = parser.parse_args()

    run_scraper(args.league_code, args.comp_code, args.output)
