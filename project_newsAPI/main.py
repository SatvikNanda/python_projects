import requests
from send_email import send_email

# Extracting pre-requisites
topic = "tesla"
api_key = "56daefbaafbc4640b069bd6b695852f9" #sample apikey, hence not hidden
url = f"https://newsapi.org/v2/everything?q=tesla&from=2024-06-25&sortBy=publishedAt&apiKey=56daefbaafbc4640b069bd6b695852f9&language=en"

# Make request
response = requests.get(url)

# Get a dictionary of data
content = response.json()


# Access the news title and description
body = ""

for article in content["articles"][:20]:
    if article["title"] is not None:
        body ="Subject: Today's News" + "\n" + body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)