import streamlit as st
from PIL import Image

# ===== PAGE CONFIG =====
st.set_page_config(page_title="Education Career App", layout="wide")

# ===== BACKGROUND (TOP SECTION ONLY) =====
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("images/homepage_bg.png");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ===== NAVIGATION BAR =====
st.markdown("""
    <style>
        .navbar {
            display: flex;
            justify-content: center;
            gap: 40px;
            font-size: 18px;
            margin-bottom: 30px;
        }
        .navbar a {
            color: white;
            text-decoration: none;
            font-weight: bold;
        }
    </style>
    <div class="navbar">
        <a href="#home">Homepage</a>
        <a href="#dataset">Dataset Overview</a>
        <a href="#plot">Plot</a>
        <a href="#code">Code</a>
    </div>
""", unsafe_allow_html=True)

# ===== HOMEPAGE SECTION =====
st.markdown('<a name="home"></a>', unsafe_allow_html=True)
st.markdown("""
    <div style="background: rgba(0, 0, 0, 0.5); 
                color: white; 
                text-align: center; 
                padding: 60px 20px; 
                border-radius: 15px;">
        <h1 style="font-size: 64px;">EDUCATION<br>CAREER<br>SUCCESS</h1>
        <br><br>
        <a href="#team">
            <button style="margin: 10px; padding: 12px 24px; font-size: 18px; border-radius: 12px;">Learn about us</button>
        </a>
    </div>
""", unsafe_allow_html=True)

# ===== TEAM SECTION =====
st.markdown('<a name="team"></a>', unsafe_allow_html=True)

# ===== TEAM BACKGROUND (start from Our Team downward) =====
st.markdown("""
    <style>
    .team-section {
        background: url("images/team_section_bg.png");
        background-size: cover;
        background-position: center;
        padding: 60px 20px;
        border-radius: 0px;
        color: white;
    }
    .team-member-name {
        text-align: center;
        font-weight: bold;
        margin-top: 10px;
    }
    </style>
    <div class="team-section">
""", unsafe_allow_html=True)

st.markdown("### Our Team")

# ===== TEAM MEMBERS (keep original filenames) =====
team_members = [
    {"name": "Kiều Anh", "image": "images/Nguyễn Kiều Anh.png"},
    {"name": "Khánh Phương", "image": "images/Lê Nguyễn Khánh Phương.png"},
    {"name": "Bảo Ngọc", "image": "images/Nguyễn Bảo Ngọc.png"},
    {"name": "Khánh Linh", "image": "images/Nguyễn Trần Khánh Linh.png"},
    {"name": "Bảo Nguyên", "image": "images/Nguyễn Huỳnh Bảo Nguyên.png"},
    {"name": "Thu Thảo", "image": "images/Vũ Thị Thu Thảo.png"},
    {"name": "Sazahng", "image": "images/Sazahng.png"},
]

# ===== PAGINATION (3 per page) =====
if "team_page" not in st.session_state:
    st.session_state.team_page = 1

def show_team(page):
    per_page = 3
    start = (page - 1) * per_page
    end = start + per_page
    members = team_members[start:end]

    cols = st.columns(3)
    for col, member in zip(cols, members):
        with col:
            try:
                img = Image.open(member["image"])
                st.image(img, width=200)  # square image
            except:
                st.warning(f"Không tìm thấy ảnh: {member['image']}")
            st.markdown(f"<div class='team-member-name'>{member['name']}</div>", unsafe_allow_html=True)

    # Pagination buttons
    col1, col2, col3 = st.columns([1, 8, 1])
    with col1:
        if page > 1:
            if st.button("⬅️", key="prev"):
                st.session_state.team_page -= 1
    with col3:
        if end < len(team_members):
            if st.button("➡️", key="next"):
                st.session_state.team_page += 1

show_team(st.session_state.team_page)

# ===== CLOSE team-section DIV =====
st.markdown("</div>", unsafe_allow_html=True)
