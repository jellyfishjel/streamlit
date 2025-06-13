import streamlit as st
from PIL import Image, ImageOps
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


def make_circle(img, size=(300, 300)):
    # Cắt ảnh vuông từ trung tâm
    img = ImageOps.fit(img, size, method=Image.Resampling.LANCZOS)
    
    # Tạo mask hình tròn
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)
    
    # Áp mask lên ảnh
    result = Image.new("RGBA", size)
    result.paste(img, (0, 0), mask)
    return result

def show_members(members):
    cols = st.columns(len(members))
    for col, member in zip(cols, members):
        with col:
            try:
                img = Image.open(member["image"]).convert("RGBA")
                circ_img = make_circle(img)
                st.image(circ_img, caption=member["name"], use_container_width=False)
            except FileNotFoundError:
                st.error(f"Không tìm thấy ảnh: {member['image']}")

# Hiển thị 2 hàng
show_members(team_members[:4])
st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
show_members(team_members[4:])
