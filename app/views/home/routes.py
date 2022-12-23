from flask import Blueprint, render_template, request, redirect
from app.models import User
from flask_login import current_user


home_blueprint = Blueprint("home", __name__, url_prefix="/home",
                        template_folder="templates", static_folder="static")


@home_blueprint.route("/", methods=["GET", "POST"])
def homepage():
    return render_template("index.html")
        