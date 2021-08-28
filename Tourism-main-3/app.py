from collections import namedtuple
from typing import Text
from flask import Flask, render_template, request, jsonify, redirect
from flask.helpers import url_for
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


@app.route("/flight HtoC")
def flight1():
    return render_template("HtoC.html")


@app.route("/flight CtoB")
def flight2():
    return render_template("CtoB.html")


@app.route("/flight BtoG")
def flight3():
    return render_template("BtoG.html")


@app.route("/flight CtoD")
def flight4():
    return render_template("CtoD.html")


@app.route("/flight CtoG")
def flight5():
    return render_template("CtoG.html")


@app.route("/flight CtoH")
def flight6():
    return render_template("CtoH.html")


@app.route("/flight CtoK")
def flight7():
    return render_template("CtoK.html")


@app.route("/flight CtoM")
def flight8():
    return render_template("CtoM.html")


@app.route("/flight DtoC")
def flight9():
    return render_template("DtoC.html")


@app.route("/flight GtoB")
def flight10():
    return render_template("GtoB.html")


@app.route("/flight KtoC")
def flight11():
    return render_template("KtoC.html")


@app.route("/flight MtoC")
def flight12():
    return render_template("MtoC.html")


@app.route("/two")
def two():
    return render_template("two.html")


@app.route("/three")
def three():
    return render_template("three.html")


@app.route("/four")
def four():
    return render_template("four.html")


@app.route("/five")
def five():
    return render_template("five.html")


@app.route("/book")
def book():
    return render_template("search1.html")


@app.route("/terms")
def terms():
    return render_template("terms.html")


@app.route("/one")
def one():
    return render_template("one.html")


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/payment")
def payment():
    return render_template("payment dummy.html")


@app.route('/flight CtoD', methods=['GET', 'POST'])
def shortenurl():
    if request.method == 'POST':
        fname = request.form.get('fname')
        tname = request.form.get('tname')
        if fname == 'chennai' and tname == 'delhi':
            return render_template('CtoD.html')
        elif fname == 'chennai' and tname == 'mumbai':
            return render_template('CtoM.html')
        elif fname == 'chennai' and tname == 'hyderabad':
            return render_template('CtoH.html')
        elif fname == 'chennai' and tname == 'goa':
            return render_template('CtoG.html')
        elif fname == 'chennai' and tname == 'bangalore':
            return render_template('CtoB.html')
        elif fname == "delhi" and tname == "chennai":
            return render_template("DtoC.html")
        elif fname == "mumbai" and tname == "chennai":
            return render_template("MtoC.html")
        elif fname == "hyderabad" and tname == "chennai":
            return render_template("HtoC.html")
        elif fname == "bangalore" and tname == "goa":
            return render_template("BtoG.html")
        elif fname == "chennai" and tname == "kolkata":
            return render_template("CtoK.html")
        elif fname == "goa" and tname == "bangalore":
            return render_template("GtoB.html")
        elif fname == "kolkata" and tname == "chennai":
            return render_template("KtoC.html")
        elif fname == "mumbai" and tname == "chennai":
            return render_template("MtoC.html")
        else:
            return 'not a valid respone'
    else:
        return 'Not a valid request method for this route'


@app.route("/receipt", methods=['POST', 'GET'])
def details():
    if request.method == 'POST':
        fname = request.form["fname"]
        lname = request.form["lname"]
        email = request.form["email"]
        mobile = request.form["mobile"]
        price = request.form["amt"]

        add_new_lname(lname)
        add_new_fname(fname)
        add_new_email(email)
        add_new_mobile(mobile)

        return render_template('receipt.html', lname=lname, fname=fname, email=email, mobile=mobile, price=price)
    return render_template('receipt.html')


@app.route("/form", methods=['GET', 'POST'])
def price():
    if request.method == 'POST':
        price = request.form["price"]

        return render_template("form.html", price=price)
    return render_template("form.html")


@ app.route("/", methods=['GET', 'POST'])
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
