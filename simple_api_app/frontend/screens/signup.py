import requests
import streamlit as st
from datetime import datetime
import json
from utils import make_request

def register_page():
    """Registration page"""
    st.title("📝 Register")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("### Create your account")
        
        with st.form("register_form"):
            email = st.text_input("Email", placeholder="Enter your email")
            password = st.text_input("Password", type="password", placeholder="Enter your password")
            confirm_password = st.text_input("Confirm Password", type="password", placeholder="Confirm your password")
            submit = st.form_submit_button("Register", use_container_width=True)
            
            if submit:
                if email and password and confirm_password:
                    if password != confirm_password:
                        st.error("Passwords do not match")
                    else:
                        result = make_request("POST", "/users", {"email": email, "password": password})
                        if result:
                            st.success("Account created successfully! Please login.")
                            st.session_state.page = "login"
                            st.rerun()
                else:
                    st.error("Please fill in all fields")
        
        st.markdown("---")
        st.markdown("Already have an account?")
        if st.button("Login", use_container_width=True):
            st.session_state.page = "login"
            st.rerun()
