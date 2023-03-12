import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport



# Define la función st_profile_report para mostrar el informe
def st_profile_report(pr):
    """
    Función para mostrar el informe de pandas_profiling en Streamlit
    """
    report = pr.to_html()
    report = report.replace('<head>', '<head><meta charset="UTF-8">')
    st.write(report, unsafe_allow_html=True)


    
data = pd.read_csv("penguins.csv")


# Genera el informe utilizando pandas_profiling
profile = ProfileReport(data, title='Pandas Profiling Report', explorative=True)

# Muestra el informe en Streamlit utilizando el widget 'st_pandas_profiling_report'
st_profile_report(profile)
