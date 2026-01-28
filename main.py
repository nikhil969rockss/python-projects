import os
from dotenv import load_dotenv
from langchain_core.agents import AgentActionMessageLog

from langchain_core.messages import  HumanMessage,AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain.agents import create_agent,AgentState
from todoist_api_python.api import TodoistAPI

load_dotenv()

GEMINI_API_KEY=os.getenv('GEMINI_API')
TODOIST_API_KEY=os.getenv('TODOIST_API')

todoist = TodoistAPI(TODOIST_API_KEY)

@tool
def add_task(task:str, desc:str|None=None)-> None:
    """add task to the list, if user ask to add task something"""
    todoist.add_task(content=task,description=desc)

tools = [add_task]
model = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    google_api_key=GEMINI_API_KEY,
    temperature=1
)
system_prompt = """
You are a helpful assistance, You will help the user to add task.
if user want to add todo or task use add_task tool
"""

prompt = ChatPromptTemplate([
     ("system",system_prompt),
     MessagesPlaceholder("history"),
     ("user", "{input}")
])

# chain = prompt | model | StrOutputParser()
parser = StrOutputParser()
agent = create_agent(model=model, tools=tools)

state =  AgentState(
    messages=[]
)

while True:
    user_input = input("You: ")
    state['messages'].append(HumanMessage(content=user_input))

    state = agent.invoke(state)

    ai_response = state['messages'][-1]

    print("AI:",ai_response.content)
