import streamlit as st

st.set_page_config(page_title="Education Career App", layout="wide")
def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

# Load CSS
local_css("style/style.css")



# ==== Page title ====
st.title("👩‍💻 Our Team")

# ==== Danh sách thành viên ====
team_members = [
    {"name": "Nguyễn Kiều Anh", "image": "images/Nguyen Kieu Anh.png"},
    {"name": "Lê Nguyễn Khánh Phương", "image": "images/Le Nguyen Khanh Phuong.png"},
    {"name": "Nguyễn Bảo Ngọc", "image": "images/Nguyen Bao Ngoc.png"},
    {"name": "Nguyễn Trần Khánh Linh", "image": "images/Nguyen Tran Khánh Linh.png"},
    {"name": "Nguyễn Huỳnh Bảo Nguyên", "image": "images/Nguyễn Huynh Bảo Nguyên.png"},
    {"name": "Vũ Thị Thu Thảo", "image": "images/Vu Thi Thu Thao.png"},
    {"name": "Nguyễn Bội Ngọc", "image": "images/Nguyễn Bội Ngọc.png"},
]

# ==== Chia thành 2 hàng ====
top_row = team_members[:4]
bottom_row = team_members[4:]

def render_row(members):
    cols = st.columns(len(members))
    for col, member in zip(cols, members):
        with col:
            st.image(member["image"], width=180)
            st.markdown(f"<div style='text-align:center; font-weight:bold; font-size:16px'>{member['name']}</div>", unsafe_allow_html=True)

render_row(top_row)
st.markdown("<div style='margin-top:30px;'></div>", unsafe_allow_html=True)
render_row(bottom_row)
