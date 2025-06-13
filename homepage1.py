import streamlit as st
from PIL import Image
import base64
from io import BytesIO

st.set_page_config(page_title="Education Career App", layout="wide")

# ==== Tiêu đề ====
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

# ==== Hàm chuyển ảnh sang base64 và bo tròn ====
def image_to_base64_circle(image_path, size=(150, 150)):
    img = Image.open(image_path).convert("RGBA").resize(size)
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)
    output = Image.new("RGBA", size)
    output.paste(img, (0, 0), mask)
    buffered = BytesIO()
    output.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# ==== CSS Grid + HTML hiển thị ====
html_code = """
<style>
.team-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 30px;
    margin-top: 30px;
}
.member {
    text-align: center;
    width: 150px;
}
.member img {
    border-radius: 50%;
    width: 150px;
    height: 150px;
    object-fit: cover;
    border: 3px solid #ddd;
}
.member-name {
    margin-top: 10px;
    font-weight: bold;
}
</style>
<div class="team-grid">
"""

# ==== Thêm từng thành viên vào HTML ====
for member in team_members:
    img_base64 = image_to_base64_circle(member["image"])
    html_code += f"""
    <div class="member">
        <img src="data:image/png;base64,{img_base64}" alt="{member['name']}">
        <div class="member-name">{member['name']}</div>
    </div>
    """

html_code += "</div>"

# ==== Hiển thị lên Streamlit ====
st.markdown(html_code, unsafe_allow_html=True)
