import requests
import streamlit as st
from datetime import datetime
import json
from screens.login import login_page
from screens.signup import register_page
from screens.todo import todos_page

# BACKEND_URL = st.secrets.get("BACKEND_URL", "http://localhost:8000")
BACKEND_URL = "http://backend:8000"

st.set_page_config(page_title="Todo App", page_icon="✅", layout="wide")

# Initialize session state
if "user_id" not in st.session_state:
    st.session_state.user_id = None
if "user_email" not in st.session_state:
    st.session_state.user_email = None
if "page" not in st.session_state:
    st.session_state.page = "login"

# Main app logic
def main():
    if st.session_state.page == "login":
        login_page()
    elif st.session_state.page == "register":
        register_page()
    elif st.session_state.page == "todos":
        if st.session_state.user_id:
            todos_page()
        else:
            st.session_state.page = "login"
            st.rerun()
    else:
        st.session_state.page = "login"
        st.rerun()

if __name__ == "__main__":
    main()

