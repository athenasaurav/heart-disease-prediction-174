import pickle
import numpy as np

# load trained model
model = pickle.load(open("heart_trained_model.p", "rb"))

# function to do prediction
def predict_heart(age, sex, cp, thalach, exang, oldpeak, slope, ca, thal):
    # prepare input as a list
    X = [age, sex, cp, thalach, exang, oldpeak, slope, ca, thal]
    X = np.reshape(X, (1,-1))    
    return model.predict(X)[0]