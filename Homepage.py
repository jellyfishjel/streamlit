import streamlit as st
from PIL import Image
import os

# ===== PAGE CONFIG =====
st.set_page_config(
    page_title="Education Career App",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===== BACKGROUND STYLE =====
st.markdown(
    f"""
    <style>
        .stApp {{
            background-image: url('images/homepage_bg.png');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        .centered {{
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            text-align: center;
            color: #1a1a1a;
        }}
        .centered h1 {{
            font-size: 70px;
            font-weight: 900;
            margin-bottom: 50px;
        }}
        .centered button {{
            background-color: white;
            color: black;
            padding: 12px 30px;
            font-size: 18px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: all 0.3s ease;
        }}
        .centered button:hover {{
            background-color: #ddd;
        }}
    </style>
    <div class="centered">
        <h1>EDUCATION CAREER SUCCESS</h1>
        <a href="#team"><button>Let's get started</button></a>
    </div>
    """,
    unsafe_allow_html=True
)

# ===== ABOUT US SECTION =====
st.markdown('<a name="team"></a>', unsafe_allow_html=True)
st.markdown("""<h2 style='text-align: center; margin-top: 3rem;'>Our Team ⭐</h2>""", unsafe_allow_html=True)

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

# Split into two rows
top_row = team_members[:4]
bottom_row = team_members[4:]

for row in [top_row, bottom_row]:
    cols = st.columns(len(row))
    for col, member in zip(cols, row):
        with col:
            img_path = os.path.join(team_folder, member["file"])
            st.image(img_path, width=160)
            st.markdown(f"<p style='text-align: center'><strong>{member['name']}</strong></p>", unsafe_allow_html=True)
