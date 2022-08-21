#import Flask 
from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict/', methods=['GET','POST'])
def predict():
    if request.method == "POST":
        
        age_of_mother = request.form.get('Age of Mother')
        oe_gestational = request.form.get('OE Gestational Age')
        lmp_gestational = request.form.get('LMP Gestational Age')
        bmi = request.form.get('Pregnency BMI')
        prenatal_visits = request.form.get('Number of Prenatal Visits')
        try:
            prediction = preprocessDataAndPredict(age_of_mother, oe_gestational, lmp_gestational, bmi, prenatal_visits)
            return render_template('predict.html', prediction = prediction)
        except ValueError:
            return "Please Enter valid values"
        pass
    pass
def preprocessDataAndPredict(age_of_mother, oe_gestational, lmp_gestational, bmi, prenatal_visits):
    data = [age_of_mother, oe_gestational, lmp_gestational, bmi, prenatal_visits]
    print(data)
    data = np.array(data).astype(np.float64)
    data = data.reshape(1,-1)
    print(data)
    file = open("birth_model.pkl",'rb')
    trained_model = joblib.load(file)
    prediction = trained_model.predict(data)
    return prediction

    pass
if __name__ == '__main__':
    app.run(debug=True)