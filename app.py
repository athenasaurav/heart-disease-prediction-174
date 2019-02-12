from flask import Flask, request
import sys
import os
import heart_model as heart

app = Flask(__name__)

# return default response for root folder
@app.route('/')
def root():
    return '<h1>Heart Model Prediction</h1>'

# accept GET or POST methods
@app.route('/heart', methods=['get', 'post'])
def heart_predict():
    # age, sex, cp, thalach, exang, oldpeak, slope, ca, thal
    result = 'nil'
    try:
        age = int(request.values.get('age'))
        sex = int(request.values.get('sex'))
        cp = int(request.values.get('cp'))
        thalach = int(request.values.get('thalach'))
        exang = int(request.values.get('exang'))
        oldpeak = float(request.values.get('oldpeak'))
        slope = int(request.values.get('slope'))
        ca = int(request.values.get('ca'))
        thal = int(request.values.get('thal'))
        result = heart.predict_heart(age, sex, cp, thalach, exang, oldpeak, slope, ca, thal)
    except Exception as e:
        print('error:', e)
    return str(result)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 9099))
    app.run(host='127.0.0.1', port=port, debug=True)