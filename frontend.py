import streamlit as st

st.title("Weather Forecast For The Next Days")

place = st.text_input(label="Place: ",help="Enter a place to find forecast for",
                      max_chars=100)
forecast_days = st.slider(label="Forcast Days for",min_value=1, max_value=5 )
weather_selection = st.selectbox(label="Select data to view",
                                 options=["Temperature", "Sky"])

st.subheader(f"Temperature for the next {forecast_days} days in {place}" )


