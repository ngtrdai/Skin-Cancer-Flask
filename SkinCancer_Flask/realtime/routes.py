from flask import render_template, request, Blueprint
from flask import flash, url_for, redirect, abort
from SkinCancer_Flask import app

realtime = Blueprint('realtime', __name__)


@realtime.route("/realtime")
def realtimePage():
    return render_template("realtime.html", url="realtime")