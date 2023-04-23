from flask import Flask, render_template, request
import pickle
import sklearn
import numpy as np


app = Flask(__name__)
model = pickle.load(open('Liver_analysis.pkl', 'rb'))



@app.route('/')
def about():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')




@app.route('/predict')
def index():
    return render_template('predict.html')


@app.route('/pred', methods=['post'])
def pred():
    age = request.form['Age']
    gender = request.form['Gender']
    tb = request.form['Total_bilirubin']
    db = request.form['Direct_bilirubin']
    ap = request.form['Alkaline_Phosphotase']
    aa1 = request.form['Alamine_Aminotransferase']
    aa2 = request.form['Aspartate_Aminotransferase']
    tp = request.form['Total_protiens']
    a = request.form['Albumin']
    agr = request.form['Albumin_and_Globulin_Ratio']


    data = [[float(age), float(gender), float(tb), float(db), float(ap), float(aa1), float(aa2), float(tp), float(a),
         float(agr)]]



    prediction = model.predict(data)

    if prediction == 1:

        return render_template('Submit.html', prediction_text='You have liver disease')
    else:

        return render_template('Submit.html', prediction_text='You dont have liver disease')

if __name__ == '__main__':
    app.run(debug=True)
