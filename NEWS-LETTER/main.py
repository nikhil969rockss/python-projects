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

body="Subject: Today's top news on TECHNOLOGY" + '\n'
news_number =1
for article in articles:

      if article["title"] is not None and article["description"] is not None:

          news_count = f"News-{news_number}" + '\n'
          title = f"Title- {article["title"]}" + 2*'\n'
          description = "Description- " + article["description"]+ '\n'
          link = "Read full article: " + article["url"] + 3*'\n'

          body =  body  + news_count+ title + description + link
          news_number+=1

body = body.encode('utf-8')
send_email(message=body)
