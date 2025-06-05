import streamlit as st
from PIL import Image

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
            padding: 4rem 2rem;
        }
    </style>
    <div id="team-section">
    """,
    unsafe_allow_html=True
)

# ===== SCROLL ANCHOR =====
st.markdown('<a name="team"></a>', unsafe_allow_html=True)

# ===== TITLE "OUR TEAM" =====
st.markdown("""
    <div style="
        text-align: center;
        font-size: 42px;
        font-family: 'Bungee', sans-serif;
        color: #faf4dc;
        margin: 2rem 0 3rem 0;">
        OUR TEAM 
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
    {"name": "Bội Ngọc", "image": "images/Nguyen Boi Ngoc.png"},
]

# Hiển thị: 4 thành viên hàng đầu, 3 ở dưới
top_row = team_members[:4]
bottom_row = team_members[4:]

for row in [top_row, bottom_row]:
    cols = st.columns(len(row))
    for col, member in zip(cols, row):
        with col:
            st.image(member["image"], width=160)
            st.markdown(
                f"<p style='text-align: center; color: #faf4dc; font-size: 18px;'><strong>{member['name']}</strong></p>",
                unsafe_allow_html=True
            )

# ===== ĐÓNG DIV CỦA TEAM SECTION =====
st.markdown("</div>", unsafe_allow_html=True)
