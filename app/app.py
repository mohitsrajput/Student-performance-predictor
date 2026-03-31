import streamlit as st
from src.predict import predict

st.title('Student Performance Predictor')

study = st.number_input('Study Hours')
attendance = st.number_input('Attendance')
marks = st.number_input('Previous Marks')

if st.button('Predict'):
    result = predict([study, attendance, marks])
    st.success(f'Predicted Score: {result[0]}')
