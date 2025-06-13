import streamlit as st
from PIL import Image

st.set_page_config(page_title="Education Career App", layout="wide")

# === Load CSS nếu có ===
def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style/style.css")

# === Tiêu đề chính ===
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

# === Hiển thị thành viên hàng đầu (dàn đều) ===
def show_members(members, size=300):
    cols = st.columns(len(members))
    for col, member in zip(cols, members):
        with col:
            try:
                img = Image.open(member["image"]).resize((size, size))
                st.image(img, caption=member["name"])
            except FileNotFoundError:
                st.error(f"Không tìm thấy ảnh: {member['image']}")

# === Hiển thị thành viên canh giữa (có thêm cột trống) ===
def show_members_centered(members, size=250):
    # Tỷ lệ: cột trống - ảnh - ảnh - ảnh - cột trống
    cols = st.columns([1, 3, 3, 3, 1])
    for i, member in enumerate(members):
        with cols[i + 1]:  # bỏ cột đầu
            try:
                img = Image.open(member["image"]).resize((size, size))
                st.image(img, caption=member["name"])
            except FileNotFoundError:
                st.error(f"Không tìm thấy ảnh: {member['image']}")

# === Hiển thị hai hàng ===
show_members(team_members[:4], size=300)
st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
show_members_centered(team_members[4:], size=300)
