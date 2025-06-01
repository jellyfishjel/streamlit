# main.py
import streamlit as st
import os
import importlib.util

st.title("🌐 Multi-App Streamlit Dashboard")
app_option = st.sidebar.selectbox("Chọn ứng dụng", ["App 1", "App 2", "App 3"])

app_paths = {
    "App 1": "app1/app.py",
    "App 2": "app2/app.py",
    "App 3": "app3/app.py"
}

def run_app(path):
    spec = importlib.util.spec_from_file_location("app", path)
    app = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(app)

run_app(app_paths[app_option])
