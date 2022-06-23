import imp
from flask import render_template, request, Blueprint
from flask import flash, url_for, redirect, abort
from SkinCancer_Flask import app

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/trangchu")
def home():
    return render_template("home.html", url="home")