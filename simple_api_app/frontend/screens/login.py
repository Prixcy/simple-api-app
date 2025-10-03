import requests
import streamlit as st
from datetime import datetime
import json
from utils import make_request


def login_page():
    """Login page"""
    st.title("🔐 Login")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("### Welcome back!")
        
        with st.form("login_form"):
            email = st.text_input("Email", placeholder="Enter your email")
            password = st.text_input("Password", type="password", placeholder="Enter your password")
            submit = st.form_submit_button("Login", use_container_width=True)
            
            if submit:
                if email and password:
                    result = make_request("POST", "/auth/login", {"email": email, "password": password})
                    if result:
                        st.session_state.user_id = result["user_id"]
                        st.session_state.user_email = result["email"]
                        st.session_state.page = "todos"
                        st.rerun()
                else:
                    st.error("Please fill in all fields")
        
        st.markdown("---")
        st.markdown("Don't have an account?")
        if st.button("Register", use_container_width=True):
            st.session_state.page = "register"
            st.rerun()
