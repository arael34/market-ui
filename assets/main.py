from re import L
from flask import Flask, render_template, request, session, redirect, url_for
import plotly
import json

from controllers.viewer import view_f
#from controllers.folder import

app = Flask(__name__)
app.secret_key = "hello"

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

"""
Login page. The user enters their name and creates a session.
If a user accesses this page again, they're redirected to their profile
"""
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["name"]
        session["user"] = user
        return redirect(url_for("user"))
    elif request.method == "GET":
        return render_template("login.html")

"""
Profile page.

POST method means logout. If they logout, user is popped from the session.
If a user accesses this page without logging in, they're redirected to 
the login page.
"""
@app.route("/user", methods=["POST", "GET"])
def user():
    if request.method == "POST":
        session.pop("user", None)
        return redirect(url_for("login"))
    elif "user" not in session:
        return redirect(url_for("login"))
    else:
        user = session["user"]
        return render_template("user.html", user=user)

"""
Stock plot view. Without a symbol given, the user is redirected to home.
"""
@app.route("/view", methods=["POST"])
def view():
    if request.method != "POST":
        return redirect(url_for("/"))
    text = request.form['in']
    # view_f returns candlestick plot
    fig = view_f(text)
    # endcode plot as json
    fjson = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("return.html", figJSON=fjson)

"""
folders !
"""
@app.route("/folders", methods=["POST", "GET"])
def add_to_folder():
    if request.method == "POST":
        req = request.form["req"]
        if req == "create":
            pass
    return render_template("folders.html")

if __name__ == "__main__":
    app.run(debug=True)
