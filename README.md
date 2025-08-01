# 🧬 Vitamin Deficiency Detector and Predictor

A machine learning web application that detects vitamin deficiencies based on user-submitted images. The model is trained to analyze visual features from the eye, skin, and nails, and provides predictions of possible deficiencies along with related disease risks.

## 🚀 Features

- 🧠 Uses a pre-trained ResNet152V2 model
- 📷 Accepts user-uploaded images (eye, skin, nail)
- 🔍 Predicts levels of various vitamin deficiencies
- 🩺 Suggests potential diseases based on deficiencies
- 🌐 Deployed using Flask web framework
- 💾 Lightweight frontend with HTML, CSS, and JS

---

## 🧪 Supported Deficiencies

- Vitamin A, B-complex (B2, B3, B9, B12), C, D, E, K  
- Zinc, Iron, Biotin, Protein

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Model**: ResNet152V2 (Keras, TensorFlow)
- **LFS**: Git Large File Storage for model weights

---

## 📁 Project Structure

├── app.py # Flask backend
├── vitamin_deficiency_model.h5 # Trained model (Git LFS)
├── templates/
│ └── index.html # Main HTML page
├── static/
│ ├── styles.css # Styling
│ └── script.js # JS logic
├── requirements.txt # Dependencies
├── class_indices.json # Mapping for model classes
└── README.md



---

## ⚙️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/UdayKarthik2003/Vitamin_deficiency_detector_and__predictior.git
   cd Vitamin_deficiency_detector_and__predictior
Create a virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the app

bash
Copy
Edit
python app.py
