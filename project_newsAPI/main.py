import requests
from send_email import send_email

# Extracting pre-requisites
topic = "tesla"
api_key = "c6c55f26caeb4a76aecc6c4c29818759"
url = f"https://newsapi.org/v2/everything?q={topic}&from=2024-06-12&sortBy=publishedAt&apiKey=c6c55f26caeb4a76aecc6c4c29818759&language=en"

# Make request
request = requests.get(url)

# Get a dictionary of data
content = request.json()

# Access the news title and description
body = ""

for article in content["articles"][:20]:
    if article["title"] is not None:
        body ="Subject: Today's News" + "\n" + body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)