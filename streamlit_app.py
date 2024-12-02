import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

st.title('MAI Dashboard')

df = pd.read_csv('https://raw.githubusercontent.com/LUCE-Blockchain/Databases-for-teaching/refs/heads/main/Framingham%20Dataset.csv')

'## Project data'
'If you show data in streamlit they can get nicely formatted as dataframe (you can even scroll!)'
# look at the data
st.dataframe(df)

'## Data visualization'
'You can show data visualizations from different modules, such as matplotlib or altair'

'### Age vs Systolic BP using matplotlib'
fig, ax = plt.subplots()
ax.scatter(df.AGE, df.SYSBP, alpha=0.2)
st.pyplot(fig)

'### Age vs Systolic BP using Altair'
chart = alt.Chart(df).mark_circle().encode(
    x='AGE',
    y='SYSBP'
)

st.altair_chart(chart)

'## Adding interactivity'
'It is super easy to create widgets, and immediately store the selected value in a variable'

yvar = st.selectbox(label='Enter y-axis variable',
                     options=['SYSBP', 'DIABP', 'CIGPDAY'])
fig, ax = plt.subplots()
ax.scatter(df.AGE, df[yvar], alpha=0.3)
st.pyplot(fig)

'''You can also use a widget to hide a section in your code,
with just a simple `if` statement!'''


show_extra_plot = st.checkbox('Show colorful plot:')
if show_extra_plot:
    chart = alt.Chart(df).mark_bar().encode(
        x='mean(TOTCHOL)',
        y='SEX:N',
        color='SEX:N'
    )
    st.altair_chart(chart)

