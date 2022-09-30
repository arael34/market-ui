from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .routes import routes
from .auth import auth

def create_app():
    app = Flask(__name__)
    app.secret_key = "arael034"
    app.register_blueprint(routes, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db = SQLAlchemy(app)

    return app
    