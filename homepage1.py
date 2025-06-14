import streamlit as st
from PIL import Image

# ==== Cấu hình trang ====
st.set_page_config(page_title="Education & Career App", layout="wide")

# ==== Load font: Bungee (cho heading), Poppins 500 (cho nội dung) ====
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Bungee&family=Poppins:wght@500&display=swap" rel="stylesheet">
<style>
    html, body, p, li, div {
        font-family: 'Poppins', sans-serif !important;
        font-size: 14px !important;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Bungee', cursive !important;
        font-weight: 400 !important;
    }

    /* Thu nhỏ padding toàn trang */
    [data-testid="stAppViewContainer"] {
        padding: 1rem 2rem;
    }

    /* Thu gọn padding sidebar */
    section[data-testid="stSidebar"] {
        padding: 1rem 1rem;
    }

    /* Thu nhỏ tiêu đề và card */
    .big-font {
        font-size: 20px !important;
    }
</style>
""", unsafe_allow_html=True)

# ==== Giao diện phần giới thiệu ====
st.markdown("""
<div style="padding: 2rem 2rem 2.5rem; background: linear-gradient(135deg, #fff2e6, #fce4ec); border-radius: 18px; box-shadow: 0 6px 12px rgba(0,0,0,0.08); text-align: center;">
    
    <h2 style="font-size: 30px; color: #cf5a2e; margin-bottom: 1rem;">
        🎯 How does education impact your career?<br>📈 Let data reveal the path!
    </h2>

    <p style="font-size: 15px; max-width: 800px; margin: 0 auto; color: #333;">
        <strong>Education Career App</strong> is an interactive dashboard that helps you uncover the link between <strong>education</strong>, <strong>job opportunities</strong>, and <strong>entrepreneurship</strong>.
    </p>

    <ul style="text-align: left; max-width: 550px; margin: 1.5rem auto 2rem; font-size: 14px;">
        <li>📊 Analyze job offer trends across gender, age, and education level</li>
        <li>🎓 Dive into field of study patterns and age distributions</li>
        <li>🚀 Explore entrepreneurship behavior among young professionals</li>
    </ul>

    <p style="font-size: 14px; color: #333;">
        Created by students of <strong>Business IT2</strong> from <em>Vietnamese–German University (VGU)</em>.
    </p>

    <a href="#chart" style="margin-top: 1.5rem; display: inline-block; background-color: #cf5a2e; color: white; padding: 10px 24px; border-radius: 25px; font-weight: bold; text-decoration: none; font-size: 14px;">
        🚀 Start Exploring
    </a>

</div>
""", unsafe_allow_html=True)

# ==== OUR TEAM Section ====
st.markdown('<div class="team-title">OUR TEAM</div>', unsafe_allow_html=True)

# ==== Danh sách thành viên ====
team_members = [
    {"name": "Nguyễn Kiều Anh", "image": "image/Nguyen Kieu Anh.png"},
    {"name": "Lê Nguyễn Khánh Phương", "image": "image/Le Nguyen Khanh Phuong.png"},
    {"name": "Nguyễn Bảo Ngọc", "image": "image/Nguyen Bao Ngoc.png"},
    {"name": "Nguyễn Trần Khánh Linh", "image": "image/Nguyen Tran Khanh Linh.png"},
    {"name": "Nguyễn Huỳnh Bảo Nguyên", "image": "image/Nguyen Huynh Bao Nguyen.png"},
    {"name": "Vũ Thị Thu Thảo", "image": "image/Vu Thi Thu Thao.png"},
    {"name": "Nguyễn Bội Ngọc", "image": "image/Nguyen Boi Ngoc.png"},
]

# ==== Top row ====
top_row = team_members[:4]
cols_top = st.columns(len(top_row))
for col, member in zip(cols_top, top_row):
    with col:
        st.image(member["image"], width=250)
        st.markdown( f"<div style='text-align:center; font-weight:bold; font-size:15px; color:black'>{member['name']}</div>", unsafe_allow_html=True)

# ==== Spacing ====
st.markdown("<div class='row-spacing'></div>", unsafe_allow_html=True)

# ==== Bottom row (3 people centered) ====
bottom_row = team_members[4:]
cols_bot = st.columns([1, 3, 3, 3, 1])  # center 3 members
for i, member in enumerate(bottom_row):
    with cols_bot[i + 1]:
        st.image(member["image"], width=300)
        st.markdown(f"<div style='text-align:center; font-weight:bold; font-size:15px; color:black'>{member['name']}</div>", unsafe_allow_html=True)
