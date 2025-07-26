import requests
import json

# Step 1: GET request to the API
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# Step 2: Check if it worked
if response.status_code == 200:
    # Step 3: Convert response to Python dictionary
    data = response.json()

    # Step 4: Print it nicely
    print(json.dumps(data, indent=2))
else:
    print:(f"Requst failed with status code: {response.status_code}")