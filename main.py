# main.py
import streamlit as st
import os
import importlib.util

st.title("🌐 Multi-App Streamlit Dashboard")
app_option = st.sidebar.selectbox("Chọn ứng dụng", ["App 1", "App 2", "App 3"])

app_paths = {
    "App 1": "pages/homepage.py",
    "App 2": "pages/graphtab.py",
    "App 3": "pages/overview.py"
}

def run_app(path):
    spec = importlib.util.spec_from_file_location("app", path)
    app = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(app)

run_app(app_paths[app_option])
