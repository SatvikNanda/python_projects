import requests
import selectorlib
import smtplib, ssl
import os

URL = "https://programmer100.pythonanywhere.com/tours/"

def scrape(url):
    """Scrape the page source from URL"""
    response = requests.get(url)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("project_music_webScraper/extract.yaml")
    value = extractor.extract(source)["tours"]
    return value

def send_email(message):
    host = "smtp.gmail.com"
    port = 465


    username = "satvik.nanda@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "satvik.nanda@gmail.com"


    context  = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context = context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
    print("Email was sent successfully!")

def store(extracted):
    with open("project_music_webScraper/data.txt", "a") as file:
        file.write(extracted + "\n")


def read():
    with open("project_music_webScraper/data.txt", "r") as file:
        return file.read()

if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    
    content = read()

    print(extracted)

    if extracted != "No upcoming tours":
        if extracted not in content:
            store(extracted)
            send_email(message="Hey, new event was found!")

    