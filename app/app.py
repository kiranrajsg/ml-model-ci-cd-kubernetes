from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

MODEL_PATH = "model/model.joblib"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("Model file not found")

model = joblib.load(MODEL_PATH)

@app.route("/", methods=["GET"])
def health():
    return "OK", 200

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = data.get("features")

    if features is None:
        return jsonify({"error": "No features provided"}), 400

    prediction = model.predict([features])
    return jsonify({"prediction": int(prediction[0])})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
