import streamlit as st

# ===== SETUP PAGE =====
st.set_page_config(layout="wide", page_title="Education & Career Success")

# ===== CSS TO HANDLE 2 BACKGROUNDS =====
st.markdown("""
    <style>
        .homepage {
            background-image: url('images/homepage_bg.png');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            padding: 150px 30px;
            color: #faf4dc;
            text-align: center;
            font-family: 'Bungee', sans-serif;
        }

        .team-section {
            background-image: url('images/team_section_bg.png');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            padding: 100px 50px;
        }

        .team-title {
            text-align: center;
            font-size: 40px;
            color: white;
            margin-bottom: 40px;
            font-weight: bold;
        }

        .member-name {
            text-align: center;
            font-weight: bold;
            color: white;
            margin-top: 10px;
            font-size: 18px;
        }

        .start-btn {
            margin-top: 50px;
        }

        .start-btn button {
            padding: 14px 32px;
            font-size: 18px;
            border-radius: 10px;
            border: none;
            cursor: pointer;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# ===== HOMEPAGE HERO SECTION =====
st.markdown('<div class="homepage">', unsafe_allow_html=True)
st.markdown("<h1 style='font-size:72px;'>EDUCATION<br>CAREER<br>SUCCESS</h1>", unsafe_allow_html=True)
st.markdown("""
    <div class="start-btn">
        <a href="#team-section">
            <button style="background-color: white; color: black;">Let's get started</button>
        </a>
    </div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ===== TEAM SECTION =====
st.markdown('<div class="team-section" id="team-section">', unsafe_allow_html=True)
st.markdown('<div class="team-title">Our Team</div>', unsafe_allow_html=True)

# === TEAM MEMBERS ===
team_members = [
    {"name": "Nguyễn Kiều Anh", "image": "images/Nguyễn Kiều Anh.png"},
    {"name": "Lê Nguyễn Khánh Phương", "image": "images/Lê Nguyễn Khánh Phương.png"},
    {"name": "Nguyễn Bảo Ngọc", "image": "images/Nguyễn Bảo Ngọc.png"},
    {"name": "Nguyễn Trần Khánh Linh", "image": "images/Nguyễn Trần Khánh Linh.png"},
    {"name": "Nguyễn Huỳnh Bảo Nguyên", "image": "images/Nguyễn Huỳnh Bảo Nguyên.png"},
    {"name": "Vũ Thị Thu Thảo", "image": "images/Vũ Thị Thu Thảo.png"},
    {"name": "Sazahng", "image": "images/Sazahng.png"},
]

cols = st.columns(4)
for idx, member in enumerate(team_members):
    col = cols[idx % 4]
    with col:
        st.image(member["image"], use_column_width=True)
        st.markdown(f"<div class='member-name'>{member['name']}</div>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
