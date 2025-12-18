import streamlit as st
import requests

st.title("🚀 Streamlit → Flask Integration")

name = st.text_input("Enter your name")

if st.button("Call Flask API"):
    if name:
        response = requests.get(f"http://127.0.0.1:5000/hello/{name}")
        data = response.json()
        st.success(data["message"])
    else:
        st.warning("Please enter a name")
