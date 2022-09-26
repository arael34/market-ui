from flask import Flask, render_template, request
import plotly
import json

from controllers.viewer import view

app = Flask(__name__)

@app.route("/", methods=["GET"])
def _index():
    return render_template('index.html')

@app.route("/view", methods=["POST"])
def _view():
    if request.method != 'POST':
        return
    text = request.form['in']
    fig = view(text)
    fjson = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("return.html", figJSON=fjson)
    
def main():
    app.run()

if __name__ == "__main__":
    main()