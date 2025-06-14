import streamlit as st
from PIL import Image

# ==== Page Config ====
st.set_page_config(page_title="Education Career App", layout="wide")

# ==== Load CSS ====
def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style/style.css")  # Optional, nếu bạn có file riêng

# ==== Import Google Fonts ====
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Bungee&family=Quicksand:wght@400;600&display=swap" rel="stylesheet">
<style>
    body, p, li {
        font-family: 'Quicksand', sans-serif !important;
        color: #333;
    }

    .homepage {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        padding: 80px 20px 40px;
    }

    .homepage h1 {
        font-family: 'Bungee', sans-serif;
        font-size: 64px;
        color: #cf5a2e;
        line-height: 1.2;
        margin-bottom: 10px;
    }

    .team-title {
        text-align: center;
        font-size: 36px;
        font-family: 'Bungee', sans-serif;
        color: black;
        margin: 3rem 0 2rem;
    }

    .member-img {
        border-radius: 50%;
        width: 230px;
        height: 230px;
        object-fit: cover;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }

    .member-img:hover {
        transform: scale(1.05);
    }

    .explore-btn {
        display: inline-block;
        background-color: #cf5a2e;
        color: white;
        padding: 12px 28px;
        border-radius: 30px;
        font-weight: bold;
        text-decoration: none;
        font-size: 16px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }

    .explore-btn:hover {
        transform: scale(1.05);
        background-color: #b94924;
    }
</style>
""", unsafe_allow_html=True)

# ==== Title ====
st.markdown("""
<div class="homepage">
    <h1>EDUCATION<br>CAREER<br>SUCCESS</h1>
</div>
""", unsafe_allow_html=True)

# ==== Intro Box ====
st.markdown("""
<div style="padding: 2rem 2rem 3rem; background: linear-gradient(135deg, #ffe9d6, #fbe3e3); border-radius: 20px; box-shadow: 0 8px 16px rgba(0,0,0,0.1); text-align: center;">

<h2 style="font-family:'Bungee', sans-serif; font-size: 36px; color: #cf5a2e; margin-bottom: 1rem;">
🎓 How does education shape your future? <br>📊 Let the data tell the story!
</h2>

<p style="font-size: 18px; max-width: 850px; margin: 0 auto;">
<strong>Education Career App</strong> helps you explore the connection between <strong>education</strong> and <strong>career success</strong>. With interactive visualizations, you'll be able to:
</p>

<ul style="text-align: left; max-width: 600px; margin: 2rem auto; font-size: 17px;">
    <li>🔍 Understand key factors that influence your career path</li>
    <li>📚 Compare trends across different education levels</li>
    <li>🚀 Make smarter, data-driven career decisions</li>
</ul>

<p style="font-size: 17px;">
This app is a student project by <strong>Team</strong> for the <em>Business IT2</em> course at <strong>Vietnamese–German University (VGU)</strong>.
</p>

<a href="?page=1_charts" class="explore-btn">🚀 Explore Now</a>

</div>
""", unsafe_allow_html=True)

# ==== OUR TEAM Section ====
st.markdown('<div class="team-title">OUR TEAM</div>', unsafe_allow_html=True)

team_members = [
    {"name": "Nguyễn Kiều Anh", "image": "image/Nguyen Kieu Anh.png"},
    {"name": "Lê Nguyễn Khánh Phương", "image": "image/Le Nguyen Khanh Phuong.png"},
    {"name": "Nguyễn Bảo Ngọc", "image": "image/Nguyen Bao Ngoc.png"},
    {"name": "Nguyễn Trần Khánh Linh", "image": "image/Nguyen Tran Khanh Linh.png"},
    {"name": "Nguyễn Huỳnh Bảo Nguyên", "image": "image/Nguyen Huynh Bao Nguyen.png"},
    {"name": "Vũ Thị Thu Thảo", "image": "image/Vu Thi Thu Thao.png"},
    {"name": "Nguyễn Bội Ngọc", "image": "image/Nguyen Boi Ngoc.png"},
]

# === Display Members in Grid ===
cols = st.columns(4)
for idx, member in enumerate(team_members):
    with cols[idx % 4]:
        st.markdown(f"<img src='{member['image']}' class='member-img'>", unsafe_allow_html=True)
        st.markdown(f"<div style='text-align:center; font-weight:bold; font-size:15px;'>{member['name']}</div>", unsafe_allow_html=True)
    if (idx + 1) % 4 == 0:
        cols = st.columns(4)
