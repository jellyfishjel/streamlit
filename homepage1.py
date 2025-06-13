import streamlit as st
from PIL import Image, ImageDraw

st.set_page_config(page_title="Education Career App", layout="wide")

# ==== Hàm xử lý hình tròn và resize đồng đều ====
def crop_circle(image_path, size=(150, 150)):
    img = Image.open(image_path).convert("RGBA").resize(size)

    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)

    output = Image.new("RGBA", size)
    output.paste(img, (0, 0), mask)
    return output

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

# ==== Hiển thị tiêu đề ====
st.title("EDUCATION CAREER SUCCESS 🎓")
st.subheader("Our amazing team behind the project")

# ==== Chia nhóm thành viên thành từng dòng 3 người ====
n_cols = 3
rows = [team_members[i:i+n_cols] for i in range(0, len(team_members), n_cols)]

for row in rows:
    cols = st.columns(n_cols)
    for col, member in zip(cols, row):
        with col:
            circled_img = crop_circle(member["image"])
            st.image(circled_img)
            st.markdown(
                f"<div style='text-align: center; font-weight: bold'>{member['name']}</div>",
                unsafe_allow_html=True
            )
