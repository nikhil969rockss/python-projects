import os
from dotenv import load_dotenv
from langchain_core.agents import AgentActionMessageLog

from langchain_core.messages import  HumanMessage,AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain.agents import create_agent
from todoist_api_python.api import TodoistAPI

load_dotenv()

GEMINI_API_KEY=os.getenv('GEMINI_API')
TODOIST_API_KEY=os.getenv('TODOIST_API')

todoist = TodoistAPI(TODOIST_API_KEY)

@tool
def add_task(task:str, desc:str=None)-> None:
    """add task to the list, if user ask to add task something"""
    todoist.add_task(content=task,description=desc)

tools = [add_task]
model = ChatGoogleGenerativeAI(
    model='gemini-3-flash-preview',
    google_api_key=GEMINI_API_KEY,
    temperature=1
)
system_prompt = """
You are a helpful assistance, You will help the user to add task.
if user want to add todo or task use add_task tool
"""

user_input = "add a task for buy milk with description only amul"

prompt = ChatPromptTemplate([
     ("system",system_prompt)
    ,("user", user_input)])

# chain = prompt | model | StrOutputParser()

agent = create_agent(model=model, tools=tools)


response = agent.invoke(
    {"messages": [{"role": "user", "content": user_input}]}
)

print(response['messages'])

