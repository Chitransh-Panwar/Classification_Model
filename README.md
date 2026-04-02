# 🔢 Handwritten Digit Classifier (0–9)

A machine learning web application that classifies handwritten digit images (0–9) using a trained Scikit-learn model. Users can upload an image through a simple frontend interface, and the backend API returns the predicted digit.

---

## 🚀 Features

* Upload image of a handwritten digit
* Real-time prediction using trained ML model
* Simple and clean UI
* Flask-based REST API
* Scikit-learn model integration

---

## 🧠 Model Details

* Algorithm: Scikit-learn Classifier
* Input: 28 × 28 grayscale image
* Preprocessing:

  * Resize to 28×28
  * Convert to grayscale
  * Normalize pixel values (0–1)
  * Flatten to 784 features
* Output: Digit (0–9)

---

## 🛠️ Tech Stack

* Python
* Flask
* Scikit-learn
* NumPy
* Pillow (PIL)
* HTML, JavaScript

---

## 📂 Project Structure

```
Classification_Model/
│── app.py               # Flask backend API
│── classification.py   # Model training script
│── model.pkl           # Trained model
│── index.html          # Frontend UI
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/Classification_Model.git
cd Classification_Model
pip install -r requirements.txt
```

---

## ▶️ Run the Application

### 1. Start Flask Server

```bash
python app.py
```

Server will run at:

```
http://127.0.0.1:5000/
```

---

### 2. Open Frontend

Open `index.html` in your browser
(or use Live Server on port 5500)

---

## 📸 Usage

1. Upload an image of a handwritten digit (0–9)
2. Click **Predict**
3. View predicted result instantly

---

## ⚠️ Notes

* Ensure the uploaded image is clear and resembles MNIST-style digits
* Model file (`model.pkl`) must be present in the root directory
* If model is not included, add it manually or download it before running

---

## 🔮 Future Improvements

* Add drawing canvas for digit input
* Deploy on cloud (Render / AWS)
* Improve model accuracy with deep learning
* Add drag-and-drop UI
* Mobile responsiveness

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and improve the project.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Chitransh Panwar**

---

⭐ If you found this project helpful, consider giving it a star!
