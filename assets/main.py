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

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["name"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        return render_template("user.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))

@app.route("/view", methods=["POST"])
def view():
    if request.method != "POST":
        return
    text = request.form['in']
    fig = view_f(text)
    fjson = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("return.html", figJSON=fjson)
    
@app.route("/folders", methods=["POST"])
def add_to_folder():
    return render_template("folders.html")

if __name__ == "__main__":
    app.run(debug=True)