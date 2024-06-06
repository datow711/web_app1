import streamlit as st
import functions as fc

todos = fc.get_todos()

def add_todo():
    todo_toadd = st.session_state["new_todo"]+'\n'
    todos.append(todo_toadd)
    fc.writetodo(todos)

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This is my first app project of this course")

for index, todo in enumerate(todos):
    item = todo.strip('\n')
    checkbox = st.checkbox(item,key=todo)
    if checkbox:
        todos.pop(index)
        fc.writetodo(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter todo", placeholder="Add a new todo.", 
              on_change=add_todo, key="new_todo")

st.session_state