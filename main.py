from flask import Flask, render_template, request, url_for, flash
import qrcode
import random, datetime

app=Flask(__name__)
app.config["SECRET_KEY"] = "17398@!(]HWVGG52730`097307HK%WR$ER-CRW"

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
    img.save("static/"+name)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route("/generate", methods=["POST", "GET"])
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
            return render_template("success.html", filename=name)

@app.route("/api/generate/<message>", methods=["POST", "GET"])
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

app.run(debug=True)
