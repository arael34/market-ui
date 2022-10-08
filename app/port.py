from flask import Blueprint, request, redirect, url_for

from .controllers.portfolio import add_to_portfolio, del_from_portfolio, clear_portfolio

port = Blueprint("port", __name__)

@port.route("/add", methods=["GET", "PUT"])
def add():
    add_to_portfolio(request.form.get("add"))
    return redirect(url_for("routes.portfolio"))

@port.route("/del", methods=["GET", "PUT"])
def delete():
    del_from_portfolio(request.form.get())
    return redirect(url_for("routes.portfolio"))

@port.route("/clear", methods=["GET", "PUT"])
def clear():
    clear_portfolio()
    return redirect(url_for("routes.portfolio"))
