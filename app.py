from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
import cv2
import json
import os

app = Flask(__name__, static_folder="static", template_folder="templates")

# Load the trained model
MODEL_PATH = "vitamin_deficiency_model.h5"
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file '{MODEL_PATH}' not found.")
model = tf.keras.models.load_model(MODEL_PATH)

# Load class indices
CLASS_INDICES_PATH = "class_indices.json"
if not os.path.exists(CLASS_INDICES_PATH):
    raise FileNotFoundError(f"Class indices file '{CLASS_INDICES_PATH}' not found.")
with open(CLASS_INDICES_PATH, "r") as f:
    class_indices = json.load(f)
classes = {v: k for k, v in class_indices.items()}

# Define vitamin-disease mapping
vitamin_disease_mapping = {
    "Vitamin A deficiency": ["Night Blindness", "Dry Skin"],
    "Vitamin B1 deficiency": ["Beriberi", "Memory Issues"],
    "Vitamin B2 deficiency": ["Cracked Lips", "Mouth Ulcers"],
    "Vitamin B3 deficiency": ["Pellagra", "Diarrhea"],
    "Vitamin B6 deficiency": ["Anemia", "Irritability"],
    "Vitamin B12 deficiency": ["Nerve Damage", "Fatigue"],
    "Vitamin C deficiency": ["Scurvy", "Bleeding Gums"],
    "Vitamin D deficiency": ["Osteoporosis", "Heart Disease"],
    "Vitamin E deficiency": ["Nerve Damage", "Vision Problems"],
    "Vitamin K deficiency": ["Excessive Bleeding", "Bruising"]
}

# Image preprocessing
def preprocess_image(image_file):
    image = np.frombuffer(image_file.read(), np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    image = cv2.resize(image, (224, 224))
    image = image / 255.0
    return np.expand_dims(image, axis=0)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    if "eye" not in request.files or "skin" not in request.files or "nail" not in request.files:
        return jsonify({"error": "Please upload all three images"}), 400

    try:
        eye_img = preprocess_image(request.files["eye"])
        skin_img = preprocess_image(request.files["skin"])
        nail_img = preprocess_image(request.files["nail"])

        preds_eye = model.predict(eye_img)[0]
        preds_skin = model.predict(skin_img)[0]
        preds_nail = model.predict(nail_img)[0]

        avg_preds = (preds_eye + preds_skin + preds_nail) / 3
        deficiencies = {classes[i]: float(pred) for i, pred in enumerate(avg_preds)}

        top_2_deficiencies = sorted(deficiencies.items(), key=lambda x: x[1], reverse=True)[:2]

        result = []
        for vitamin, _ in top_2_deficiencies:
            diseases = vitamin_disease_mapping.get(vitamin, [])
            result.append({"vitamin": vitamin, "diseases": diseases})

        return jsonify({"top_2_deficiencies": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
