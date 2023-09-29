# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 06:14:07 2023

@author: HP
"""

import pickle
from flask import Flask, render_template, request, escape

app = Flask(__name__, template_folder='templates')

# Load the pre-trained model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/', methods=['GET', 'POST'])
def index():
    predicted_cluster = None  # Default value

    if request.method == 'POST':
        # Get user input
        recency = float(request.form['recency'])
        frequency = float(request.form['frequency'])
        monetory = float(request.form['monetory'])

        # Predict the cluster for the input
        input_data = [[recency, frequency, monetory]]
        predicted_cluster = model.predict(input_data)[0]

        return f'Predicted Cluster: {predicted_cluster}'

    return render_template('index.html' , predicted_cluster=predicted_cluster)

if __name__ == '__main__':
    app.run(debug=True)
