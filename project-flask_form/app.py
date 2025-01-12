from flask import Flask, render_template

app = Flask(__name__)


# Handling http request
@app.route("/")
def index():
    return render_template("index.html") #render template calls the index.html file





app.run(debug=True, port=5001)