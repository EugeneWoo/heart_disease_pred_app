#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# import necessary libraries
import pandas as pd
import numpy as np
# import scikit-learn
import streamlit as st
import joblib
import shap
import matplotlib
# from IPython import get_ipython
# from PIL import Image

# load the model object into the python file.
model = joblib.load("randomforest_heartdisease.joblib")

# set up the streamlit page settings
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(page_title="Heart Disease Psychic", layout="wide")


# In[ ]:


# Take input from users for numerical features  

def main():
    with st.form("road_traffic_severity_form"):
        age_option = st.sidebar.slider("What is your age?", 25, 80, value=25)
        st.write('You are ', age_option, ' years old.')

        choices = {0: "Male", 1: "Female"}
        def format_func(option):
            return choices[option]

        sex_option = st.sidebar.selectbox("What is your gender? Select 0 for male and 1 for female.", options=list(choices.keys()), format_func=format_func)
        st.write(f"You selected option {sex_option} representing {format_func(sex_option)}")

        bp_option = st.sidebar.slider("What is your systolic blood pressure in mmHg?", 90, 210, value=90)
        st.write("Your systolic blood pressure is", bp_option, "mmHg.")

        cholestrol_option = st.sidebar.slider("What is your total cholesterol level in mg/dL?", 120, 570, value=120)
        st.write("Your total cholesterol is", cholestrol_option, "mg/dL.")
        
        # User hit submit button to predict heart disease
        submit = st.sidebar.form_submit_button("Predict")

    if submit:
        input_array = np.array([age_option,sex_option,bp_option,cholestrol_option], ndmin=2)

    # predict the output using model object
    prediction = model.predict(input_array)[0]
    
    def hd_predict(prediction):
        if prediction == 0:
            hd_pred = 'living a life free of heart disease.'
            pred_prob = rf_best.predict_proba(input_1)[0][prediction]
        else: 
            hd_pred = 'suffering from heart disease in future.'
            pred_prob = round(rf_best.predict_proba(input_1)[0][prediction],2)*100
        return(hd_pred,pred_prob)

    st.write("You have a",hd_predict(prediction)[1],"% probability of",hd_predict(prediction)[0])

if __name__ == '__main__':
    main()

