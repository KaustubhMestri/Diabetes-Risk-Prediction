# 🩺 Diabetes Risk Prediction
**Diabetes Risk Prediction** is a Python-based machine learning web application that predicts an individual's risk of diabetes using clinical health indicators from the Pima Indians Diabetes Dataset.

**Disclaimer**: For informational use only. Consult a qualified healthcare professional for medical advice.

## Overview
An end-to-end ML pipeline that preprocesses clinical data, trains and evaluates multiple classification models, and serves predictions through an interactive Flask web interface.

## Key Features
- Predicts diabetes risk from 8 clinical input features
- Compares multiple ML models (Logistic Regression, Random Forest, SVM, XGBoost, etc.)
- Serialized model for fast, real-time inference
- Clean Flask web UI for user-friendly predictions
- Detailed Jupyter notebooks covering EDA, preprocessing, and model training

## Tech Stack
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white" alt="Flask"/>
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white" alt="Scikit-Learn"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="Pandas"/>
  <img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white" alt="NumPy"/>
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white" alt="Jupyter"/>
</p>

## Installation

Install:
- **Git**: [Download](https://git-scm.com/download/win)
- **Python 3.8+**: [Download](https://www.python.org/downloads/)

### Clone Repository
1. Open CLI.
2. Run:
   ```bash
   git clone https://github.com/KaustubhMestri/Diabetes-Risk-Prediction
   cd Diabetes-Risk-Prediction
   ```

### Set Up Environment
1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
2. Activate:
   ```bash
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Run App
```bash
python app.py
```
Open `http://127.0.0.1:5000`.

## Dataset
The model is trained on the **Pima Indians Diabetes Dataset** (NIDDK). Input features include: `Pregnancies`, `Glucose`, `BloodPressure`, `SkinThickness`, `Insulin`, `BMI`, `DiabetesPedigreeFunction`, and `Age`.

## Contributing
1. Create an [issue](https://github.com/KaustubhMestri/Diabetes-Risk-Prediction/issues).
2. Branch: `feature/<n>` or `bugfix/<n>`
   ```bash
   git checkout -b feature/<n>
   ```
3. Commit:
   ```bash
   git add .
   git commit -m "#<issue> message"
   ```
4. Push:
   ```bash
   git push origin feature/<n>
   ```
5. Submit PR to `main`.

## License
Apache 2.0 License. See [LICENSE](LICENSE).
