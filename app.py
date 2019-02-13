from flask import Flask, request, jsonify
import flask.json as json
import sys
import os
import heart_model as heart

app = Flask(__name__)

# return default response for root folder
@app.route('/')
def root():
    python_version = "\npython-version%s\n" % sys.version
    return python_version 

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

@app.route('/dialogflow', methods=['post'])
def dialogflow():
    result = {'fulfillmentText':'n/a'}
    try:
        input = request.get_json()
        if input['queryResult']['intent']['displayName'] == 'predict':
            for context in input['queryResult']['outputContexts']:
                if context['name'].endswith('user-data'):
                    print('context name: {}'.format(context['name']))
                    params = context['parameters']
                    
                    print(params.get('age'))
                    print(params.get('sex'))
                    print(params.get('cp'))
                    print(params.get('thalach'))
                    print(params.get('exang'))
                    print(params.get('oldpeak'))
                    print(params.get('slope'))
                    print(params.get('ca'))
                    print(params.get('thal'))

                    age = int(params.get('age'))
                    sex = int(params.get('sex'))
                    cp = int(params.get('cp'))
                    thalach = int(params.get('thalach'))
                    exang = int(params.get('exang'))
                    oldpeak = float(params.get('oldpeak'))
                    slope = int(params.get('slope'))
                    ca = int(params.get('ca'))
                    thal = int(params.get('thal'))

                    output = heart.predict_heart(age, sex, cp, thalach, exang, oldpeak, slope, ca, thal)
                    print('The prediction is {}'.format(output))
                    
                    result = {'fulfillmentText':'Our amazing machine algorithm predicted that you {} a heart disease'.format('have' if output==1 else 'do no have')}
        else:
            result = {'fulfillmentText':'Our amazing machine learning algorithm predicted that you may have a heart disease'}
    except Exception as e:
        print('error: ', e)

    return json.dumps(result)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 9099))
    app.run(host='0.0.0.0', port=port, debug=True)