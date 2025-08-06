# 🧾 SOP – How to Run Chat-Scraper CLI

This guide walks you through installing and running the `chat-scrape` command-line tool to scrape webpage headings and save them to a CSV file.

---

## ✅ 1. Clone the Repository

```bash
git clone https://github.com/bckt-s/LearningPython
cd chat_scraper
```

---

## ✅ 2. Create and Activate a Virtual Environment

Create the virtual environment:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate    # (Windows)
```

You should now see `(.venv)` in your terminal prompt.

---

## ✅ 3. Install the Package (Editable Mode)

Install the package in editable mode:

```bash
pip install -e .
```

---

## ✅ 4. Install Required Dependencies

```bash
pip install requests beautifulsoup4
```

These are used to fetch and parse the webpage.

---

## ✅ 5. Run the Scraper Tool

To scrape headings and save to a CSV file:

```bash
chat-scrape https://www.bbc.com -o headlines.csv
```

- `url` is required (the page to scrape)
- `-o` or `--output` is optional (default is `scraped_data.csv`)

---

## 🧪 6. Example Output

Running:

```bash
chat-scrape https://www.bbc.com -o headlines.csv
```

Might create `headlines.csv` with:

```
h1,BBC News
h2,World
h3,Live Updates
...
```

---

## 🛠 7. Troubleshooting

- ❌ **Command not found?**  
  Make sure you activated the virtual environment:

  ```bash
  .venv\Scripts\activate
  ```

- ❌ **Empty CSV file?**  
  The page may not contain `<h1>`, `<h2>`, or `<h3>` tags  
  or it may use JavaScript to render content (not supported here).

- ❌ **Can't overwrite file?**  
  Make sure the file isn’t open in Excel or another program.

---

## 📌 Notes

- You can run this tool on different pages with different filenames.
- All scraping happens locally — no data is sent to external APIs.
