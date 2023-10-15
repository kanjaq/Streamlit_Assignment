import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

def load_data():
    df = pd.read_csv('IRIS.csv')
    return df

data = load_data()

st.title('IRIS DATA SET')
st.write('Exploration of Iris Data set')

if st.checkbox("Show raw data"):
    st.subheader("iris Data")
    st.dataframe(data)
else:
    st.write('Click to show the data')

# Question 1: Show the average sepal length for each species

if st.checkbox('Show the average sepal length for each species'):
    st.subheader('Average sepal length')
    grouped_data = data.groupby('species')['sepal_length'].mean()
    st.write(grouped_data)

# Question 2: Display a scatter plot comparing two features
st.subheader("Compare two features using a scatter plot")
feature_1 = st.selectbox("Select the first feature:", data.columns[:-1])
feature_2 = st.selectbox("Select the second feature:", data.columns[:-1])

scatter_plot = px.scatter(data, x=feature_1, y=feature_2, color="species", hover_name="species")
st.plotly_chart(scatter_plot)

# Question 3: Filter data based on species
st.subheader('Filtering data based on species')
selected_species = st.multiselect('Select species to display: ', data['species'].unique())

if selected_species:
    filtered_data = data[data["species"].isin(selected_species)]
    st.dataframe(filtered_data)
else:
    st.write('No species selected')

# Question 4: Display a pairplot for the selected species

if st.checkbox('Selected Species'):
    st.subheader('Display a pairplot')

    if selected_species:
        sns.pairplot(filtered_data, hue="species")
    else:
        sns.pairplot(data, hue="species")
        
    st.pyplot(data)


