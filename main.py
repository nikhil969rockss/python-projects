import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

gemini_key = os.getenv('GEMINI_API_KEY')

model = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash-lite',
    google_api_key=gemini_key,
    temperature=0.7
)


system_prompt = """
You are elbert Einstein, you are expert in physics, as well as the concept,
of making it easier to explain, also relate the concept with some real life 
example, also you are bit numerous, reply with that tone,
answer each query min 1 line or max 4-5 lines not beyond that keep it short
"""

print("AI: Hello I'm Albert Einstein, How can i assist you: ")
user_input = input("You: ")

response = model.invoke([{"role": "system", "content": system_prompt},
              {"role": "user", "content": user_input}])
print(response.content)