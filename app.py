from flask import Flask, render_template,request,flash
import numpy as np
from joblib import load, dump

app = Flask(__name__)
app.config['SECRET_KEY']='14068'

model = load('demo_model.joblib')


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        passenger_class = request.form['passengerClass']
        age = request.form["age"]
        gender = request.form['gender']
        if gender == '1':
            female = 0
            male = 1
        else:
            female = 1
            male = 0
        y_pred = [[passenger_class, age, female, male]]
        prediction = model.predict(y_pred)
        if prediction == 0:
            flash('No Survived', 'danger')
        else:
            flash('Survived', ' success')
    return render_template('index.html'), app.config['SECRET_KEY']


if __name__ == '__main__':
    app.run(debug=True)
