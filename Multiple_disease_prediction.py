# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 00:08:48 2022

@author: dell
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models

diabetes_model= pickle.load(open('diabetes_model.sav','rb'))
heart_model= pickle.load(open('heart_disease.sav','rb'))
parkinsons_model= pickle.load(open('parkinsons.sav','rb'))

#sidebar for navigate

with st.sidebar:
    selected=option_menu('Multiple Disease Prediction System',
                         ['Diabetes Prediction',
                          'Heart Disease Prediction',
                          'Parkinsons Prediction'],
                         icons=['activity','heart','person'],
                         default_index=0)
    
#diabetes prediction page
if (selected=='Diabetes Prediction'):
    #page title
    st.title('Diabetes Prediction using ML')
    
    #getting the input data
    
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies=st.text_input('Number of Pregnancies')
    
    with col2:
        Glucose=st.text_input('Glucose Level')
    
    with col3:
        BloodPressure=st.text_input('Blood Pressure Value')

    with col1:
        SkinThickness=st.text_input('Skin Thickness Value')

    with col2:
        Insulin=st.text_input('Insulin Level')

    with col3:
        BMI=st.text_input('BMI Value')
   
    with col1:
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function Value')
    
    with col2:
        Age=st.text_input('Age')
        
    #CODE FOR PREDICTION
    diab_diagnosis=''
    
    #creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if(diab_prediction[0]==1):
            diab_diagnosis='You are Diabetic'
        else:
            diab_diagnosis='You are not Diabetic'
    
    st.success(diab_diagnosis)
    

if (selected=='Heart Disease Prediction'):
    #page title
    st.title('Heart Disease Prediction using ML')
    
    #getting the input data
    
    col1,col2,col3=st.columns(3)
    
    with col1:
        age=st.text_input('Age')
    
    with col2:
        sex=st.text_input('Sex')
    
    with col3:
        cp=st.text_input('Chest Pain Type (4 values)')

    with col1:
        trestbps=st.text_input('Resting blood pressure')

    with col2:
        chol=st.text_input('Serum Cholestrol in mg/dl ')

    with col3:
        fbs=st.text_input('Fasting Blood Sugar > 120 mg/dl')
   
    with col1:
        restecg=st.text_input('Resting ECG (values 0,1,2)')
    
    with col2:
        thalach=st.text_input('Maximum Heart Rate')
    
    with col3:
        exang=st.text_input('Exercise induced angina')
        
    with col1:
         oldpeak=st.text_input('Old Peak')
    
    with col2:
         slope=st.text_input('Slope of the peak exercise')
     
    with col3:
         ca=st.text_input('No. of Major Vessels(0-3)')
         
    with col1:
         thal=st.text_input('0 = normal; 1 = fixed defect; 2 = reversable defect')
    
    #CODE FOR PREDICTION
    hrt_diagnosis=''
    
    #creating a button for prediction
    
    if st.button('Heart Disease Test Result'):
        hrt_prediction=heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if(hrt_prediction[0]==1):
            hrt_diagnosis='You have a Heart Disease'
        else:
            hrt_diagnosis='You are Healthy with no heart disease'
    
    st.success(hrt_diagnosis)
    
if (selected=='Parkinsons Prediction'):
    #page title
    st.title('Parkinsons Prediction using ML')
    col1,col2,col3,col4,col5=st.columns(5)
    
    with col1:
        Fo=st.text_input('MDVP:Fo(Hz)')
    
    with col2:
        Fhi=st.text_input('MDVP:Fhi(Hz)')
    
    with col3:
        Flo=st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent= st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs=st.text_input('MDVP:Jitter(Abs)')

    with col1:
         RAP=st.text_input('MDVP:RAP')
   
    with col2:
         PPQ =st.text_input('MDVP:PPQ')
    
    with col3:
         Jitter_DDP =st.text_input('Jitter:DDP')
    
    with col4:
         Shimmer=st.text_input('MDVP:Shimmer')
        
    with col5:
         Shimmer_dB=st.text_input('MDVP:Shimmer(dB)')
    
    with col1:
         APQ3=st.text_input('Shimmer:APQ3')
     
    with col2:
         APQ5=st.text_input('Shimmer:APQ5')
         
    with col3:
         APQ =st.text_input('MDVP:APQ')
    with col4:
        DDA=st.text_input('Shimmer:DDA')
    
    with col5:
        NHR =st.text_input('NHR')
    
    with col1:
        HNR= st.text_input('HNR')

    with col2:
        RPDE=st.text_input('RPDE')

    with col3:
        DFA=st.text_input('DFA')

    with col4:
        spread1=st.text_input('Spread1')
   
    with col5:
        spread2=st.text_input('Spread2')
    
    with col1:
        D2=st.text_input('D2')
    
    with col2:
        PPE=st.text_input('PPE')
        
    #CODE FOR PREDICTION
    parkinson_diagnosis=''
    
    #creating a button for prediction
    
    if st.button('Parkinson Disease Test Result'):
        parkinson_diagnosis_prediction=parkinsons_model.predict([[Fo,Fhi,Flo,Jitter_percent,Jitter_Abs,RAP,PPQ,Jitter_DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        if(parkinson_diagnosis_prediction[0]==1):
            parkinson_diagnosis='You have Parkinsons Disease'
        else:
            parkinson_diagnosis='You do not have Parkinsons Disease'
    
    st.success(parkinson_diagnosis)
    
    

    