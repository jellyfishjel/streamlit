import streamlit as st
from PIL import Image
import os

# ===== PAGE CONFIG =====
st.set_page_config(
    page_title="Education Career App",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===== LOAD CUSTOM FONT =====
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Bungee&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# ===== STYLING (Homepage background + Title) =====
st.markdown(
    f"""
    <style>
        .homepage {{
            background-image: url('images/homepage_bg.png');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
        }}
        .homepage h1 {{
            font-family: 'Bungee', sans-serif;
            font-size: 72px;
            color: #faf4dc;
            margin-bottom: 40px;
        }}
        .homepage button {{
            background-color: white;
            color: black;
            padding: 14px 30px;
            font-size: 18px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
        }}
        .homepage button:hover {{
            background-color: #ddd;
        }}
    </style>

    <div class="homepage">
        <h1>EDUCATION<br>CAREER<br>SUCCESS</h1>
        <a href="#team-section"><button>Let's get started</button></a>
    </div>
    """,
    unsafe_allow_html=True
)

# ===== TEAM SECTION BACKGROUND STYLE =====
st.markdown(
    f"""
    <style>
        .team-section {{
            background-image: url('images/team_section_bg.png');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            padding: 80px 30px;
        }}
        .team-title {{
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: white;
            margin-bottom: 40px;
        }}
        .member-name {{
            text-align: center;
            font-weight: bold;
            color: white;
            margin-top: 10px;
            font-size: 18px;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# ===== TEAM SECTION CONTENT =====
st.markdown('<div class="team-section" id="team-section">', unsafe_allow_html=True)
st.markdown('<div class="team-title">Our Team ⭐</div>', unsafe_allow_html=True)

# === TEAM IMAGES ===
team_folder = "images/team"
team_members = [
    {"name": "Nguyễn Kiều Anh", "file": "Nguyễn Kiều Anh.png"},
    {"name": "Lê Nguyễn Khánh Phương", "file": "Lê Nguyễn Khánh Phương.png"},
    {"name": "Nguyễn Bảo Ngọc", "file": "Nguyễn Bảo Ngọc.png"},
    {"name": "Nguyễn Trần Khánh Linh", "file": "Nguyễn Trần Khánh Linh.png"},
    {"name": "Nguyễn Huỳnh Bảo Nguyên", "file": "Nguyễn Huỳnh Bảo Nguyên.png"},
    {"name": "Vũ Thị Thu Thảo", "file": "Vũ Thị Thu Thảo.png"},
    {"name": "Bội Ngọc", "file": "Sazahng.png"}
]

# Chia thành 2 hàng
top_row = team_members[:4]
bottom_row = team_members[4:]

for row in [top_row, bottom_row]:
    cols = st.columns(len(row))
    for col, member in zip(cols, row):
        with col:
            img_path = os.path.join(team_folder, member["file"])
            st.image(img_path, width=160)
            st.markdown(f"<div class='member-name'>{member['name']}</div>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
