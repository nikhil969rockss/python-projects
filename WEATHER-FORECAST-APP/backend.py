import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
print(API_KEY)

def get_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"

    response = requests.get(url)
    data = response.json()
    forecast_data = data["list"]
    return forecast_data


if __name__ == '__main__':
    get_weather_data("new york")


