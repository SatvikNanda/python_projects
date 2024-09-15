import sqlite3

#establish connection and cursor
connection = sqlite3.connect("project_music_webScraper/data.db")
cursor = connection.cursor()

#query data
cursor.execute("SELECT * FROM events WHERE band_name='Tigers'")

rows = cursor.fetchall()
print(rows)

#insert new rows
new_rows = [('Cats', 'Cat City', '2088.10.17'),
            ('Hens', 'Hen City', '2088.10.20')]

cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()

cursor.execute("SELECT * FROM events")
rows2 = cursor.fetchall()
print(rows2)