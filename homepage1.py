import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Education Career App", layout="wide")
# === Load CSS ===
def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style/style.css")

# === Title ===
st.title("🎓 EDUCATION CAREER SUCCESS")
st.subheader("Meet Our Amazing Team")


# === Danh sách thành viên ===
team_members = [
    {"name": "Nguyễn Kiều Anh", "image": "images/Nguyen Kieu Anh.png"},
    {"name": "Lê Nguyễn Khánh Phương", "image": "images/Le Nguyen Khanh Phuong.png"},
    {"name": "Nguyễn Bảo Ngọc", "image": "images/Nguyen Bao Ngoc.png"},
    {"name": "Nguyễn Trần Khánh Linh", "image": "images/Nguyen Tran Khanh Linh.png"},
    {"name": "Nguyễn Huỳnh Bảo Nguyên", "image": "images/Nguyen Huynh Bao Nguyen.png"},
    {"name": "Vũ Thị Thu Thảo", "image": "images/Vu Thi Thu Thao.png"},
    {"name": "Nguyễn Bội Ngọc", "image": "images/Nguyen Boi Ngoc.png"},
]

def show_members(members):
    cols = st.columns(len(members))
    for col, member in zip(cols, members):
        with col:
            if os.path.exists(member["image"]):
                st.markdown(
                    f"""
                    <div class='member-container'>
                        <img src="data:image/png;base64,{image_to_base64(member['image'])}" class="member-img"/>
                        <div class="member-name">{member['name']}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.error(f"Không tìm thấy ảnh: {member['image']}")

# Helper: convert ảnh sang base64
import base64
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# === Gọi hàm hiển thị ===
show_members(team_members[:4])
st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
show_members(team_members[4:])
