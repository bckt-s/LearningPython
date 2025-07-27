#!/usr/bin/env python3
"""
Chatbot-Guided Web Scraper with Friendly Selector Bank

1. Greet & mood-check.
2. Ask for URL once.
3. Loop: ask for CSS selector or friendly term (type 'help').
   • If 'help', show bank of simple terms.
   • If pick a term, map it to its real selector.
   • If custom, accept raw CSS.
4. Download & parse page, catching bad selectors or no matches.
5. Show sample items.
6. Offer to save to CSV.
"""

import sys
import csv
import requests
from bs4 import BeautifulSoup
from soupsieve import SelectorSyntaxError

# ───────────────────────────────────────────────────────────
# 1) Mood & Name Helpers
# ───────────────────────────────────────────────────────────
def get_name():
    return input("Hello! What's your name? ").strip()

def evaluate_mood(user):
    prompt = f"How are you doing today, {user}? (good/bad) "
    messages = {
        "good": f"Amazing! It's good to hear that, {user}.",
        "bad":  f"Sorry to hear that, {user}. Hopefully tomorrow is brighter."
    }
    while True:
        resp = input(prompt).strip().lower()
        if resp in messages:
            print(messages[resp])
            return resp
        prompt = f"Please answer 'good' or 'bad', {user}: "

# ───────────────────────────────────────────────────────────
# 2) Selector Bank & Prompt
# ───────────────────────────────────────────────────────────
# A mapping of friendly terms → (CSS selector, description)
SELECTOR_BANK = {
    "link":       ("a",             "All clickable links on the page."),
    "header":     ("h1, h2, h3",    "Main titles and subtitles (headers)."),
    "paragraph":  ("p",             "Blocks of paragraph text."),
    "image":      ("img",           "Images embedded in the page."),
    "list_item":  ("li",            "Items in lists (e.g., menus)."),
    "button":     ("button",        "All <button> elements."),
    "table_row":  ("tr",            "Rows in any table."),
}

def get_scrape_selector():
    """
    Prompt for a selector term or raw CSS.
    Typing 'help' shows a friendly bank of terms.
    Returns a real CSS selector string.
    """
    help_text = ["\nYou can use these simple terms:"]
    for term, (_css, desc) in SELECTOR_BANK.items():
        help_text.append(f"  • {term:<10} → {desc}")
    help_text.append("Or type 'custom' to enter your own CSS selector.")
    help_text = "\n".join(help_text)

    while True:
        sel = input("Enter selector term or 'help': ").strip().lower()

        if sel == 'help':
            print(help_text)
            continue

        if sel == 'custom':
            raw = input("Enter your CSS selector (e.g. '.my-class', '#id'): ").strip()
            if raw:
                return raw
            else:
                print("Selector cannot be blank. Try again.")
                continue

        # If user picked a friendly term:
        if sel in SELECTOR_BANK:
            css, _ = SELECTOR_BANK[sel]
            print(f"You chose '{sel}', which means CSS selector: {css}")
            return css

        # Unknown input:
        print(f"Unrecognized term '{sel}'. Type 'help' to see options, or 'custom'.")

# ───────────────────────────────────────────────────────────
# 3) Download & Parse Helpers
# ───────────────────────────────────────────────────────────
def download_page(url):
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        return resp.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_items(html, selector):
    soup = BeautifulSoup(html, 'html.parser')
    # May raise SelectorSyntaxError if selector is malformed
    elems = soup.select(selector)
    return [el.get_text(strip=True) for el in elems]

# ───────────────────────────────────────────────────────────
# 4) Confirm & Save
# ───────────────────────────────────────────────────────────
def confirm_and_save(items):
    print("\nSample items:")
    for i, it in enumerate(items[:5], 1):
        print(f"{i}. {it}")
    choice = input(f"\nSave all {len(items)} items to 'scraped_data.csv'? (yes/no) ").strip().lower()
    if choice == 'yes':
        with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Item'])
            for it in items:
                writer.writerow([it])
        print("Data saved to 'scraped_data.csv'.")
    else:
        print("Data not saved.")

# ───────────────────────────────────────────────────────────
# 5) Main Flow with Retry Loop
# ───────────────────────────────────────────────────────────
def main():
    user = get_name()
    _ = evaluate_mood(user)

    url = input("Enter the full URL to scrape: ").strip()
    html = download_page(url)
    if html is None:
        print("Could not retrieve page; exiting.")
        sys.exit(1)

    while True:
        selector = get_scrape_selector()

        try:
            items = parse_items(html, selector)
        except SelectorSyntaxError as err:
            print(f"Invalid CSS selector: {err}")
            retry = input("Try again? (yes/no) ").strip().lower()
            if retry == 'yes':
                continue
            print("Exiting.")
            sys.exit(1)

        if not items:
            print(f"No items matched selector '{selector}'.")
            retry = input("Try a different selector? (yes/no) ").strip().lower()
            if retry == 'yes':
                continue
            print("Exiting.")
            sys.exit(1)

        # Found items: break out
        break

    confirm_and_save(items)
    print("Thank you for using Chat-Scraper! Goodbye.")

if __name__ == "__main__":
    main()
