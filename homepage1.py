from PIL import Image
import streamlit as st

st.set_page_config(page_title="Education Career App", layout="wide")
def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

# Load CSS
local_css("style/style.css")


# ==== Tiêu đề chính ====
st.title("EDUCATION CAREER SUCCESS 🎓")
st.subheader("Our amazing team behind the project")

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

# ==== Hàm hiển thị 1 hàng ảnh ====
def render_row(members):
    cols = st.columns(len(members))
    for col, member in zip(cols, members):
        with col:
            try:
                img = Image.open(member["image"]).resize((180, 180))
                # Bọc cả hình + tên trong 1 div để căn giữa toàn bộ
                col.markdown(
                    f"""
                    <div style='text-align: center;'>
                        <img src='data:image/png;base64,{image_to_base64(img)}' width='180' style='border-radius: 50%;'><br>
                        <div style='font-weight: bold; font-size: 16px; margin-top: 8px;'>{member['name']}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            except FileNotFoundError:
                st.error(f"Không tìm thấy ảnh: {member['image']}")


# ==== Gọi hàm hiển thị ====
st.markdown("## 👩‍💻 Team Members")
top_row = team_members[:4]
bottom_row = team_members[4:]
