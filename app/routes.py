from flask import Blueprint, render_template, request, redirect, url_for
import plotly
import json

from .controllers.viewer import view_f

routes = Blueprint("routes", __name__)

@routes.route("/", methods=["GET"])
def search():
    return render_template("search.html")

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
        return redirect(url_for("routes.search"))
