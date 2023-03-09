import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns



st.title("Palmer's penguins")
st.markdown('Use this Streamlit app to make your own scatterplot about penguins!')
penguin_file = st.file_uploader("Select Your Local Penguins CSV (default provided)")
if penguin_file is not None:
    penguins_df = pd.read_csv(penguin_file)
else:
    penguins_df = pd.read_csv("penguins.csv")
#selected_species = st.selectbox('what species',['Adelie','Gentoo','Chinstrap'])
selected_x_var = st.selectbox('What do want the x variable to be?',
     ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])
selected_y_var = st.selectbox('What about the y?',
     ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])
#import the csv
penguins_df = pd.read_csv('penguins.csv')
#penguins_df = penguins_df[penguins_df['species'] == selected_species] 
alt_chart = (
    alt.Chart(penguins_df,title=f"Scatterplot of  Penguins")
    .mark_circle()
    .encode(
        x=selected_x_var,
        y=selected_y_var,
        color = "species",
    )
    .interactive()
)
st.altair_chart(alt_chart,use_container_width=True )
st.write(penguins_df.head())