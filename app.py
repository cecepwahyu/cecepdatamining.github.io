from flask import Flask, request, render_template
import pickle

import numpy

app = Flask(__name__)

model_file = open('modelLogReg.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', Classification=0)

@app.route('/predict', methods=['POST'])
def predict():
    '''
    '''
    Age, BMI, Glucose, Insulin, HOMA, Leptin, Adiponectin, Resistin, MCP1 = [x for x in request.form.values()]

    data = []

    data.append(int(Age))
    data.append(float(BMI))
    data.append(int(Glucose))
    data.append(float(Insulin))
    data.append(float(HOMA))
    data.append(float(Leptin))
    data.append(float(Adiponectin))
    data.append(float(Resistin))
    data.append(float(MCP1))

    prediction = model.predict([data])
    output = round(int(prediction[0]),2)
    return render_template('index.html', Classification=output, Age=Age, BMI=BMI, Glucose=Glucose, Insulin=Insulin, HOMA=HOMA, Leptin=Leptin, Adiponectin=Adiponectin, Resistin=Resistin, MCP1=MCP1)


if __name__ == '__main':
    app.run(debug=True)