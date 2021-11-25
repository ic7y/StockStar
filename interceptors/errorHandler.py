from app import *
from flask import render_template


@app.errorhandler(404)
def errorhandler(e):
    return render_template("index.html")
