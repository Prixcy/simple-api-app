import requests
import streamlit as st
from datetime import datetime
import json
from utils import make_request


def todos_page():
    """Todo management page"""
    st.title("Todos")
    
    # Header with user info and logout
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"**Welcome, {st.session_state.user_email}**")
    with col2:
        if st.button("Logout", type="secondary"):
            st.session_state.user_id = None
            st.session_state.user_email = None  
            st.session_state.page = "login"
            st.rerun()
    
    st.markdown("---")
    
    # Add new todo
    with st.expander("➕ Add New Todo", expanded=True):
        with st.form("add_todo_form"):
            col1, col2 = st.columns([3, 1])
            with col1:
                content = st.text_input("Todo content", placeholder="What needs to be done?")
            with col2:
                reminding_time = st.text_input("Reminder time", placeholder="e.g., 2024-01-01 10:00")
            
            if st.form_submit_button("Add Todo", use_container_width=True):
                if content:
                    result = make_request("POST", "/todos", {
                        "user_id": st.session_state.user_id,
                        "content": content,
                        "reminding_time": reminding_time if reminding_time else None
                    })
                    if result:
                        st.success("Todo added successfully!")
                        st.rerun()
                else:
                    st.error("Please enter todo content")
    
    # Display todos
    st.markdown("### Your Todos")
    
    # Fetch todos
    todos = make_request("GET", f"/todos/{st.session_state.user_id}")
    
    if todos:
        for todo in todos:
            with st.container():
                col1, col2, col3 = st.columns([1, 6, 1])
                
                with col1:
                    # Checkbox for completion (visual only for now)
                    completed = st.checkbox("", key=f"check_{todo['todo_id']}")
                
                with col2:
                    content_strip = todo['content'].strip()
                    st.markdown(f"**{content_strip}**")
                    if todo['reminding_time']:
                        st.caption(f"⏰ Reminder: {todo['reminding_time']}")
                
                with col3:
                    # Edit and delete buttons
                    col_edit, col_delete = st.columns(2)
                    
                    with col_edit:
                        if st.button("✏️", key=f"edit_{todo['todo_id']}", help="Edit"):
                            st.session_state[f"editing_{todo['todo_id']}"] = True
                            st.rerun()
                    
                    with col_delete:
                        if st.button("🗑️", key=f"delete_{todo['todo_id']}", help="Delete"):
                            result = make_request("DELETE", f"/todos/{todo['todo_id']}")
                            if result:
                                st.success("Todo deleted!")
                                st.rerun()
                
                # Edit form
                if st.session_state.get(f"editing_{todo['todo_id']}", False):
                    with st.form(f"edit_form_{todo['todo_id']}"):
                        new_content = st.text_input("Edit content", value=todo['content'], key=f"new_content_{todo['todo_id']}")
                        new_reminder = st.text_input("Edit reminder", value=todo['reminding_time'] or "", key=f"new_reminder_{todo['todo_id']}")
                        
                        col_save, col_cancel = st.columns(2)
                        with col_save:
                            if st.form_submit_button("Save", use_container_width=True):
                                result = make_request("PUT", f"/todos/{todo['todo_id']}", {
                                    "content": new_content,
                                    "reminding_time": new_reminder if new_reminder else None
                                })
                                if result:
                                    st.session_state[f"editing_{todo['todo_id']}"] = False
                                    st.success("Todo updated!")
                                    st.rerun()
                        
                        with col_cancel:
                            if st.form_submit_button("Cancel", use_container_width=True):
                                st.session_state[f"editing_{todo['todo_id']}"] = False
                                st.rerun()
                
                st.markdown("---")
    else:
        st.info("No todos yet. Add one above to get started!")
