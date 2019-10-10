from deep_privacy_anonymize import anon_and_write_imgs
import os
import uuid
import gc
import platform
from flask import Flask, flash, redirect, request, url_for, jsonify
import sys


UPLOAD_FOLDER = "./upload"
PUBLIC_FOLDER = "./public"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

"""
curl -F "file=@ainsley.jpg" localhost:5000/
"""

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["PUBLIC_FOLDER"] = PUBLIC_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )

@app.route("/", methods=["POST"])
def upload_file():
    # check if the post request has the file part
    if "file" not in request.files:
        errr = f'Image file must be included'
        return jsonify(error=errr)
    file = request.files["file"]
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == "":
        flash("No selected file")
        return redirect(request.url)
    if not file or not allowed_file(file.filename):
        errr = f'Image file must be under 16MB in one of these formats:{ALLOWED_EXTENSIONS}'
        return jsonify(error=errr)
    print(uuid.uuid4())
    ext = file.filename.rsplit(".", 1)[1].lower()
    filename = f'{uuid.uuid4()}.{ext}'
    filepath_upload = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath_upload)
    path_to_ckpt = './deep_privacy/resources/cpu_checkpoint.ckpt'
    filepath_public = os.path.join(app.config["PUBLIC_FOLDER"], filename)
    anon_and_write_imgs([filepath_upload],[filepath_public])
    # return redirect(url_for("uploaded_file", filename=filename))
    print('garbage collection')
    gc.collect()
    if sys.platform == 'darwin':
        return jsonify(file_url=f'http://localhost:5000{filepath_public[1:]}')
    else:
        return jsonify(file_url=f'http://142.93.98.12{filepath_public[1:]}')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
