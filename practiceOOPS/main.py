import requests
import selectorlib
import smtplib, ssl
import os
import time
import sqlite3

URL = "https://programmer100.pythonanywhere.com/tours/"




class Event:
    def scrape(self, url):
        """Scrape the page source from URL"""
        response = requests.get(url)
        source = response.text
        return source

    def extract(self, source):
        extractor = selectorlib.Extractor.from_yaml_file("project_music_webScraper/extract.yaml")
        value = extractor.extract(source)["tours"]
        return value


class Email:
    def send(self, message):
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


class Database:
    def __init__(self, database_path):
        self.connection = sqlite3.connect(database_path)

    def store(self, extracted):
        row = extracted.split(",")
        row = [item.strip() for item in row]

        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
        self.connection.commit()


    def read(self, extracted):
        row = extracted.split(",")
        row = [item.strip() for item in row]
        band_name, city_name, date = row

        cursor = self.connection.cursor()

        #query data
        cursor.execute("SELECT * FROM events WHERE band_name=? AND city_name=? AND date=?", (band_name,city_name,date))
        rows = cursor.fetchall()
        print(rows)

        return rows

if __name__ == "__main__":
    while True:
        event = Event() # calling the Event class
        scraped = event.scrape(URL) # these are no longer functions, these are methods
        extracted = event.extract(scraped)

        print(extracted)

        if extracted != "No upcoming tours":
            database = Database(database_path="project_music_webScraper/data.db")
            row = database.read(extracted)
            if not row:
                database.store(extracted)

                email = Email()
                email.send(message="Hey, new event was found!")
        time.sleep(2)

    