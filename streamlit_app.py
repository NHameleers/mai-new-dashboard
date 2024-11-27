import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('MAI Dashboard')

df = pd.read_csv('https://raw.githubusercontent.com/LUCE-Blockchain/Databases-for-teaching/refs/heads/main/Framingham%20Dataset.csv')

'## Project data'
# look at the data
st.dataframe(df)

'## Matplotlib figure'
fig, ax = plt.subplots()
ax.scatter(df.AGE, df.SYSBP, alpha=0.3)
st.pyplot(fig)

'## Adding interactivity'
yvar = st.selectbox(label='Enter y-axis variable', options=['SYSBP'])
fig, ax = plt.subplots()
ax.scatter(df.AGE, df[yvar], alpha=0.3)
st.pyplot(fig)

