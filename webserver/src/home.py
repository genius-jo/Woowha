from flask import Flask, render_template, request
from werkzeug import secure_filename
import redis
import os
from datetime import datetime

app = Flask(__name__)

cache = redis.Redis(host="redis", port=6379)

ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg"])


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/home")
def render_file():
    return render_template("upload.html")


@app.route("/fileUpload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        f = request.files["file"]

        if f and allowed_file(f.filename):
            f_name = datetime.now().strftime("%Y%m%d%H%M%S%f")
            f.save(f_name + ".jpg")
            cache.lpush("img", f_name)
            return "file uploaded successfully"

        return "error!"
    return "error!"


@app.route("/fileResult/<int:status_code>/")
def downloan_file(status_code):
    if status_code == 200:
        return render_template("result_page.html", image_file="01.jpg")

    return "error!"
