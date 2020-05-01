from flask import Flask, redirect, url_for,render_template, session, request, g
from actions import *
from queries import insert_new_admin
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/user/<username>")
def reservations(username):
    return render_template("reservations.html")

@app.route("/login")
def login_and_register():
    return render_template("login.html")

@app.route("/hotel/<hotelname>")
def hotel_page(hotelname):
    return render_template("hotel.html")

@app.route("/admin")
def admin_page():
    return render_template("admin.html")

@app.route("/adminregistersubmit", methods=["POST"])
def admin_registration():
    pass


@app.route("/home")
def sendHome():
    return render_template("bla.html")


@app.route("/getData")
def send_data():
    data = [
        (1, "Joseph"),
        (2, "John")
    ]
    return json.dumps(data)

if __name__ == "__main__":
    app.run(debug=True)