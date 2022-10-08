from flask import Blueprint, request, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, AnonymousUserMixin

from .models import User, Portfolio
from . import db

auth = Blueprint("auth", __name__)

"""
Signup page
username must be longer than 3 characters,
and confirm password feature
"""
@auth.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        password_c = request.form.get("password-c")

        user = User.query.filter_by(username=username).first()
        if user:
            flash("Username already exists.", category="error")
        elif len(username) < 4:
            flash("Username must be longer than 3 characters.", category="error")
        elif password != password_c:
            flash("Passwords don't match, try again.", category="error")
        else:
            user = User(username=username, password=generate_password_hash(password, method="sha256"), portfolio = Portfolio(symbols=""))
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            return redirect(url_for("auth.user"))

    return render_template("signup.html")

"""
Login page. The user enters their name and creates a session.
If a user accesses this page again, they're redirected to their profile
"""
@auth.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        un = request.form["username"]
        pw = request.form["password"]

        user = User.query.filter_by(username=un).first()
        if user:
            if check_password_hash(user.password, pw):
                login_user(user, remember=True)
                return redirect(url_for("auth.user"))
            else:
                flash("Username or password is incorrect, try again.", category="error")
        else:
            flash("Username or password is incorrect, try again.", category="error")
            
    return render_template("login.html")

"""
Profile page.

POST method means logout. If they logout, user is popped from the session.
If a user accesses this page without logging in, they're redirected to 
the login page.
"""
@auth.route("/user", methods=["POST", "GET"])
def user():
    user = current_user
    if request.method == "POST":
        logout_user()
        return redirect(url_for("auth.login"))
    elif isinstance(user, AnonymousUserMixin) or isinstance(user, type(None)):
        return redirect(url_for("auth.signup"))
    else:
        return render_template("user.html", user=user.username)
