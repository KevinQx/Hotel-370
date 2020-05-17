from flask import Flask, redirect, url_for,render_template, session, request, g, send_from_directory,jsonify
from actions import *
from queries import *
import json

app = Flask(__name__)
app.secret_key = "hello"

@app.route("/login", methods=["GET", "POST"])
def login():
    if "user" in session:
        return "user is currently logged in"
    if request.method == "POST":
        un = request.form["un"]
        pw = request.form["pw"]
        print(session)
        if user_in_db(un, pw):
            session["user"] = un
            return redirect(url_for("home"))
    return render_template("login.html")
    

@app.route("/logout")
def logout():
    session.pop("user")
    session.pop("date")
    return render_template("home.html")


@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        fn = request.form["fn"]
        ln = request.form["ln"]
        un = request.form["un"]
        pw = request.form["pw"]
        insert_new_user(fn,ln,un,pw)
    return render_template("login.html")


#Loading Pages
@app.route("/")
def home():
    data = select_all_hotels()
    session["date"] = "something"
    return render_template('home.html', hotels=data)



@app.route("/reservations/<username>")
def reservations(username):
    return render_template("reservations.html")


@app.route("/hotel/<chain>/<hotelname>")
def hotel_page(chain, hotelname):
    data = select_all_hotels()
    for d in data:
        if chain == d[-1] and hotelname == d[2]:
            address = d[3:5]
            return render_template(
                "hotel.html", 
                name=hotelname, 
                location=address, 
                chain=chain,
                hotels=data
            )
    return redirect(url_for("home"))


@app.route("/admin")
def admin():
    return render_template("admin.html")


# Returning Data

@app.route("/getAllLocations")
def getAllLocations():
    return json.dumps(select_all_locations())


# @app.route("/login")
# def login_and_register():
#     return render_template("login.html")

# @app.route("/adminregistersubmit", methods=["POST"])
# def admin_registration():
#     pass


# @app.route("/home")
# def sendHome():
#     return render_template("bla.html")


# @app.route("/getData")
# def send_data():
#     data = [
#         (1, "Joseph"),
#         (2, "John")
#     ]
#     return json.dumps(data)

# @app.route('/postData', methods=["GET","POST"])
# def receivePost():
#     if request.method == "POST":
#         return json.dumps(request.form)

@app.route('/js/<path>')
def send_js(path):
    return send_from_directory('js', path)


if __name__ == "__main__":
    app.run(debug=True)