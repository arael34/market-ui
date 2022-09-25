from flask import Flask, render_template, request, redirect

from controllers.viewer import view
from dash_ex.dash_init import graph_init

app = Flask(__name__)
graph_init(app)

@app.route("/")
def _index():
    return render_template('index.html')

@app.route("/view", methods=["POST"])
def _view():
    if request.method != 'POST':
        return
    text = request.form['in']
    fig = view(text)
    fig.show()
    
    return render_template('return.html')

def main():
    app.run()

if __name__ == "__main__":
    main()