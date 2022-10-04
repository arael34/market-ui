from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

migrate = Migrate()
db = SQLAlchemy()
DB_NAME = "users.db"

from .routes import routes
from .auth import auth

def create_app():
    app = Flask(__name__)
    app.secret_key = "arael034"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)
    #db.create_all(app=app)

    app.register_blueprint(routes, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    lm = LoginManager()
    lm.login_view = "auth.login"
    lm.init_app(app)

    from .models import User
    @lm.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
    