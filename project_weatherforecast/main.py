import os
from flask import Flask, render_template
import pandas as pd

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Create the Flask app and specify the templates folder
app = Flask(__name__, template_folder=os.path.join(current_dir, 'templates'))

stations = pd.read_csv("C:/Users/satvi/OneDrive/Desktop/python/udemy/project_weatherforecast/data_small/stations.txt", skiprows=17)
stations = stations[['STAID', 'STANAME                                 ']]
@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = "C:/Users/satvi/OneDrive/Desktop/python/udemy/project_weatherforecast/data_small/TG_STAID"+ str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    print("Temperature:", temperature)
    response_data = {
        "station": station,
        "date": date,
        "temperature": temperature
    }
    return response_data

@app.route("/api/v1/<station>")
def all_data(station):
    filename = "C:/Users/satvi/OneDrive/Desktop/python/udemy/project_weatherforecast/data_small/TG_STAID"+ str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient='records')
    return result

@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station, year):
    filename = "C:/Users/satvi/OneDrive/Desktop/python/udemy/project_weatherforecast/data_small/TG_STAID"+ str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df['    DATE'] = df['    DATE'].astype(str)
    result = df[df['    DATE'].str.startswith(str(year))].to_dict(orient='records')
    return result





if __name__ == "__main__":
    app.run(debug=True) #note that if you are running multiple apps then change the default from port 5000 to anything else to not clash
