from flask import Blueprint, request, redirect, url_for
from flask_login import current_user

from .controllers.portfolio import add_to_portfolio, del_from_portfolio, clear_portfolio

port = Blueprint("port", __name__)

@port.route("/add", methods=["PUT"])
def add():
    user = current_user
    add_to_portfolio(user, request.form.get())
    return redirect(url_for("routes.portfolio"))

@port.route("/del", methods=["PUT"])
def delete():
    user = current_user
    del_from_portfolio(user, request.form.get())
    return redirect(url_for("routes.portfolio"))

@port.route("/clear", methods=["PUT"])
def clear():
    user = current_user
    clear_portfolio(user)
    return redirect(url_for("routes.portfolio"))
