import streamlit as st
from PIL import Image, ImageDraw

# ==== Page Config ====
st.set_page_config(page_title="Education Career App", layout="wide")

# ==== Hàm cắt hình tròn ====
def crop_circle(image_path, size=(200, 200)):
    img = Image.open(image_path).convert("RGBA").resize(size)

    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)

    output = Image.new("RGBA", size)
    output.paste(img, (0, 0), mask)
    return output

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

# ==== Chia thành 2 hàng: 4 trên, 3 dưới ====
top_row = team_members[:4]
bottom_row = team_members[4:]

# ==== Hiển thị hàng đầu ====
st.markdown("## 👩‍💻 Team Members")

cols_top = st.columns(len(top_row))
for col, member in zip(cols_top, top_row):
    with col:
        circled_img = crop_circle(member["image"])
        st.image(circled_img, use_column_width=True)
        st.markdown(
            f"<div style='text-align: center; font-weight: bold; margin-top: 8px'>{member['name']}</div>",
            unsafe_allow_html=True
        )

# ==== Hàng thứ 2 ====
st.write("")
cols_bottom = st.columns(len(bottom_row))
for col, member in zip(cols_bottom, bottom_row):
    with col:
        circled_img = crop_circle(member["image"])
        st.image(circled_img, use_column_width=True)
        st.markdown(
            f"<div style='text-align: center; font-weight: bold; margin-top: 8px'>{member['name']}</div>",
            unsafe_allow_html=True
        )
