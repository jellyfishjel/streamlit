import streamlit as st
from PIL import Image
import base64

st.set_page_config(page_title="Education Career App", layout="wide")

# ========== Helper: Convert image to base64 ==========
def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ========== Background images ==========
home_bg = get_base64("images/homepage_bg.png")
team_bg = get_base64("images/team_section_bg.png")

# ========== CSS ==========
st.markdown(f"""
    <style>
    .homepage-wrapper {{
        background-image: url("data:image/png;base64,{home_bg}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        padding: 80px 20px;
    }}

    .team-section {{
        background-image: url("data:image/png;base64,{team_bg}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        padding: 80px 40px;
        margin-top: 30px;
    }}

    .navbar {{
        display: flex;
        justify-content: center;
        gap: 40px;
        font-size: 18px;
        margin-bottom: 30px;
    }}
    .navbar a {{
        color: white;
        text-decoration: none;
        font-weight: bold;
    }}

    .homepage-box {{
        background: rgba(0, 0, 0, 0.5);
        color: white;
        text-align: center;
        padding: 60px 20px;
        border-radius: 15px;
    }}
    .homepage-box h1 {{
        font-size: 64px;
    }}
    .homepage-box button {{
        margin: 10px;
        padding: 12px 24px;
        font-size: 18px;
        border-radius: 12px;
        cursor: pointer;
    }}

    .team-img {{
        width: 200px;
        height: 200px;
        object-fit: cover;
        border-radius: 10px;
        display: block;
        margin-left: auto;
        margin-right: auto;
        border: 3px solid white;
    }}
    .team-name {{
        text-align: center;
        font-weight: bold;
        color: white;
        margin-top: 8px;
        font-size: 16px;
    }}

    .pagination {{
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }}
    </style>
""", unsafe_allow_html=True)

# ========== Navigation ==========
st.markdown("""
    <div class="navbar">
        <a href="#home">Homepage</a>
        <a href="#dataset">Dataset Overview</a>
        <a href="#plot">Plot</a>
        <a href="#code">Code</a>
    </div>
""", unsafe_allow_html=True)

# ========== Homepage ==========
st.markdown('<a name="home"></a>', unsafe_allow_html=True)
st.markdown(f"""
    <div class="homepage-wrapper">
        <div class="homepage-box">
            <h1>EDUCATION<br>CAREER<br>SUCCESS</h1>
            <br><br>
            <a href="#team">
                <button>Learn about us</button>
            </a>
        </div>
    </div>
""", unsafe_allow_html=True)

# ========== Team Data ==========
team_members = [
    {"name": "Kiều Anh", "image": "images/Nguyễn Kiều Anh.png"},
    {"name": "Khánh Phương", "image": "images/Lê Nguyễn Khánh Phương.png"},
    {"name": "Bảo Ngọc", "image": "images/Nguyễn Bảo Ngọc.png"},
    {"name": "Khánh Linh", "image": "images/Nguyễn Trần Khánh Linh.png"},
    {"name": "Bảo Nguyên", "image": "images/Nguyễn Huỳnh Bảo Nguyên.png"},
    {"name": "Thu Thảo", "image": "images/Vũ Thị Thu Thảo.png"},
]

# ========== Pagination ==========
if "team_page" not in st.session_state:
    st.session_state.team_page = 1

members_per_page = 3
total_pages = (len(team_members) + members_per_page - 1) // members_per_page

# ========== Team Section ==========
st.markdown('<a name="team"></a>', unsafe_allow_html=True)
st.markdown('<div class="team-section">', unsafe_allow_html=True)
st.subheader("Our Team", anchor=False)

def show_team(page):
    start = (page - 1) * members_per_page
    end = start + members_per_page
    members = team_members[start:end]

    cols = st.columns(len(members))
    for col, member in zip(cols, members):
        with col:
            try:
                with open(member["image"], "rb") as f:
                    img_data = base64.b64encode(f.read()).decode()
                st.markdown(
                    f'<img class="team-img" src="data:image/png;base64,{img_data}"/>',
                    unsafe_allow_html=True,
                )
            except FileNotFoundError:
                st.warning(f"Không tìm thấy ảnh: {member['image']}")
            st.markdown(f'<div class="team-name">{member["name"]}</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 9])
    with col1:
        if page > 1 and st.button("⬅️", key="prev"):
            st.session_state.team_page -= 1
    with col2:
        if page < total_pages and st.button("➡️", key="next"):
            st.session_state.team_page += 1

show_team(st.session_state.team_page)
st.markdown('</div>', unsafe_allow_html=True)
