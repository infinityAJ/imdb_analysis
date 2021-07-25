import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt 
import plotly.express as px

st.set_page_config(layout='wide', page_title="IMDB data analysis")

@st.cache
def load_movies_data():
    df = pd.read_csv('data\IMDb movies.csv')
    return df

st.title("Data Analysis of IMDB Movies") 
st.write("")
c = st.beta_columns(3)
c[0].image('sorte.jpg',use_column_width=True)
c[1].image('Miss_Jerry_(1894).jpg',use_column_width=True)
c[2].image('kelly.jpg',use_column_width=True)
st.markdown("<hr>", unsafe_allow_html=True)

data = load_movies_data()

if st.sidebar.checkbox("view data"):
   st.header("View Raw Data")
   st.write("")
   row_size = st.sidebar.slider('size of records',value=10, min_value=0, max_value=data.shape[0])
   st.write(data.head(row_size))
   st.markdown("<hr>", unsafe_allow_html=True)

if st.sidebar.checkbox("show plot"):
   st.header("Plot of every column in the dataset")
   st.write("")
   fig, ax = plt.subplots()
   data.plot(ax=ax)
   st.pyplot(fig)
   st.markdown("<hr>", unsafe_allow_html=True)

if st.sidebar.checkbox("duration"):
   st.header("show duration and year")
   st.write("")
   fig = px.bar(data, x='duration',y='year')
   st.plotly_chart(fig)
   st.markdown("<hr>", unsafe_allow_html=True)

if st.sidebar.checkbox("pie chart"):
   st.header("Pie chart of countries")
   st.write("")
   fig = px.pie(data, names='country')
   st.plotly_chart(fig)
   st.markdown("<hr>", unsafe_allow_html=True)

if st.sidebar.checkbox("language"):
   st.header("Pie chart of languages")
   st.write("")
   fig = px.pie(data, names='language', color_discrete_sequence=px.colors.sequential.RdBu,title='Most used language in movies')
   st.plotly_chart(fig)
   st.markdown("<hr>", unsafe_allow_html=True)
