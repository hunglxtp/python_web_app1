import streamlit as st
import functions

todos = functions.get_todos('./files/todos.txt')

def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo+'\n')
    functions.write_todos(todos, './files/todos.txt')

def remove_todo():
    pass


st.title("My Todo App")
st.subheader("This is my todo App")
st.write("This app is to increase your productivity !")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos, './files/todos.txt')
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo : ",
              placeholder="Enter a todo...",
              on_change=add_todo,
              key='new_todo')
