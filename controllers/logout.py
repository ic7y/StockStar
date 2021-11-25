from flask import Blueprint, render_template, request, redirect, make_response
from app import *

logout_page = Blueprint("logout_page", __name__, url_prefix="/StockStar")


@logout_page.route('/logout')
def logout():
    key = app.config['AUTH_COOKIE_NAME']

    response = make_response(redirect("/StockStar/index"))
    response.delete_cookie(key)
    return response
