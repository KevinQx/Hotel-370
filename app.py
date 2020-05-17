from flask import Flask, redirect, url_for, render_template, session, request, g, send_from_directory,jsonify
from actions import *
from queries import *
from datetime import date
import json

app = Flask(__name__)
app.secret_key = "hello"


@app.route("/tiara")
def tiara():
    return render_template("Hotel.htm")


@app.route("/login", methods=["GET", "POST"])
def login():
    if "user" in session:
        return "user is currently logged in"
    if request.method == "POST":
        un = request.form["un"]
        pw = request.form["pw"]
        if user_in_db(un, pw):
            session["user"] = un
            session["userid"] = select_user_id_by_name(un)
            session["date"] = date.today()
            session["date_display"] = date.today().strftime("%D")
            return redirect(url_for("home"))
    return render_template("login.html")
    

@app.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("userid", None)
    session.pop("date", None)
    session.pop("admin", None)
    return render_template("home.html")


@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        fn = request.form["fn"]
        ln = request.form["ln"]
        un = request.form["un"]
        pw = request.form["pw"]
        insert_new_user(fn, ln, un, pw)
    return render_template("login.html")


#Loading Pages
@app.route("/")
def home():
    data = select_all_hotels()
    # session["date"] = "something"
    return render_template('home.html', hotels=data)


@app.route("/add_reservation")
def add_reservation():
    pass


@app.route("/reservations")
def reservations():
    if "user" in session:
        username = session["user"]
        data = select_reservations_by_custid(session["userid"])
        return render_template("reservations.html", d=data)
    return redirect(url_for("home"))


@app.route("/hotel/<chain>")
@app.route("/hotel/<chain>/<hotelname>")
def hotel_page(chain, hotelname=None):
    data = select_all_hotels()
    if hotelname:
        for d in data:
            if chain == d[-1] and hotelname == d[2]:
                address = d[3:5]
                return render_template(
                    "hotel.html", 
                    name=hotelname, 
                    location=address, 
                    chain=chain,
                    hotels=data,
                    chain_id = d[0],
                    rooms = select_all_rooms_by_chain(d[0])
                )
        return redirect(url_for("home"))
    else:
        pass


@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "GET":
        if "user" in session:
            return "please logout as a user first"
        elif "admin" in session:    
            return render_template("admin.html")    
        else:
            return render_template("admin_login.html")
    elif request.method == "POST":
        un = request.form["un"]
        pw = request.form["pw"]
        if admin_in_db(un, pw):
            session["admin"] = un
            session["date"] = date.today()
            session["date_display"] = date.today().strftime("%D")
            return render_template("admin.html")
        return redirect(url_for("home"))


@app.route("/register_admin", methods=["GET","POST"])
def register_admin():
    if request.method == "POST":
        hn = request.form["hn"]
        un = request.form["un"]
        pw = request.form["pw"]
        # insert_new_user(fn,ln,un,pw)
        if not hotel_name_exists(hn):
            insert_new_hotel(hn)
            idn = hotel_id_from_name(hn)
            insert_new_admin(un,pw,idn)
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