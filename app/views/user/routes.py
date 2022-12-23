from flask import Blueprint, render_template, request, redirect
from app.models import User, QRcode
from flask_login import current_user


user_blueprint = Blueprint("user", __name__, url_prefix="/user",
                        template_folder="templates", static_folder="static")


@user_blueprint.route("/data", methods=["GET"])
def user_data():
    user_qr_codes = QRcode.query.filter(QRcode.user_id==current_user.id).all()

    return render_template("user_data.html", user_qr_codes=user_qr_codes)
