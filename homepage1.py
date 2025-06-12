import streamlit as st
from PIL import Image

# ==== Page Config ====
st.set_page_config(page_title="Education Career App", layout="wide")

# ==== Title ====
st.title("EDUCATION CAREER SUCCESS 🎓")
st.subheader("Meet Our Amazing Team")

# ==== Danh sách thành viên ====
team_members = [
    {"name": "Nguyễn Kiều Anh", "image": "images/Nguyen Kieu Anh.png"},
    {"name": "Lê Nguyễn Khánh Phương", "image": "images/Le Nguyen Khánh Phương.png"},
    {"name": "Nguyễn Bảo Ngọc", "image": "images/Nguyễn Bảo Ngọc.png"},
    {"name": "Nguyễn Trần Khánh Linh", "image": "images/Nguyễn Trần Khánh Linh.png"},
    {"name": "Nguyễn Huỳnh Bảo Nguyên", "image": "images/Nguyễn Huỳnh Bảo Nguyên.png"},
    {"name": "Vũ Thị Thu Thảo", "image": "images/Vũ Thị Thu Thảo.png"},
    {"name": "Nguyễn Bội Ngọc", "image": "images/Nguyễn Bội Ngọc.png"},
]

# ==== Chia 2 hàng ====
top_row = team_members[:4]
bottom_row = team_members[4:]

# ==== Hàm hiển thị 1 hàng thành viên ====
def display_team_row(members):
    cols = st.columns(len(members))
    for col, member in zip(cols, members):
        with col:
            img = Image.open(member["image"]).resize((250, 250))  # resize ảnh cho đồng đều
            st.image(img, use_container_width=True)
            st.markdown(
                f"<div style='text-align:center; font-weight:bold; margin-top:8px'>{member['name']}</div>",
                unsafe_allow_html=True
            )

# ==== Hiển thị từng hàng ====
st.markdown("## 👩‍💻 Our Team Members")

display_team_row(top_row)
st.markdown("<br>", unsafe_allow_html=True)  # khoảng cách giữa hai hàng
display_team_row(bottom_row)
