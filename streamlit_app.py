import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('MAI Dashboard')

df = pd.read_csv('https://raw.githubusercontent.com/LUCE-Blockchain/Databases-for-teaching/refs/heads/main/Framingham%20Dataset.csv')

# st.dataframe(df.head())

# add matplotlib figure
fig, ax = plt.subplots()
ax.scatter(df.AGE, df.SYSBP, alpha=0.3)
st.pyplot(fig)