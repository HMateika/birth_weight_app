#import Flask 
from flask import Flask, render_template, request
import numpy as np
#create an instance of Flask
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict/', methods=['GET','POST'])
def predict():
    if request.method == "POST":
        #get form data
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
    #put all inputs in array
    test_data = [age_of_mother, oe_gestational, lmp_gestational, bmi, prenatal_visits]
    print(test_data)
    #convert value data into numpy array
    test_data = np.array(test_data).astype(np.float)
    #reshape array
    test_data = test_data.reshape(1,-1)
    print(test_data)
    #open file
    #load trained model
    trained_model = tf.saved_model.load("/Users/harri/birth_weight_app/model_saved_model.pb")
    #predict
    prediction = trained_model.predict(test_data)
    return prediction
    pass
if __name__ == '__main__':
    app.run(debug=True)