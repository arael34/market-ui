from flask import flash
from flask_login import current_user
from .. import db

def add_to_portfolio(symbol):
    if isinstance(symbol, type(None)):
        flash("Please enter a symbol.")
    else:
        user = current_user
        user.portfolio = symbol
        db.session.commit()

def del_from_portfolio(symbol):
    pass

def clear_portfolio():
    user = current_user
    user.portfolio = "";