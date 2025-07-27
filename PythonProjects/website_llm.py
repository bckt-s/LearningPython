import csv
import subprocess

items = []

# Read scraped data
with open('scraped_data.csv', 'r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if row:
            items.append(row[0])

# Format the data into a readable list
formatted = '\n- ' + '\n- '.join(items)

# LLM prompt
prompt = f"""You are a smart content analyst.

Below is a list of items scraped from a website.

Please analyze the content and answer:
1. What kind of website does this likely come from?
2. What topics or themes does it focus on?
3. Why might someone scrape this data?
4. What insights or categories can be derived?

Scraped content:
{formatted}
"""

# Run the local LLM using subprocess
def run_llm(prompt):
    result = subprocess.run(
        ['ollama', 'run', 'mistral'],
        input=prompt.encode(),
        stdout=subprocess.PIPE
    )
    return result.stdout.decode()

response = run_llm(prompt)
print(response)

