from flask import Flask, request, send_from_directory, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename # 👈 Ajoute cet import
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "images"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/upload", methods=["POST"])
def upload():
    # Vérifie si la requête contient bien la partie 'image'
    if 'image' not in request.files:
        return jsonify({"error": "Aucun fichier envoyé"}), 400
        
    file = request.files['image']
    
    # Vérifie si l'utilisateur a vraiment sélectionné un fichier
    if file.filename == '':
        return jsonify({"error": "Aucun fichier sélectionné"}), 400

    # Sécurise le nom du fichier
    if file:
        filename = secure_filename(file.filename) # 👈 Protège le nom
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        return jsonify({
            "message": "image uploaded",
            "url": f"/images/{filename}"
        })

# ... Le reste de ton code (list_images et get_image) est très bien ! ...

if __name__ == "__main__":
    app.run(host="10.66.66.84", port=5000)