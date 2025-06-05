import streamlit as st
from PIL import Image
import os

# ==== PAGE CONFIG ====
st.set_page_config(
    page_title="Education Career App",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==== IMPORT GOOGLE FONT BUNGEE ====
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Bungee&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# ==== HOMEPAGE STYLE ====
st.markdown(
    """
    <style>
        body {
            margin: 0;
        }
        .homepage {
            background-image: url('images/homepage_bg.png');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }
        .homepage h1 {
            font-family: 'Bungee', sans-serif;
            font-size: 70px;
            color: #faf4dc;
            margin-bottom: 30px;
        }
        .homepage button {
            background-color: white;
            color: black;
            padding: 12px 30px;
            font-size: 18px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .homepage button:hover {
            background-color: #ddd;
        }
    </style>
    <div class="homepage">
        <h1>EDUCATION CAREER SUCCESS</h1>
        <a href="#team"><button>Let's get started</button></a>
    </div>
    """,
    unsafe_allow_html=True
)

# ==== OUR TEAM SECTION STYLE ====
st.markdown(
    """
    <style>
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
            margin-bottom: 3rem;
        }
        .member-name {
            text-align: center;
            color: black;
            font-size: 18px;
            margin-top: 12px;
        }
        .spacer {
            margin-top: 4rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ==== ANCHOR & SECTION ====
st.markdown('<a name="team"></a>', unsafe_allow_html=True)
st.markdown('<div id="team-section">', unsafe_allow_html=True)
st.markdown('<div class="team-title">Our Team ⭐</div>', unsafe_allow_html=True)

# ==== TEAM MEMBERS ====
team_members = [
    {"name": "Nguyễn Kiều Anh", "image": "images/Nguyen Kieu Anh.png"},
    {"name": "Lê Nguyễn Khánh Phương", "image": "images/Le Nguyen Khanh Phuong.png"},
    {"name": "Nguyễn Bảo Ngọc", "image": "images/Nguyen Bao Ngoc.png"},
    {"name": "Nguyễn Trần Khánh Linh", "image": "images/Nguyen Tran Khanh Linh.png"},
    {"name": "Nguyễn Huỳnh Bảo Nguyên", "image": "images/Nguyen Huynh Bao Nguyen.png"},
    {"name": "Vũ Thị Thu Thảo", "image": "images/Vu Thi Thu Thao.png"},
    {"name": "Bội Ngọc", "image": "images/Nguyen Boi Ngoc.png"},
]

# Hiển thị 4 người hàng đầu, 3 người hàng dưới
top_row = team_members[:4]
bottom_row = team_members[4:]

for row in [top_row, bottom_row]:
    cols = st.columns(len(row))
    for col, member in zip(cols, row):
        with col:
            st.image(member["image"], width=180)
            st.markdown(f"<div class='member-name'><strong>{member['name']}</strong></div>", unsafe_allow_html=True)
    if row == top_row:
        st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

# Đóng section
st.markdown('</div>', unsafe_allow_html=True)
