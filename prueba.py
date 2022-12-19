import streamlit as st
import pandas as pd
st.write("""PROYECTO FINAL""")
df=pd.read_csv("ENCUESTA.csv")
st.line_chart(df)