from flask import render_template, request, Blueprint
from flask import flash, url_for, redirect, abort
from SkinCancer_Flask import app

infoUngThuDa = Blueprint('infoUngThuDa', __name__)


@infoUngThuDa.route("/info")
def infoUngThuDaPage():
    return render_template("info_benh.html", url="info_benh")