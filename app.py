//file: main.py
from flask import Flask, render_template, request

@app.route('/predict/', methods=['GET','POST'])
def predict():
    if request.method == "POST":
        #get form data
        age_of_mother = request.form.get('Age of Mother')
        oe_gestational = request.form.get('OE Gestational Age')
        lmp_gestational = request.form.get('LMP Gestational Age')
        bmi = request.form.get('Pregnency BMI')
        prenatal_visits = request.form.get('Number of Prenatal Visits')
        return render_template('predict.html')
    pass