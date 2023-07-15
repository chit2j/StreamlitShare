#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 13:59:29 2023

@author: nawchittoojune
"""

# import the streamlit library
import streamlit as st
import joblib

# give a title to our app
st.title('Will you survive or not if you were on the Titanic?')
Titanic_LR_Model = joblib.load("Titanic_LR_Model.pkl")

image = 'titanic.jpg'  # Replace 'path_to_image.jpg' with the actual path to your image file
st.image(image, caption='Titanic Image by Đỗ Thiệp from Pixabay')
#Image by Đỗ Thiệp from Pixabay
name = st.text_input('Enter your name', '')

if name:

    st.success(f" **Hi {name}!This prediction is just for fun. For prediction, Please provide your age, passenger class, number of siblings, and number of parents/children accompanying you on the Titanic, if applicable.**")
    

    # Create radio buttons
    sex= st.radio("Select your Gender", ("Male", "Female"))
    if sex=="Male":
        g=0
    else:
        g=1
        
    c= st.radio("Select your Class", ("First Class", "Second Class","Third Class"))
    if c=="First Class":
        pclass=1
    elif c=="Second Class":
        pclass=2
    else:
        pclass=3
    
    age = st.number_input('Enter your age', min_value=0, max_value=100, value=25, step=1)
    
    sib = st.number_input('Enter the number of siblings /spouse accompanying you', min_value=0, max_value=100, value=0, step=1)
    
    
    parch = st.number_input('Enter the number of parents/childern accompanying you', min_value=0, max_value=100, value=0, step=1)
    
    
    
    data=[g,pclass,age,sib,parch]
    
    result=Titanic_LR_Model.predict([data])
    
    button_clicked = st.button("Predict")
    if button_clicked:
        
        if result==0:
            st.success(f"**Based on the available data, {name} !You will not survive if you were on the Titanic**")
        else:
            st.success(f"**Based on the available data, {name} !You will survive if you were on the Titanic**")

