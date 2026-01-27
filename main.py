import os
from dotenv import load_dotenv

from langchain_core.messages import  HumanMessage,AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

GEMINI_API_KEY=os.getenv('GEMINI_API')
TODOIST_API_KEY=os.getenv('TODOIST_API')

model = ChatGoogleGenerativeAI(
    model='gemini-3-flash-preview',
    google_api_key=GEMINI_API_KEY,
    temperature=1
)
system_prompt = """
You are a helpful assistance, You will help the user to add task.
"""

user_input = "Tell me a joke today"

prompt = ChatPromptTemplate([
     ("system",system_prompt)
    ,("user", user_input)])

chain = prompt | model | StrOutputParser()

response = chain.invoke({
    "input": user_input
})

print(response)

