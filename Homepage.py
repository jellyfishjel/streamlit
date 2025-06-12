import streamlit as st
import base64
import os

# ==== Function to encode background image ====
def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ==== Get single background image ====
bg_image = get_base64_image("images/team_section_bg.png")

# ==== Page Config ====
st.set_page_config(
    page_title="Education Career App",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==== Import font ====
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Bungee&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# ==== Global CSS with unified background ====
st.markdown(f"""
    <style>
        html, body, .stApp {{
            background: url("data:image/png;base64,{bg_image}") no-repeat center center fixed;
            background-size: cover;
        }}

        .homepage {{
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 100px 20px 80px;
        }}

        .homepage h1 {{
            font-family: 'Bungee', sans-serif;
            font-size: 64px;
            color: #cf5a2e;  /* Updated color */
            line-height: 1.2;
            margin-bottom: 40px;
        }}

        .homepage button {{
            background: linear-gradient(to right, #f6d365, #fda085);
            color: black;
            padding: 12px 30px;
            font-size: 16px;
            border: none;
            border-radius: 20px;
            cursor: pointer;
        }}

        .team-title {{
            text-align: center;
            font-size: 36px;
            font-family: 'Bungee', sans-serif;
            color: black;
            margin-bottom: 3rem;
            margin-top: 3rem;
        }}

        .member-name {{
            text-align: center;
            font-weight: bold;
            color: black;
            margin-top: 8px;
            font-size: 16px;
        }}

        .row-spacing {{
            margin-top: 40px;
        }}
    </style>
""", unsafe_allow_html=True)

# ==== HOMEPAGE section ====
st.markdown(f"""
    <div class="homepage">
        <h1>EDUCATION<br>CAREER<br>SUCCESS</h1>
        <a href="#team"><button>Read the report</button></a>
    </div>
""", unsafe_allow_html=True)

# ==== OUR TEAM section ====
st.markdown('<a name="team"></a>', unsafe_allow_html=True)
st.markdown('<div class="team-title">OUR TEAM</div>', unsafe_allow_html=True)

team_members = [
    {"name": "Nguyễn Kiều Anh", "image": "images/Nguyen Kieu Anh.png"},
    {"name": "Lê Nguyễn Khánh Phương", "image": "images/Le Nguyen Khanh Phuong.png"},
    {"name": "Nguyễn Bảo Ngọc", "image": "images/Nguyen Bao Ngoc.png"},
    {"name": "Nguyễn Trần Khánh Linh", "image": "images/Nguyen Tran Khanh Linh.png"},
    {"name": "Nguyễn Huỳnh Bảo Nguyên", "image": "images/Nguyen Huynh Bao Nguyen.png"},
    {"name": "Vũ Thị Thu Thảo", "image": "images/Vu Thi Thu Thao.png"},
    {"name": "Nguyễn Bội Ngọc", "image": "images/Nguyen Boi Ngoc.png"},
]

# === Split into 2 rows ===
top_row = team_members[:4]
bottom_row = team_members[4:]

for row in [top_row, bottom_row]:
    cols = st.columns(len(row))
    for col, member in zip(cols, row):
        with col:
            st.image(member["image"], width=180)
            st.markdown(f"<div class='member-name'>{member['name']}</div>", unsafe_allow_html=True)

    if row == top_row:
        st.markdown("<div class='row-spacing'></div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
