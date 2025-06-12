import streamlit as st
import base64

# ==== Page config ====
st.set_page_config(
    page_title="Education Career App",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==== Encode background image ====
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

bg_image = get_base64_image("images/team_section_bg.png")

# ==== Google Font and CSS ====
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Bungee&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

st.markdown(f"""
    <style>
        body {{
            margin: 0;
            padding: 0;
        }}
        .stApp {{
            background-image: url("data:image/png;base64,{bg_image}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        .homepage {{
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
        }}
        .homepage h1 {{
            font-family: 'Bungee', sans-serif;
            font-size: 64px;
            color: #cf5a2e;
            margin-bottom: 40px;
        }}
        .homepage a > button {{
            background: linear-gradient(to right, #f6d365, #fda085);
            color: black;
            padding: 12px 30px;
            font-size: 18px;
            border: none;
            border-radius: 25px;
            cursor: pointer;
        }}
        .homepage a > button:hover {{
            opacity: 0.9;
        }}
    </style>
""", unsafe_allow_html=True)

# ==== Homepage content ====
st.markdown("""
    <div class="homepage">
        <h1>EDUCATION<br>CAREER<br>SUCCESS</h1>
        <a href="/Dataset_overview">
            <button>Read the report</button>
        </a>
    </div>
""", unsafe_allow_html=True)
