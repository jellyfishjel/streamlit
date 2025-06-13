import streamlit as st
from PIL import Image
import base64
from io import BytesIO

st.set_page_config(page_title="Education Career App", layout="wide")
st.title("EDUCATION CAREER SUCCESS 🎓")
st.subheader("Our amazing team behind the project")

# === Hàm chuyển ảnh thành base64 ===
def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

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

# === Hàm hiển thị thành viên theo hàng ===
def render_row(members):
    cols = st.columns(len(members))
    for col, member in zip(cols, members):
        with col:
            try:
                img = Image.open(member["image"]).resize((180, 180))
                img_base64 = image_to_base64(img)

                st.markdown(f"""
                    <div style="background-color:#fff3e0;
                                padding:20px;
                                border-radius:20px;
                                text-align:center;
                                box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                        <img src="data:image/png;base64,{img_base64}"
                             style="border-radius: 50%; width:180px; height:180px;"><br>
                        <div style="font-weight:bold; font-size:16px; margin-top:10px;">
                            {member['name']}
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            except FileNotFoundError:
                st.error(f"Không tìm thấy ảnh: {member['image']}")

# === Hiển thị 2 hàng ===
top_row = team_members[:4]
bottom_row = team_members[4:]

st.markdown("## 👩‍💻 Team Members")
render_row(top_row)
st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
render_row(bottom_row)
