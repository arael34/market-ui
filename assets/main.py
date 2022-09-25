from flask import Flask, render_template

from controllers.viewer import view

app = Flask(__name__)

@app.route("/")
def _view():
    view()
    return render_template('index.html')

def main():
    app.run()

if __name__ == "__main__":
    main()