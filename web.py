import os
from dotenv import load_dotenv
import getpass

from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI

import gradio as gr
from langchain_google_genai.chat_models import ChatGoogleGenerativeAIError

load_dotenv()

gemini_key = os.getenv('GOOGLE_API_KEY')


if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")

model = ChatGoogleGenerativeAI(
    model='gemini-3-flash-preview',
    google_api_key=gemini_key,
    temperature=0.7
)

system_prompt = """
You are elbert Einstein, you are expert in physics, as well as the concept,
of making it easier to explain, also relate the concept with some real life 
example, also you are bit humorous, reply with that tone,
answer each query min 1 line or max 4-5 lines not beyond that keep it short
"""

#creating prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder("history"),
    ("user", "{input}")

])
#creating chain
chain = prompt | model | StrOutputParser()

def submit_chat(user_mes,hist):
    try:
        langchain_history=[]
        for item in hist:
            if item['role'] == 'user':
                langchain_history.append(HumanMessage(content=item['content']))
            elif item['role'] == 'assistant':
                langchain_history.append(AIMessage(content=item['content']))

        response = chain.invoke({"input": user_mes, "history":langchain_history})

        return "",hist + [{"role": "user", "content": user_mes},
                          {"role": "assistant", "content": response}]
    except ChatGoogleGenerativeAIError as e:
        return  "", [{"role": "user", "content":user_mes},
            {"role": "assistant",
                    "content": "⚠️Sorry, Einstein reached his limit today"}]

    except Exception as e:
        return "", [{"role": "user", "content":user_mes},
            {"role": "assistant",
                    "content": f"unexpected error: {str(e)}"}]


def clear_chat():
    return "",[]

page = gr.Blocks(title="Chat with Einstein")

with page:
    gr.Markdown(
        """
        # Chat with Einstein
        Welcome to personal conversation with Albert Einstein!
        """
    )
    chatbox = gr.Chatbot(show_label=False,avatar_images=(None,"Einstein.jpg"))

    msg= gr.Textbox(placeholder="Ask me anything", autofocus=True,show_label=False)

    msg.submit(submit_chat, inputs=[msg,chatbox], outputs=[msg,chatbox])

    clear = gr.Button(value='Clear', variant='primary',)
    clear.click(fn=clear_chat, outputs=[msg,chatbox])

page.launch(share=True,
            theme=gr.themes.Glass(font=[gr.themes.GoogleFont("Inconsolata"),
            "Arial", "sans-serif"],text_size='lg'),)