from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

scaler = pickle.load(open('models/standardscaler.pkl', 'rb'))
model = pickle.load(open('models/diabetes.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predictdata', methods=['POST'])
def predictdatapoint():
    Pregnancies = int(request.form.get("Pregnancies"))
    Glucose = float(request.form.get("Glucose"))
    BloodPressure = float(request.form.get("BloodPressure"))
    SkinThickness = float(request.form.get("SkinThickness"))
    Insulin = float(request.form.get("Insulin"))
    BMI = float(request.form.get("BMI"))
    DiabetesPedigreeFunction = float(request.form.get("DiabetesPedigreeFunction"))
    Age = float(request.form.get("Age"))

    new_data = scaler.transform([[Pregnancies, Glucose, BloodPressure,
                                  SkinThickness, Insulin, BMI,
                                  DiabetesPedigreeFunction, Age]])
    prediction = model.predict(new_data)[0]

    result = "Diabetic" if prediction == 1 else "Non-Diabetic"
    return render_template('single_prediction.html', result=result)

if __name__ == "__main__":
    app.run(debug=True, port=5001)