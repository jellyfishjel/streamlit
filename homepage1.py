import streamlit as st
import base64

# ==== Hàm mã hóa ảnh thành base64 để nhúng vào HTML ====
def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ==== Cấu hình trang ====
st.set_page_config(page_title="Education Career App", layout="wide")

# ==== CSS đơn giản ====
st.markdown(f"""
    <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bg_image}");
            background-size: cover;
            background-position: center;
        }}
        .title {{
            text-align: center;
            font-size: 50px;
            font-weight: bold;
            color: #cf5a2e;
            margin-top: 80px;
            margin-bottom: 40px;
        }}
        .member-name {{
            text-align: center;
            margin-top: 10px;
            font-weight: bold;
            color: black;
        }}
    </style>
""", unsafe_allow_html=True)

# ==== Tiêu đề ====
st.markdown("<div class='title'>EDUCATION<br>CAREER<br>SUCCESS</div>", unsafe_allow_html=True)

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

# ==== Hiển thị thành viên (chia làm 2 hàng) ====
top_row = team_members[:4]
bottom_row = team_members[4:]

for row in [top_row, bottom_row]:
    cols = st.columns(len(row))
    for col, member in zip(cols, row):
        with col:
            image_base64 = get_base64_image(member["image"])
            st.markdown(f"""
                <div style='text-align: center;'>
                    <img src='data:image/png;base64,{image_base64}' width='180'/>
                    <div class='member-name'>{member["name"]}</div>
                </div>
            """, unsafe_allow_html=True)
