import streamlit as st
import functions
import os

if not os.path.exists("todos.txt") :
    with open("todos.txt","w") as file:
        pass

all_todos = functions.get_todos()



st.title("My Todo Web App")
st.subheader("This todo app was developed by Nikhil-R")
st.write("This is a minimal todo app to organise your day")

for todo in all_todos:
    st.checkbox(todo)


st.text_input(label="Enter a todo",placeholder="Enter a todo...",
              key="todo-input",label_visibility="hidden",)

st.session_state

