import streamlit as st
import pandas as pd
st.title('SF Trees')
st.write(
    """This app analyses trees in San Francisco using
    a dataset kindly provided by SF DPW"""
)
trees_df = pd.read_csv('trees.csv')
df_dbh_grouped = pd.DataFrame(trees_df.groupby(['DBH']).count()['TreeID'])
df_dbh_grouped.columns = ['tree_count']
st.line_chart(df_dbh_grouped)
st.bar_chart(df_dbh_grouped)
st.area_chart(df_dbh_grouped)