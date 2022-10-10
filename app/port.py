from flask import Blueprint, request, redirect, url_for, render_template, flash
from flask_login import current_user, AnonymousUserMixin

from . import db

port = Blueprint("port", __name__)

@port.route("/", methods=["GET"])
def portfolio():
    user = current_user
    if isinstance(user, AnonymousUserMixin) or isinstance(user, type(None)):
        return redirect(url_for("auth.signup"))
    return render_template("portfolio.html", portfolio=user.portfolio)

@port.route("/add", methods=["GET", "PUT"])
def add():
    symbol = request.form.get("add")
    if isinstance(symbol, type(None)):
        flash("Please enter a symbol.")
    else:
        user = current_user
        user.portfolio = symbol
        db.session.commit()
    return redirect(url_for("routes.portfolio"))

@port.route("/del", methods=["GET", "PUT"])
def delete():
    return redirect(url_for("routes.portfolio"))

@port.route("/clear", methods=["GET", "PUT"])
def clear():
    user = current_user
    user.portfolio = ""
    db.session.commit()
    return redirect(url_for("routes.portfolio"))
