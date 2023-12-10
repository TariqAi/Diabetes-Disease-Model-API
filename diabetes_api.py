# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 10:37:02 2023

@author: ZMZM
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

class model_input (BaseModel):
    
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int
    
    
#loaded the saved model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))



@app.post('/diabetes_prediction')
def diabetes_pred(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dectinory = json.loads(input_data)
    
    #Dectinory input
    preg = input_dectinory['Pregnancies']
    glu = input_dectinory['Glucose']
    bp = input_dectinory['BloodPressure']
    skin = input_dectinory['SkinThickness']
    insulin = input_dectinory['Insulin']
    bmi = input_dectinory['BMI']
    dpf = input_dectinory['DiabetesPedigreeFunction']
    age = input_dectinory['Age']
    
    #List input
    input_list = [preg, glu, bp, skin, insulin, bmi, dpf, age]
    
    prediction = diabetes_model.predict([input_list])
    
    if prediction[0] == 0:
        return 'The Person is not diabetic'
    else:
        return 'The Person is diabetic'
    
    
    
    
    
    
    
    
    