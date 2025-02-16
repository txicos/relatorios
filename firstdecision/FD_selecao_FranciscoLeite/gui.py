import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8080/prod"

st.title("Data from API")

if st.button("Fetch Data"):
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  
        data = response.json()
        df = pd.DataFrame(data)
        for col in df.select_dtypes(include=['object']).columns:
          df[col] = df[col].astype(str)
        st.dataframe(df)
    except Exception as e:
        st.error(f"Failed to fetch data:\n{e}")
