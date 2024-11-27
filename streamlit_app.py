import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('MAI Dashboard')

df = pd.read_csv('https://raw.githubusercontent.com/LUCE-Blockchain/Databases-for-teaching/refs/heads/main/Framingham%20Dataset.csv')

st.dataframe(df.head())