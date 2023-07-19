import streamlit as st
import pandas as pd
import pickle

def main():
    st.title("Heart Disease Prediction")
    # User input fields
    age = st.number_input("age", value=0, min_value=0, max_value=150, step=1)
    gender = st.selectbox("gender", options=["Female", "Male"])
    height = st.number_input("height (cm)", value=0.0, min_value=0.0, step=1.0)
    weight = st.number_input("weight (kg)", value=0.0, min_value=0.0, step=0.1)
    ap_hi = st.number_input("systolic Blood Pressure", value=0, min_value=0, max_value=300, step=1)
    ap_lo = st.number_input("diastolic Blood Pressure", value=0, min_value=0, max_value=300, step=1)
    cholesterol = st.selectbox("cholesterol", options=["Normal", "Above Normal", "Well Above Normal"])
    gluc = st.selectbox("gluc", options=["Normal", "Above Normal", "Well Above Normal"])
    smoke = st.selectbox("Smoking", options=["No", "Yes"])
    alco = st.selectbox("alco Consumption", options=["No", "Yes"])
    active = st.selectbox("active", options=["No", "Yes"])
    
    # Convert categorical inputs to numeric
    gender = 1 if gender == "Male" else 0
    cholesterol = convert_label(cholesterol)
    gluc = convert_label(gluc)
    smoke = 1 if smoke == "Yes" else 0
    alco = 1 if alco == "Yes" else 0
    active = 1 if active == "Yes" else 0
    
    # Create feature DataFrame
    data = pd.DataFrame({
        "age": [age],
        "gender": [gender],
        "height": [height],
        "weight": [weight],
        "ap_hi": [ap_hi],
        "ap_lo": [ap_lo],
        "cholesterol": [cholesterol],
        "gluc": [gluc],
        "smoke": [smoke],
        "alco": [alco],
        "active": [active]
    })
    
    # Load the trained model
    model = load_model()
    
    # Make prediction
    if st.button("Predict"):
        result = predict(model, data)
        st.write("Prediction:", result)

def load_model():
    # Load the pre-trained model
    with open("model_pickle (2).pkl", "rb") as file:
        model = pickle.load(file)
    return model

def predict(model, data):
    # Perform prediction using the loaded model
    result = model.predict(data)
    return result[0]

def convert_label(label):
    if label == "Normal":
        return "great you are fit, it is time to celebrate"
    elif label == "Above Normal":
        return "oops you are most likely to be having a disease"
    elif label == "Well Above Normal":
        return "oops you are most likely to have a disease"

if __name__ == "__main__":
    main()