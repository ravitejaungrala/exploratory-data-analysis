import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import random
from PIL import Image
logo = Image.open('logo.png')
#pip install pandas numpy matplotlib seaborn streamlit
#to run strealit :   streamlit run test2.py 
st.set_page_config(page_title="Police  EDA", page_icon=":bar_chart:", layout="wide")
st.image(logo)
# Define the list of names
names = ["21A21A6159-U.N.V RAVITEJA", "21A21A6106-B.MANIKANTA", "21A21A6105-B.VINAY BHASKAR","21A21A6150-R.POOJA SRI","22A21A6106-V.SAI GANESH","21A21A6153-SK.N.KHASIM","21A21A6117-J.VENKATA LAKSHMI","21A21A6109-D.PREM KUMAR"]
st.title("Exploratory Data Analysis on Police Data Set")
# Add the names to the sidebar
st.sidebar.title("Project Team Members:")

for name in names:
    st.sidebar.write(name)
st.sidebar.title("Under The Guidance of :")
st.sidebar.write("Dr.Bomma.Ramakrishna")
# File upload
uploaded_file = st.file_uploader("Choose a Police Dataset csv")
if uploaded_file is not None:
    data=pd.read_csv(uploaded_file)
    st.dataframe(data)

    st.title("Police Data Analysis")



    # Display data
    if st.checkbox("Show data"):
        st.write(data.head())

    if st.checkbox("Describe police Data"):
       st.write(data.describe())
    
   
    if st.checkbox("Show first 25 rows"):
        st.write(data.head(25))

    if st.checkbox("Show shape"):
        st.write(data.shape)

    if st.checkbox("Show index"):
        st.write(data.index)

    if st.checkbox("Show columns"):
        st.write(data.columns)

    #if st.checkbox("Show data types"):
        # Convert data types to strings as a workaround for Arrow bug
        #data = data.astype(str)
        #st.dataframe(data.dtypes)

    if st.checkbox("Show count of non-null values"):
        st.write(data.count())

    if st.checkbox("Show all Null Values"):
        st.write(data.isnull().sum())

    # Remove column with missing values
    if st.checkbox("Remove column with missing values"):
        data.drop(columns="country_name", inplace=True)
        st.write("Column 'country_name' removed.")

    

    # For speeding, were men or women stopped more often?
    if st.checkbox("For speeding, were men or women stopped more often?"):
        gender_counts = data[data.violation == "Speeding"].driver_gender.value_counts()
        st.write(gender_counts)

    # Does gender affect who gets searched during a stop?
    if st.checkbox("Does gender affect who gets searched during a stop?"):
        search_conducted = data.groupby("driver_gender").search_conducted.sum()
        st.write(search_conducted)
        st.write(data.search_conducted.value_counts())

    # What is the mean stop duration?
    if st.checkbox("What is the mean stop duration?"):
        stop_duration_map = {"0-15 Min": 7.5, "16-30 Min": 24, "30+ Min": 45}
        data["stop_duration"] = data["stop_duration"].map(stop_duration_map)
        mean_duration = data["stop_duration"].mean()
        st.write("Mean stop duration:", mean_duration)

    # Compare the age distributions for each violation
    if st.checkbox("Compare the age distributions for each violation"):
        age_distribution = data.groupby("violation").driver_age.describe()
        st.write(age_distribution)

   

   

    # Display bar plot of violation counts
    if st.checkbox("Show bar plot of violation counts"):
        violation_counts=data['violation'].value_counts()
        st.bar_chart(violation_counts)

  
   