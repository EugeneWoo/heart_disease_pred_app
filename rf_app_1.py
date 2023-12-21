#!/usr/bin/env python
# coding: utf-8

# import necessary libraries
import pandas as pd
import numpy as np
import sklearn
import streamlit as st
import joblib

# load the model object into the python file.
model = joblib.load("randomforest_heartdisease.joblib")

# set up the streamlit page settings
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(page_title="Heart Disease Psychic", layout="wide")

# Take input from users for numerical features  
input_array = np.empty((1,4))

# def main():
with st.form("Personal_Particulars"):
             
    choices = {0: "male", 1: "female"}
    def format_func(option):
        return choices[option]
        
    age_option = st.sidebar.slider("What is your age?", 25, 80, value=25)
    sex_option = st.sidebar.selectbox("What is your gender?", options=list(choices.keys()), format_func=format_func)
    bp_option = st.sidebar.slider("What is your systolic blood pressure in mmHg?", 90, 210, value=90)
    cholestrol_option = st.sidebar.slider("What is your total cholesterol level in mg/dL?", 120, 570, value=120)

    st.header('**Just confirming your selection**', divider='rainbow')

    st.write('You are ', age_option, ' years old.')
    # st.write(f"You selected option {sex_option} representing {format_func(sex_option)}")
    st.write(f"You are a {format_func(sex_option)}.")
    st.write("Your systolic blood pressure is", bp_option, "mmHg.")
    st.write("Your total cholesterol is", cholestrol_option, "mg/dL.")
        
    # User to submit options to predict heart disease
    submit = st.form_submit_button("Predict")

if submit:
    input_array = np.array([age_option,sex_option,bp_option,cholestrol_option], ndmin=2)
    
    # user_data = pd.DataFrame({
    #     "age": [age_option],
    #     "sex": [sex_option],
    #     "BP": [bp_option],
    #     "cholestrol": [cholestrol_option]
    #     })

# predict the output using model object
prediction = model.predict(input_array)[0]

def hd_predict(prediction):
    if prediction == 0:
        hd_pred = 'live a life free of heart disease'
        pred_prob = model.predict_proba(input_array)[0][prediction]
    else: 
        hd_pred = 'suffer from heart disease in future'
        pred_prob = model.predict_proba(input_array)[0][prediction]
    return(hd_pred,pred_prob)

st.write("You are expected to",hd_predict(prediction)[0],"with a probability of",round(hd_predict(prediction)[1],2)*100,"%.")

# if __name__ == '__main__':
#     main()

