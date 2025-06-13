import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Education Career App", layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style/style.css")

st.title("🎓 EDUCATION CAREER SUCCESS")
st.subheader("Meet Our Amazing Team")

team_members = [
    {"name": "Nguyễn Kiều Anh", "image": "images/Nguyen Kieu Anh.png"},
    {"name": "Lê Nguyễn Khánh Phương", "image": "images/Le Nguyen Khanh Phuong.png"},
    {"name": "Nguyễn Bảo Ngọc", "image": "images/Nguyen Bao Ngoc.png"},
    {"name": "Nguyễn Trần Khánh Linh", "image": "images/Nguyen Tran Khanh Linh.png"},
    {"name": "Nguyễn Huỳnh Bảo Nguyên", "image": "images/Nguyen Huynh Bao Nguyen.png"},
    {"name": "Vũ Thị Thu Thảo", "image": "images/Vu Thi Thu Thao.png"},
    {"name": "Nguyễn Bội Ngọc", "image": "images/Nguyen Boi Ngoc.png"},
]

def show_members(members, size=300):
    cols = st.columns(len(members))
    for col, member in zip(cols, members):
        with col:
            try:
                img = Image.open(member["image"]).resize((size, size))
                st.image(img, caption=member["name"])
            except FileNotFoundError:
                st.error(f"Không tìm thấy ảnh: {member['image']}")

# Hàng 1: 4 người – ảnh to hơn
show_members(team_members[:4], size=300)

# Khoảng cách giữa hai hàng
st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)

# Hàng 2: 3 người – ảnh nhỏ hơn
show_members(team_members[4:], size=180)
