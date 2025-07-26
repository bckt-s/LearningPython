import requests
import json
from bs4 import BeautifulSoup
import subprocess

TOP_STORIES_URL = 'https://hacker-news.firebaseio.com/v0/topstories.json'

# Step 1: Fetch top story IDs
response = requests.get(TOP_STORIES_URL)

if response.status_code == 200:
    data = response.json()
    top_ids = data[:5]

    # Step 2: Show top 5 stories
    for i, story_id in enumerate(top_ids, 1):
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        story_response = requests.get(story_url)

        if story_response.status_code == 200:
            story_data = story_response.json()
            title = story_data.get("title")
            score = story_data.get("score")
            url = story_data.get("url", "[no URL provided]")

            print(f"\n{i}. {title}")
            print(f"    Score: {score}")
            print(f"    URL: {url}")

    # Step 3: Choose a story to summarize
    choice = input("\nWhich story do you want to summarize? (1-5): ")
    user_index = int(choice) - 1
    chosen_id = top_ids[user_index]

    story_url = f"https://hacker-news.firebaseio.com/v0/item/{chosen_id}.json"
    story_response = requests.get(story_url)
    story_data = story_response.json()

    title = story_data.get("title")
    url = story_data.get("url", "[no URL provided]")

    if url.startswith("http"):  # Only fetch if URL is valid
        # Step 4: Fetch article HTML
        page = requests.get(url, timeout=10)
        soup = BeautifulSoup(page.text, 'html.parser')

        # Step 5: Extract main content (all paragraphs)
        paragraphs = soup.select('p')
        article_text = '\n'.join([p.get_text(strip=True) for p in paragraphs])

        # Optional: trim super long articles
        article_text = article_text[:3000]

        # Step 6: Build Mistral prompt
        prompt = f"""You are a professional summarizer. Read the article below and summarize it into a single 8-10 sentence paragraph. Focus on clarity and the most important details.

Article:
{article_text}
"""

        # Step 7: Send to Mistral
        def run_llm(prompt):
            result = subprocess.run(
                ['ollama', 'run', 'mistral'],
                input=prompt.encode(),
                stdout=subprocess.PIPE
            )
            return result.stdout.decode()

        summary = run_llm(prompt)

        print("\n💬 Summary:")
        print(summary)

    else:
        print("No valid URL to fetch article content.")
else:
    print(f"Request failed with status code: {response.status_code}")
