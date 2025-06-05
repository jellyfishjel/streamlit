import streamlit as st
import os

# ==== PAGE CONFIG ====
st.set_page_config(
    page_title="Education Career App",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==== IMPORT GOOGLE FONT ====
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Bungee&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# ==== HOMEPAGE SECTION (with background) ====
st.markdown("""
    <style>
        .stApp {
            background-image: url("images/homepage_bg.png");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        .homepage-container {
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
        }
        .homepage-title {
            font-family: 'Bungee', sans-serif;
            font-size: 70px;
            color: #faf4dc;
            margin-bottom: 40px;
        }
        .homepage-button {
            background-color: white;
            color: black;
            padding: 12px 30px;
            font-size: 18px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: 0.3s;
        }
        .homepage-button:hover {
            background-color: #ddd;
        }
    </style>
    <div class="homepage-container">
        <h1 class="homepage-title">EDUCATION CAREER SUCCESS</h1>
        <a href="#team"><button class="homepage-button">Let's get started</button></a>
    </div>
""", unsafe_allow_html=True)

# ==== OUR TEAM SECTION (anchor + custom bg) ====
st.markdown('<a name="team"></a>', unsafe_allow_html=True)
st.markdown(
    """
    <style>
        #team-section {
            background-image: url("images/team_section_bg.png");
            background-size: cover;
            background-position: center;
            padding: 4rem 2rem;
        }
        .team-title {
            text-align: center;
            font-family: 'Bungee', sans-serif;
            font-size: 42px;
            color: #faf4dc;
            margin-bottom: 3rem;
        }
        .member-name {
            text-align: center;
            font-size: 18px;
            color: #faf4dc;
        }
    </style>
    <div id="team-section">
        <div class="team-title">OUR TEAM ⭐</div>
    """,
    unsafe_allow_html=True
)

# ==== TEAM MEMBERS DISPLAY ====
team_members = [
    {"name": "Nguyễn Kiều Anh", "image": "images/Nguyen Kieu Anh.png"},
    {"name": "Lê Nguyễn Khánh Phương", "image": "images/Le Nguyen Khanh Phuong.png"},
    {"name": "Nguyễn Bảo Ngọc", "image": "images/Nguyen Bao Ngoc.png"},
    {"name": "Nguyễn Trần Khánh Linh", "image": "images/Nguyen Tran Khanh Linh.png"},
    {"name": "Nguyễn Huỳnh Bảo Nguyên", "image": "images/Nguyen Huynh Bao Nguyen.png"},
    {"name": "Vũ Thị Thu Thảo", "image": "images/Vu Thi Thu Thao.png"},
    {"name": "Bội Ngọc", "image": "images/Nguyen Boi Ngoc.png"},
]

top_row = team_members[:4]
bottom_row = team_members[4:]
img_folder = "images"

for row in [top_row, bottom_row]:
    cols = st.columns(len(row))
    for col, member in zip(cols, row):
        with col:
            path = os.path.join(img_folder, member["image"])
            st.image(path, width=160)
            st.markdown(f"<p class='member-name'><strong>{member['name']}</strong></p>", unsafe_allow_html=True)

# ==== Close team section ====
st.markdown("</div>", unsafe_allow_html=True)
