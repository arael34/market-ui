from flask import Blueprint, request, session, render_template, redirect, url_for, flash

auth = Blueprint("auth", __name__)

"""
Signup page
"""
@auth.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        password_c = request.form.get("password-c")
        if len(username) < 4:
            flash("Username must be longer than 3 characters", category="error")
        elif password != password_c:
            flash("Passwords don't match. Try Again", category="error")
        else:
            pass
            # add to db
    return render_template("signup.html")

"""
Login page. The user enters their name and creates a session.
If a user accesses this page again, they're redirected to their profile
"""
@auth.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        session["user"] = user
        return redirect(url_for("routes.user"))
    elif request.method == "GET":
        return render_template("login.html")

"""
Profile page.

POST method means logout. If they logout, user is popped from the session.
If a user accesses this page without logging in, they're redirected to 
the login page.
"""
@auth.route("/user", methods=["POST", "GET"])
def user():
    if request.method == "POST":
        session.pop("user", None)
        return redirect(url_for("routes.login"))
    elif "user" not in session:
        return redirect(url_for("routes.login"))
    else:
        user = session["user"]
        return render_template("user.html", user=user)
