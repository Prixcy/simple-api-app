import requests
import streamlit as st
from datetime import datetime
import json

BACKEND_URL = "http://backend:8000"

def make_request(method, endpoint, data=None):
    """Helper function to make API requests"""
    try:
        if method == "GET":
            response = requests.get(f"{BACKEND_URL}{endpoint}")
        elif method == "POST":
            response = requests.post(f"{BACKEND_URL}{endpoint}", json=data)
        elif method == "PUT":
            response = requests.put(f"{BACKEND_URL}{endpoint}", json=data)
        elif method == "DELETE":
            response = requests.delete(f"{BACKEND_URL}{endpoint}")
        
        if response.status_code >= 400:
            st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
            return None
        return response.json()
    except Exception as e:
        st.error(f"Connection error: {str(e)}")
        return None
