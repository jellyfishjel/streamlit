import streamlit as st

# ===== PAGE CONFIG =====
st.set_page_config(page_title="Education Career App", layout="wide")

# ===== GOOGLE FONT & CSS STYLE =====
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Bungee&display=swap" rel="stylesheet">
    <style>
        html, body {
            margin: 0;
            padding: 0;
        }

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
            text-shadow: 2px 2px 8px #ffffff80;
        }

        .title-section a > button {
            background: linear-gradient(to right, #f6d365, #fda085);
            color: black;
            padding: 12px 30px;
            font-size: 18px;
            border: none;
            border-radius: 20px;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .title-section a > button:hover {
            opacity: 0.9;
        }
    </style>
""", unsafe_allow_html=True)

# ===== HOMEPAGE CONTENT =====
st.markdown("""
    <div class="title-section">
        <h1>EDUCATION<br>CAREER<br>SUCCESS</h1>
        <a href="/Dataset_overview"><button>Read the report</button></a>
    </div>
""", unsafe_allow_html=True)
