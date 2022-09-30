from flask import Flask

from .routes import routes
from .auth import auth

def create_app():
    app = Flask(__name__)
    app.secret_key = "arael034"
    app.register_blueprint(routes, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    return app
    