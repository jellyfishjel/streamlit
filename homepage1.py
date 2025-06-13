import streamlit as st
from PIL import Image

st.set_page_config(page_title="Education Career App", layout="wide")
def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

# Load CSS
local_css("style/style.css")



st.title("🎓 Our Amazing Team")

# Load images
img_1 = Image.open("images/Nguyen Kieu Anh.png")
img_2 = Image.open("images/Le Nguyen Khanh Phuong.png")
img_3 = Image.open("images/Nguyen Bao Ngoc.png")

col1, col2, col3 = st.columns(3)

with col1:
    st.image(img_1, width=180)
    st.markdown('<div class="member-name">Nguyễn Kiều Anh</div>', unsafe_allow_html=True)

with col2:
    st.image(img_2, width=180)
    st.markdown('<div class="member-name">Lê Nguyễn Khánh Phương</div>', unsafe_allow_html=True)

with col3:
    st.image(img_3, width=180)
    st.markdown('<div class="member-name">Nguyễn Bảo Ngọc</div>', unsafe_allow_html=True)
