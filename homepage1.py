import streamlit as st
import base64
import os

# ✅ PHẢI đặt dòng này trước bất kỳ Streamlit command nào
st.set_page_config(
    page_title="Education Career App",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==== Load external CSS ====
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ==== Import font ====
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Bungee&display=swap" rel="stylesheet">
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
