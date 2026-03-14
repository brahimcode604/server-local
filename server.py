from flask import Flask, request, send_from_directory, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "images"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# upload image
@app.route("/upload", methods=["POST"])
def upload():
    file = request.files['image']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    return jsonify({
        "message": "image uploaded",
        "url": f"/images/{file.filename}"
    })


# list images
@app.route("/images", methods=["GET"])
def list_images():
    files = os.listdir(UPLOAD_FOLDER)
    return jsonify(files)


# get image
@app.route("/images/<filename>")
def get_image(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


if __name__ == "__main__":
    app.run(host="10.66.66.84", port=5000)