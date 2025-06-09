from flask import Flask, request, jsonify
from flask_cors import CORS
import face_recognition, cv2, numpy as np, base64, datetime, json, os

app = Flask(__name__)
CORS(app)
DB = "faces.json"

def save(name, encoding):
    record = {"name": name, "encoding": encoding.tolist(), "time": str(datetime.datetime.now())}
    data = json.load(open(DB)) if os.path.exists(DB) else []
    data.append(record)
    json.dump(data, open(DB, "w"))

@app.route("/register", methods=["POST"])
def register():
    body = request.json
    img_data = base64.b64decode(body["image"])
    img_np = np.frombuffer(img_data, np.uint8)
    img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)
    enc = face_recognition.face_encodings(img)
    if enc:
        save(body["name"], enc[0])
        return jsonify({"status": "success"})
    return jsonify({"status": "no face detected"})

app.run(port=5000)
