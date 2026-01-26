import requests
from send_email import send_email
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY=os.getenv('API_KEY')

URL= ("https://newsapi.org/v2/"
      "top-headlines?country=us"
      "&category=technology"
      f"&apiKey={API_KEY}")

response = requests.get(url=URL)

data = response.json()
articles = data["articles"]

body=""
for article in articles:
      if article["title"] is not None and article["description"] is not None:
          body = body + article["title"] + '\n' + article["description"] + 2*'\n'

body = body.encode('utf-8')
send_email(message=body)
