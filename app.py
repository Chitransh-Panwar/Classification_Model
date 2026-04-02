from flask import Flask, request, jsonify
import numpy as np
from PIL import Image
import joblib
import os

app = Flask(__name__)

# ✅ Load model
MODEL_PATH = "model.pkl"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("model.pkl not found. Please add it to the project.")

model = joblib.load(MODEL_PATH)
print("✅ Model loaded successfully")

# ✅ Image preprocessing (VERY IMPORTANT)
def preprocess_image(image):
    # Convert to grayscale
    image = image.convert("L")

    # Resize to 28x28 (same as training)
    image = image.resize((28, 28))

    # Convert to numpy array
    img_array = np.array(image)

    # Normalize (0–255 → 0–1)
    img_array = img_array / 255.0

    # Flatten (for sklearn models)
    img_array = img_array.flatten().reshape(1, -1)

    return img_array


# ✅ Home route
@app.route("/")
def home():
    return "Digit Classifier API is running 🚀"


# ✅ Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Check file
        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["file"]

        if file.filename == "":
            return jsonify({"error": "Empty filename"}), 400

        # Open image
        image = Image.open(file.stream)

        # Preprocess
        processed = preprocess_image(image)

        # Predict
        prediction = model.predict(processed)

        # Return result
        return jsonify({
            "prediction": int(prediction[0])
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


# ✅ Run server
if __name__ == "__main__":
    app.run(debug=True)