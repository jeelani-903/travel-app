from flask import Flask, render_template, request, jsonify
from dbfunctions import *
from flask.globals import session

app = Flask(__name__)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        result = create_user(name, email, password)

        return render_template('register.html', result=result)

    return render_template('register.html')


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/about")
def about__us():
    return render_template("aboutus.html")


@app.route("/review")
def review():
    return render_template("Rating.html")


@app.route("/flight")
def flight():
    return render_template("flights.html")


@app.route("/credentials")
def credentials():
    return render_template("credentials.html")


@app.route("/book")
def book():
    return render_template("search.html")


@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        if login_validation(email, password):
            print("logged in")
            # session["logged_in"] = True
            return render_template("home.html", loggedIn=True)
        else:
            print("wrong password")
            return render_template("login.html", status="wrong password Try again")

    else:
        return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
