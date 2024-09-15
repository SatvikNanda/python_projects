import requests
import selectorlib
import smtplib, ssl
import os
import time
import sqlite3

URL = "https://programmer100.pythonanywhere.com/tours/"


connection = sqlite3.connect("project_music_webScraper/data.db")


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
    row = extracted.split(",")
    row = [item.strip() for item in row]

    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
    connection.commit()


def read(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    band_name, city_name, date = row

    cursor = connection.cursor()

    #query data
    cursor.execute("SELECT * FROM events WHERE band_name=? AND city_name=? AND date=?", (band_name,city_name,date))
    rows = cursor.fetchall()
    print(rows)

    return rows

if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)

        print(extracted)

        if extracted != "No upcoming tours":
            row = read(extracted)
            if not row:
                store(extracted)
                send_email(message="Hey, new event was found!")
        time.sleep(2)

    