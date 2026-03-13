import streamlit as st
import plotly.express as px
from backend import get_weather_data

st.title("Weather Forecast For The Next Days")

place = st.text_input(label="Place: ",help="Enter a place to find forecast for",
                      max_chars=100)
forecast_days = st.slider(label="Forcast Days for",min_value=1, max_value=5,
                          help="Select number of days to forecast for")
weather_selection = st.selectbox(label="Select data to view",
                                 options=["Temperature", "Sky"],
                                 )

st.subheader(f"Temperature for the next {forecast_days} days in {place}" )



if place:
    try:
        forecasted_weather = get_weather_data(city=place)
        number_of_days = 8 * forecast_days
        forecasted_weather = forecasted_weather[:number_of_days]

        if weather_selection == "Temperature":

            temperatures = [data["main"]["temp"]/10 for data in
                            forecasted_weather]

            dates = [item['dt_txt'] for item in forecasted_weather]

            figure = px.line(x=dates, y=temperatures,
                     labels={"x": "Date", "y": "Temperature (C)"})
            # This requires a figure object which can be built by bokeh, or plotly
            # library
            st.plotly_chart(figure)

        elif weather_selection == 'Sky':
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}

            weather_conditions = [item["weather"][0]["main"]  for item in
                                  forecasted_weather]

            img_array = [images[condition] for condition in weather_conditions]

            weather_conditions = [item["weather"][0]["main"] + '\n\n' +item["dt_txt"]
                                  for item in forecasted_weather]

            st.image(image=img_array, width=100,caption=weather_conditions)

    except KeyError :
        st.write(f"Invalid city {place} does not exist ")


