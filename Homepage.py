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

# ==== CUSTOM STYLES ====
st.markdown("""
    <style>
        .stApp {
            background-image: url('images/homepage_bg.png');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }

        .centered {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            text-align: center;
            color: #faf4dc;
        }
        .centered h1 {
            font-size: 70px;
            font-family: 'Bungee', sans-serif;
            margin-bottom: 50px;
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

        #team-section {
            background-image: url('images/team_section_bg.png');
            background-size: cover;
            background-position: center;
            padding: 4rem 2rem;
        }

        .team-title {
            text-align: center;
            font-size: 42px;
            font-family: 'Bungee', sans-serif;
            color: black;
            margin: 2rem 0 3rem 0;
        }

        .spacer {
            height: 50px;
        }

        .name-text {
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            color: black;
            margin-top: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# ==== HOMEPAGE CONTENT ====
st.markdown("""
    <div class="centered">
        <h1>EDUCATION CAREER SUCCESS</h1>
        <a href="#team"><button>Let's get started</button></a>
    </div>
""", unsafe_allow_html=True)

# ==== OUR TEAM SECTION ====
st.markdown('<a name="team"></a>', unsafe_allow_html=True)
st.markdown('<div id="team-section">', unsafe_allow_html=True)
st.markdown("""<div class="team-title">Our Team ⭐</div>""", unsafe_allow_html=True)

# ==== TEAM MEMBERS ====
team_members = [
    {"name": "Nguyễn Kiều Anh", "image": "images/Nguyen Kieu Anh.png"},
    {"name": "Lê Nguyễn Khánh Phương", "image": "images/Le Nguyen Khanh Phuong.png"},
    {"name": "Nguyễn Bảo Ngọc", "image": "images/Nguyen Bao Ngoc.png"},
    {"name": "Nguyễn Trần Khánh Linh", "image": "images/Nguyen Tran Khanh Linh.png"},
    {"name": "Nguyễn Huỳnh Bảo Nguyên", "image": "images/Nguyen Huynh Bao Nguyen.png"},
    {"name": "Vũ Thị Thu Thảo", "image": "images/Vu Thi Thu Thao.png"},
    {"name": "Nguyễn Bội Ngọc", "image": "images/Nguyen Boi Ngoc.png"},
]

# ==== DISPLAY MEMBERS IN 2 ROWS ====
top_row = team_members[:4]
bottom_row = team_members[4:]

for row in [top_row, bottom_row]:
    cols = st.columns(len(row))
    for col, member in zip(cols, row):
        with col:
            st.image(member["image"], width=180)
            st.markdown(f"<div class='name-text'>{member['name']}</div><div style='text-align: center'>", unsafe_allow_html=True)
    if row == top_row:
        st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

# ==== END SECTION ====
st.markdown("</div>", unsafe_allow_html=True)
