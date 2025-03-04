import streamlit as st
from model import load_model
from prediction import predict_cost

model = load_model()

st.title("Predicción de Costos")

factor1 = st.number_input("Factor 1")
factor2 = st.number_input("Factor 2")
factor3 = st.number_input("Factor 3")

if st.button("Predecir"):
    input_data = [factor1, factor2, factor3]
    prediction = predict_cost(model, input_data)
    st.write(f"Predicción del costo: {prediction[0]}")
