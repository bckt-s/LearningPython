import argparse
from pathlib import Path
from chat_scraper.scraper import scrape_page

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Scrape a webpage and save to CSV.")
    parser.add_argument("url", help="The URL of the page to scrape")
    parser.add_argument("-o", "--output", default="scraped_data.csv", help="Output CSV file")
    return parser

def main() -> None:
    args = build_parser().parse_args()

    print(f"Scraping: {args.url} ...")
    rows = scrape_page(args.url)

    csv_path = Path(args.output)
    csv_path.write_text("\n".join(rows), encoding="utf-8")

    print(f"✅ Saved {len(rows)} rows to {csv_path.resolve()}")

if __name__ == "__main__":
    main()
