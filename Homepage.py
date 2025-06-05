import streamlit as st
import os

# ===== PAGE CONFIG =====
st.set_page_config(
    page_title="Education Career App",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===== IMPORT GOOGLE FONT =====
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Bungee&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# ===== HOMEPAGE BACKGROUND + TITLE =====
st.markdown(
    """
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
    </style>
    <div class="centered">
        <h1>EDUCATION CAREER SUCCESS</h1>
        <a href="#team"><button>Let's get started</button></a>
    </div>
    """,
    unsafe_allow_html=True
)

# ===== OUR TEAM SECTION BACKGROUND =====
st.markdown(
    """
    <style>
        #team-section {
            background-image: url('images/team_section_bg.png');
            background-size: cover;
            background-position: center;
            padding: 5rem 2rem;
        }
    </style>
    <div id="team-section">
    """,
    unsafe_allow_html=True
)

# ===== ANCHOR FOR SCROLL =====
st.markdown('<a name="team"></a>', unsafe_allow_html=True)

# ===== TEAM TITLE =====
st.markdown("""
    <div style="
        text-align: center;
        font-size: 42px;
        font-family: 'Bungee', sans-serif;
        color: black;
        margin: 2rem 0 3rem 0;">
        OUR TEAM ⭐
    </div>
""", unsafe_allow_html=True)

# ===== TEAM MEMBERS =====
team_members = [
    {"name": "Nguyễn Kiều Anh", "image": "images/Nguyen Kieu Anh.png"},
    {"name": "Lê Nguyễn Khánh Phương", "image": "images/Le Nguyen Khanh Phuong.png"},
    {"name": "Nguyễn Bảo Ngọc", "image": "images/Nguyen Bao Ngoc.png"},
    {"name": "Nguyễn Trần Khánh Linh", "image": "images/Nguyen Tran Khanh Linh.png"},
    {"name": "Nguyễn Huỳnh Bảo Nguyên", "image": "images/Nguyen Huynh Bao Nguyen.png"},
    {"name": "Vũ Thị Thu Thảo", "image": "images/Vu Thi Thu Thao.png"},
    {"name": "Nguyễn Bội Ngọc", "image": "images/Nguyen Boi Ngoc.png"},
]

# Tách hàng
top_row = team_members[:4]
bottom_row = team_members[4:]

# Hiển thị hàng đầu
cols_top = st.columns(len(top_row))
for col, member in zip(cols_top, top_row):
    with col:
        st.image(member["image"], width=160)
        st.markdown(
            f"<p style='text-align: center; color: black; font-size: 18px; margin-top: 8px;'><strong>{member['name']}</strong></p>",
            unsafe_allow_html=True
        )

# Tạo khoảng cách giữa 2 hàng
st.markdown("<div style='height: 3rem;'></div>", unsafe_allow_html=True)

# Hiển thị hàng dưới
cols_bottom = st.columns(len(bottom_row))
for col, member in zip(cols_bottom, bottom_row):
    with col:
        st.image(member["image"], width=160)
        st.markdown(
            f"<p style='text-align: center; color: black; font-size: 18px; margin-top: 8px;'><strong>{member['name']}</strong></p>",
            unsafe_allow_html=True
        )

# Đóng section
st.markdown("</div>", unsafe_allow_html=True)
