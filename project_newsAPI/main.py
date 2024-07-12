import requests
from send_email import send_email

# Extracting pre-requisites
api_key = "c6c55f26caeb4a76aecc6c4c29818759"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-06-12&sortBy=publishedAt&apiKey=c6c55f26caeb4a76aecc6c4c29818759"

# Make request
request = requests.get(url)

# Get a dictionary of data
content = request.json()

# Access the news title and description
body = ""

for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)