import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np 
import plotly.express as px
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
header =st.container()
dataset=st.container()
feacturs=st.container()
modet_training=st.container()

with header:
    st.title(" Canadian yearly Income Estimator")
with dataset:
    data=pd.read_csv('canada_per_capita_income.csv') 
    
       
    # Show the table data when checkbox is ON.
if st.checkbox('Show the dataset as table data'):
    st.table(data)

# Show the summary statistics as a table when checkbox is checked
if st.checkbox('Show summary statistics'):
    st.table(data.describe())
# Create the scatter plot
# Create the scatter plot
plt.title('PER CAPITA IN USD')
plt.scatter(data['year'], data['per capita income (US$)'], label="Per capita curve")
plt.xlabel("year")
plt.ylabel("per capita income (US$)")
plt.grid()
plt.legend()

# Display the scatter plot in Streamlit
st.pyplot()

# Create a scatter plot
fig = px.scatter(data, x='year', y='per capita income (US$)', title='PER CAPITA IN USD')
fig.update_layout(xaxis_title='Year', yaxis_title='Per capita income (US$)')

# Get the minimum and maximum years
min_year = data['year'].min()
max_year = data['year'].max()

# Animate the scatter plot based on selected year
year_input = st.slider('Select a year', min_value=int(min_year), max_value=int(max_year), step=1)

filtered_data = data[data['year'] <= year_input]
fig.data[0].x = filtered_data['year']
fig.data[0].y = filtered_data['per capita income (US$)']

# Display the animated scatter plot
st.plotly_chart(fig, animate=True)
# Create the scatter plot with animation
fig = px.scatter(data, x='year', y='per capita income (US$)', log_x=True, size_max=55,
                 range_x=[1970,2016], range_y=[100,10000],
                 animation_frame='year', animation_group='per capita income (US$)')

fig.update_layout(width=500, height=600)

# Display the scatter plot in Streamlit
st.write(fig)

options = list(range(1970, 2051))

# Create sidebar selectbox for year
selected_year = st.sidebar.selectbox("Select a year", options=options)
st.subheader("New dataframe")
new_df = data.drop('per capita income (US$)', axis='columns')
new_df
model = LinearRegression()
model.fit(new_df, data['per capita income (US$)'])

# Predict the per capita income for the selected year
prediction = model.predict([[selected_year]])

# Display the prediction
st.write("The predicted per capita income for year in", selected_year, "is", prediction[0])