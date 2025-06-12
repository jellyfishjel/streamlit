import streamlit as st

# Cấu hình trang
st.set_page_config(page_title="Education Career App", layout="wide")

# Nhúng font Bungee + CSS
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Bungee&display=swap" rel="stylesheet">
    <style>
        .title-section {
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 0 20px;
        }

        .title-section h1 {
            font-family: 'Bungee', cursive;
            font-size: 70px;
            color: #cf5a2e;
            margin-bottom: 50px;
            line-height: 1.2;
        }

        .title-section a > button {
            background: linear-gradient(to right, #f6d365, #fda085);
            color: black;
            padding: 12px 30px;
            font-size: 18px;
            border: none;
            border-radius: 20px;
            cursor: pointer;
        }

        .title-section a > button:hover {
            opacity: 0.9;
        }
    </style>

    <div class="title-section">
        <h1>EDUCATION<br>CAREER<br>SUCCESS</h1>
        <a href="/1_Dataset_Overview"><button>Read the report</button></a>
    </div>
""", unsafe_allow_html=True)
