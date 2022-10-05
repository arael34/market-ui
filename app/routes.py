from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, AnonymousUserMixin
import plotly
import json

from .controllers.viewer import view_f

routes = Blueprint("routes", __name__)

@routes.route("/", methods=["GET"])
def index():
    return render_template("index.html")

"""
Stock plot view. Without a symbol given, the user is redirected to home.
"""
@routes.route("/view", methods=["POST", "GET"])
def view():
    if request.method == "POST":
        if "in" in request.form:
            text = request.form["in"]
            # view_f returns candlestick plot
            fig = view_f(text)
            # endcode plot as json
            fjson = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
            return render_template("view.html", figJSON=fjson)
        else:
            pass
    elif request.method == "GET":
        return redirect(url_for("routes.index"))

"""
TODO
portfolios
"""
@routes.route("/portfolio", methods=["GET"])
def portfolio():
    user = current_user
    if isinstance(user, AnonymousUserMixin) or isinstance(user, type(None)):
        return redirect(url_for("auth.signup"))
    return render_template("portfolio.html", portfolio=user.portfolio)
