import os
from dotenv import load_dotenv
from gradio.themes.builder_app import themes, sizes

from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI

import gradio as gr

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

page = gr.Blocks(
    title="Chat with Einstein",
    theme=gr.themes.Glass(font=[gr.themes.GoogleFont("Inconsolata"), "Arial", "sans-serif"],text_size='lg'),

)

with page:
    gr.Markdown(
        """
        # Chat with Einstein
        Welcome to personal conversation with Albert Einstein!
        """
    )
    chatbox = gr.Chatbot()

    msg= gr.Textbox()

    clear = gr.Button()
page.launch(share=True)