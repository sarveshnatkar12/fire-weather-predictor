from flask import Flask , request , jsonify , render_template
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler


application = Flask(__name__)
app = application



with open('model/scaler.pkl', 'rb') as f:
    standardize_model = pickle.load(f)

with open('model/model.pkl', 'rb') as f:
    ridge_pickle = pickle.load(f)



@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        try:
            Temperature = float(request.form.get('Temperature'))
            RH = float(request.form.get('RH'))
            Ws = float(request.form.get('Ws'))  # fixed 'Wh'
            Rain = float(request.form.get('Rain'))
            FFMC = float(request.form.get('FFMC'))
            DMC = float(request.form.get('DMC'))
            ISI = float(request.form.get('ISI'))
            Classes = float(request.form.get('Classes'))
            Region = float(request.form.get('Region'))

            # Pass actual values, not column names
            input_data = [[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]]
            new_data_scaled = standardize_model.transform(input_data)
            result = ridge_pickle.predict(new_data_scaled)

            return render_template('home.html', results=result[0])

        except Exception as e:
            return f"Error occurred: {e}"

    else:
        return render_template('home.html')

                                      

if __name__=='__main__':
    app.run(host='0.0.0.0')


