from flask import Flask, render_template, request, redirect
from mongo_utils import insert_weather_data, get_all_data
import json

app = Flask(__name__)

@app.route('/')
def home():
    data = get_all_data()
    return render_template('dashboard.html', data=data)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        region = request.form['region']
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        crop = request.form['crop']
        disease_risk = request.form['disease_risk']
        
        insert_weather_data(region, temperature, humidity, crop, disease_risk)
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
