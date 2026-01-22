import streamlit as st
import functions
import os

if not os.path.exists("todos.txt") :
    with open("todos.txt","w") as file:
        pass

all_todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state['todo-input']+ '\n'
    all_todos.append(new_todo)
    functions.write_todos(all_todos)
    st.session_state['todo-input'] = ""

st.title("My Todo Web App")
st.subheader("This todo app was developed by Nikhil-R")
st.write("This is a minimal todo app to organise your day")

for index,todo in enumerate(all_todos):
    checked = st.checkbox(todo,key=todo)
    if checked:
        all_todos.pop(index)
        functions.write_todos(all_todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="Enter a todo",placeholder="Enter a todo...",
              key="todo-input",label_visibility="hidden", on_change=add_todo )


