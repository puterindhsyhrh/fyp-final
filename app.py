import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('model/student_adaboost.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/fill')
def fill():
    return render_template('fill.html')

@app.route('/predict',methods=['POST'])
def predict():

    age = request.form['age']
    gender = request.form['gender']
    institusion = request.form['institusion']
    program = request.form['program']
    mode = request.form['mode']
    cgpa = request.form['cgpa']
    status = request.form['status']
    sponsor = request.form['sponsor']
    qualification = request.form['qualification']

    input_variables = pd.DataFrame([[age, gender, institusion, program, mode, cgpa, status, sponsor, 
        qualification]],
        columns=['age', 'gender', 'institusion', 'program', 'mode', 'cgpa', 'status', 'sponsor',
         'qualification'], 
        dtype=int)

    prediction = model.predict(input_variables)[0]

    if int(prediction)==1:
        output='graduate'
    else:
        output='drop out'

    return render_template('table.html', 
        original_input={'Age':age,'Gender':gender,'Institusion':institusion,'Program':program,
        'Mode':mode,'CGPA':cgpa,'Status':status, 'Sponsor':sponsor, 'Qualification':qualification}, 
        prediction_text='You are classified as {}'.format(output))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
