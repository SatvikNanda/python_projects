from flask import Flask, render_template, request

app = Flask(__name__)


# Handling http request
@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        date = request.form["date"]
        occupation = request.form["occupation"]

        print(first_name, last_name, email, date, occupation)



    return render_template("index.html") #render template calls the index.html file





app.run(debug=True, port=5001)