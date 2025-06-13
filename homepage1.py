import streamlit as st
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(page_title="Education Career App", layout="wide")

# ==== Hàm chuyển ảnh thành base64 để nhúng vào HTML ====
def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# ==== Danh sách thành viên ====
team_members = [
    {"name": "Nguyễn Kiều Anh", "image": "images/Nguyen Kieu Anh.png"},
    {"name": "Lê Nguyễn Khánh Phương", "image": "images/Le Nguyen Khanh Phuong.png"},
    {"name": "Nguyễn Bảo Ngọc", "image": "images/Nguyen Bao Ngoc.png"},
    {"name": "Nguyễn Trần Khánh Linh", "image": "images/Nguyen Tran Khanh Linh.png"},
    {"name": "Nguyễn Huỳnh Bảo Nguyên", "image": "images/Nguyen Huynh Bao Nguyen.png"},
    {"name": "Vũ Thị Thu Thảo", "image": "images/Vu Thi Thu Thao.png"},
    {"name": "Nguyễn Bội Ngọc", "image": "images/Nguyen Boi Ngoc.png"},
]

# ==== Hàm hiển thị thành viên (theo hàng) ====
def render_row(members):
    cols = st.columns(len(members))
    for col, member in zip(cols, members):
        try:
            img = Image.open(member["image"])
            img_base64 = image_to_base64(img)

            col.markdown(f"""
                <div style='text-align: center;'>
                    <img src='data:image/png;base64,{img_base64}' width='180' style='border-radius: 50%;'><br>
                    <div style='font-weight: bold; font-size: 16px; margin-top: 8px;'>{member['name']}</div>
                </div>
            """, unsafe_allow_html=True)

        except FileNotFoundError:
            col.error(f"Không tìm thấy ảnh: {member['image']}")

# ==== Hiển thị tiêu đề ====
st.title("EDUCATION CAREER SUCCESS 🎓")
st.subheader("Our amazing team behind the project")
st.markdown("## 👩‍💻 Team Members")

# ==== Tách nhóm trên/dưới ====
top_row = team_members[:4]
bottom_row = team_members[4:]

# ==== Hiển thị ====
render_row(top_row)
st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)
render_row(bottom_row)
