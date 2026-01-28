import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
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

history=[]

#creating prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder("history"),
    ("user", "{input}")

])
#creating chain
chain = prompt | model | StrOutputParser()

print("Albert: Hello I'm Albert Einstein, How can i assist you: ")

while True:
    user_input = input("You: ")
    if user_input.strip()=='exit':
        break

    response = chain.invoke({"history": history,"input": user_input})
    print("Albert: ",response)
    history.append(HumanMessage(user_input))
    history.append(AIMessage(response))


