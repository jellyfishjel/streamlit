import streamlit as st

# Cấu hình trang
st.set_page_config(page_title="Education Career App", layout="wide")

# Nhúng font 'Bungee' và CSS tùy chỉnh
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Bungee&display=swap" rel="stylesheet">
    <style>
        .centered {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-image: url('images/homepage_bg.png');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        .centered h1 {
            font-family: 'Bungee', cursive;
            font-size: 70px;
            color: #faf4dc;
            text-align: center;
            margin-bottom: 50px;
            text-shadow: 2px 2px #00000040;
        }
        .centered button {
            background-color: white;
            color: black;
            padding: 12px 30px;
            font-size: 18px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .centered button:hover {
            background-color: #ddd;
        }
    </style>
    <div class="centered">
        <h1>EDUCATION<br>CAREER<br>SUCCESS</h1>
        <a href="1_👥_Learn_about_us"><button>Let's get started</button></a>
    </div>
""", unsafe_allow_html=True)
