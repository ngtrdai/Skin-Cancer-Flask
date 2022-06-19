from flask import render_template, request, Blueprint
from flask import flash, url_for, redirect, abort
from SkinCancer_Flask import app

detection = Blueprint('detection', __name__)


@detection.route("/nhandien")
def detectionPage():
    return render_template("detection.html", url="nhandien")