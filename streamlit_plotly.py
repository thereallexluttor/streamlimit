import streamlit as st
import pandas as pd
import plotly.express as px


st.title('SF Trees')
st.write('this app analyses trees in an francisco')
st.subheader('ploty chart ')

trees_df = pd.read_csv('trees.csv')
fig = px.histogram(trees_df['DBH'])
st.plotly_chart(fig)