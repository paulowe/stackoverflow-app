from typing import no_type_check
import streamlit as st
import numpy as np
import pickle

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()
regressor_loaded = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_predict_page():
    st.title("Software Developer Salary prediction") #to display title
    st.write("""### We need some information to predict the salary""")