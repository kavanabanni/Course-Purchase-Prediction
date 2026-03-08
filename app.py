import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Title
st.title("Student Course Purchase Prediction")

st.write("Enter student details to predict whether they will purchase the course.")

# User Inputs
age = st.number_input("Age", min_value=10, max_value=60, value=20)

study_hours = st.number_input("Study Hours Per Week", min_value=0, max_value=50, value=10)

previous_courses = st.number_input("Previous Courses Completed", min_value=0, max_value=20, value=2)

platform_visits = st.number_input("Platform Visits Per Month", min_value=0, max_value=100, value=15)

assignment_rate = st.number_input("Assignment Completion Rate (%)", min_value=0, max_value=100, value=80)

# Predict Button
if st.button("Predict Purchase"):

    input_data = np.array([[age, study_hours, previous_courses, platform_visits, assignment_rate]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Prediction: Student Likely to Purchase Course")
    else:
        st.error("Prediction: Student Not Likely to Purchase Course")