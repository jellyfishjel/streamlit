import streamlit as st
import os

# Cấu hình trang
st.set_page_config(page_title="Learn About Us", layout="wide")

st.markdown("<h2 style='text-align: center;'>Our Team ⭐</h2>", unsafe_allow_html=True)

# Thư mục chứa ảnh thành viên
team_folder = "images"
team_members = [
    {"name": "Nguyễn Kiều Anh", "image": "images/Nguyễn Kiều Anh.png"},
    {"name": "Lê Nguyễn Khánh Phương", "image": "images/Lê Nguyễn Khánh Phương.png"},
    {"name": "Nguyễn Bảo Ngọc", "image": "images/Nguyễn Bảo Ngọc.png"},
    {"name": "Nguyễn Trần Khánh Linh", "image": "images/Nguyễn Trần Khánh Linh.png"},
    {"name": "Nguyễn Huỳnh Bảo Nguyên", "image": "images/Nguyễn Huỳnh Bảo Nguyên.png"},
    {"name": "Vũ Thị Thu Thảo", "image": "images/Vũ Thị Thu Thảo.png"},
    {"name": "Sazahng", "image": "images/Sazahng.png"},
]

# Hiển thị ảnh và tên thành viên
cols = st.columns(4)
for index, member in enumerate(team_members):
    with cols[index % 4]:
        img_path = os.path.join(team_folder, member["file"])
        st.image(img_path, width=160)
        st.markdown(f"<p style='text-align: center'><strong>{member['name']}</strong></p>", unsafe_allow_html=True)

