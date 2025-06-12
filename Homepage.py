import streamlit as st
import base64
import os

# ===== Function to encode background image =====
def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ===== Load background once =====
bg_image = get_base64_image("images/team_section_bg.png")

# ===== PAGE CONFIG =====
st.set_page_config(
    page_title="Education Career App",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===== GOOGLE FONT + STYLES =====
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Bungee&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

st.markdown(f"""
    <style>
        html, body {{
            margin: 0;
            padding: 0;
            background: url("data:image/png;base64,{bg_image}") no-repeat center center fixed;
            background-size: cover;
        }}

        .title-section {{
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
        }}

        .title-section h1 {{
            font-family: 'Bungee', cursive;
            font-size: 70px;
            color: #cf5a2e;
            margin-bottom: 50px;
            line-height: 1.2;
            text-shadow: 2px 2px 8px #ffffff70;
        }}

        .title-section button {{
            background: linear-gradient(to right, #f6d365, #fda085);
            color: black;
            padding: 12px 30px;
            font-size: 18px;
            border: none;
            border-radius: 20px;
            cursor: pointer;
        }}

        .team-title {{
            text-align: center;
            font-size: 42px;
            font-family: 'Bungee', sans-serif;
            color: black;
            margin-bottom: 3rem;
            margin-top: 5rem;
        }}

        .member-name {{
            text-align: center;
            font-weight: bold;
            color: black;
            margin-top: 10px;
            font-size: 16px;
        }}

        .row-spacing {{
            margin-top: 40px;
        }}
    </style>
""", unsafe_allow_html=True)

# ===== HOMEPAGE SECTION =====
st.markdown("""
    <div class="title-section">
        <h1>EDUCATION<br>CAREER<br>SUCCESS</h1>
        <a href="#team"><button>Read the report</button></a>
    </div>
""", unsafe_allow_html=True)

# ===== OUR TEAM SECTION =====
st.markdown('<a name="team"></a>', unsafe_allow_html=True)
st.markdown('<div class="team-title">OUR TEAM</div>', unsafe_allow_html=True)

# ===== TEAM MEMBERS DATA =====
team_members = [
    {"name": "Nguyễn Kiều Anh", "image": "images/Nguyễn Kiều Anh.png"},
    {"name": "Lê Nguyễn Khánh Phương", "image": "images/Lê Nguyễn Khánh Phương.png"},
    {"name": "Nguyễn Bảo Ngọc", "image": "images/Nguyễn Bảo Ngọc.png"},
    {"name": "Nguyễn Trần Khánh Linh", "image": "images/Nguyễn Trần Khánh Linh.png"},
    {"name": "Nguyễn Huỳnh Bảo Nguyên", "image": "images/Nguyễn Huỳnh Bảo Nguyên.png"},
    {"name": "Vũ Thị Thu Thảo", "image": "images/Vũ Thị Thu Thảo.png"},
    {"name": "Nguyễn Bội Ngọc", "image": "images/Nguyễn Bội Ngọc.png"},
]

# ===== DISPLAY IMAGES + NAMES =====
top_row = team_members[:4]
bottom_row = team_members[4:]

for row in [top_row, bottom_row]:
    cols = st.columns(len(row))
    for col, member in zip(cols, row):
        with col:
            st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
            st.image(member["image"], width=180)
            st.markdown(f"<div class='member-name'>{member['name']}</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
    if row == top_row:
        st.markdown("<div class='row-spacing'></div>", unsafe_allow_html=True)
