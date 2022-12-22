from flask import Blueprint, render_template, request, redirect, flash
from app.models import User
from flask_login import current_user

import qrcode
import random, datetime, os

qrcode_blueprint = Blueprint("qrcode", __name__, url_prefix="/qrcode",
                        template_folder="templates", static_folder="static")

GENERATED_QR_DIR = "generated_QR/" # relative to the 'static' directory

def filename_gen():
    rint = random.randint(4201, 9999)
    today_date = datetime.datetime.now().strftime("%d-%m-%Y")
    filename = "QRCode-"+str(rint)+"_"+today_date+".png"
    return filename

def create(message, name):
    qr = qrcode.QRCode(
        version = 15,
        box_size = 10,
        border = 5
    ) 
    data = message
    qr.add_data(data)
    qr.make(fit = True)
    img = qr.make_image(fill="black",back_color = "white")

    if not os.path.exists(f"app/static/{GENERATED_QR_DIR}"):
        os.makedirs(f"app/static/{GENERATED_QR_DIR}")
    img.save("app/static/" + GENERATED_QR_DIR + name)    

@qrcode_blueprint.route("/generate", methods=["POST", "GET"])
def generate():
    if request.method == "GET":
        return render_template("generate.html")
    else:
        message = request.form['message']
        name = filename_gen()
        print(name)
        if message == "":
            flash('Cannot be empty', 'error')
            return render_template("generate.html")
        else:
            
            create(message=message, name=name)
            return render_template(
                "success.html",filename=GENERATED_QR_DIR + name)

@qrcode_blueprint.route("/api/generate/<message>", methods=["POST", "GET"])
def generate_api(message):
    message = message
    name = filename_gen()
    print(name)
    create(message=message, name=name)
    success = {
        "data": "QRCODE GENERATED SUCCESSFULLY",
        "error": "None"
    }
    return success
