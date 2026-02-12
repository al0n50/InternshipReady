import streamlit as st
import pandas as pd
import plotly.express as px
from apis import apod_generator
import os

# in the terminal run: streamlit run dashboard.py
# if prompts you to enter email, just press enter/return
# if streamlit not recognized,  run:
#  python -m streamlit run dashboard.py

st.title("Water Quality Dashboard")
st.header("Internship Ready Software Development")
st.subheader("Alonso Ochoa")
st.divider()

df = pd.read_csv("biscayneBay_waterquality.csv")

tab1, tab2, tab3, tab4 = st.tabs(
    ["Descr. Stats",
     "2d plot",
     "3d plot",
     "NASA's APOD"]
)

with tab1:
    st.info("Working on this")
    st.dataframe(df)
    st.caption("Raw Data")
    st.divider()
    st.dataframe(df.describe())
    st.caption("Descriptive Statistics")

with tab2:
    st.info("Be patient")
    fig1 = px.line(df,
                   x="Time",
                   y="Temperature (c)")
    st.plotly_chart(fig1)

    fig2 = px.scatter(df,
                      x="ODO mg/L",
                      y="Temperature (c)",
                      color="pH")
    st.plotly_chart(fig2)

with tab3:
    st.success("Its worth the wait")
    fig3 = px.scatter_3d(df,
                         x="Longitude",
                         y="Latitude",
                         z="Total Water Column (m)")
    fig3.update_scenes(zaxis_autorange="reversed")
    st.plotly_chart(fig3)

with tab4:
    st.header("NASA's Astronomy Picture of Day")
    #TODO: call a function that generates the APOD
    url = "https://api.nasa.gov/planetary/apod?api_key="
    response = apod_generator(url,os.getenv("NASA_API_KEY"))

    #TODO: display the APOD image and title and other features

