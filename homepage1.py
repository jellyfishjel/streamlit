import streamlit as st
from PIL import Image



# ==== Page Config ====
st.set_page_config(
    page_title="Education Career App",
    layout="wide"
)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style/style.css")

# ==== Import font ====
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Bungee&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)


# ==== Global CSS ====
st.markdown("""
     <style>
        .homepage {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 20px 20px 30px;
        }

        .homepage h1 {
            font-family: 'Bungee', sans-serif;
            font-size: 60px;
            color: #cf5a2e;
            line-height: 1.0;
            margin-bottom: 0px;
        }

        .team-title {
            text-align: center;
            font-size: 36px;
            font-family: 'Bungee', sans-serif;
            color: black;
            margin-bottom: 3rem;
            margin-top: 3rem;
        }
     </style>
""", unsafe_allow_html=True)


st.markdown("""
    <div class="homepage">
        <h1>EDUCATION<br>CAREER<br>SUCCESS</h1>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="fade-in" style="text-align: center; max-width: 900px; margin: auto; padding-top: 10px;">
        <p style="font-size: 20px; color: #444;">
            This project explores the connection between <b>education background</b> and <b>career success</b> through an interactive data dashboard.
        </p>
        <p style="font-size: 18px; color: #666;">
            Our goal is to help students and young professionals understand how factors like <i>degree level, age, and job position</i> may impact their career trajectory — all visualized through clean, user-friendly graphs.
        </p>
        <p style="font-size: 17px; color: #666;">
            Developed using <b>Python, Streamlit, and Plotly</b> by <b style="color: #cf5a2e;">Team Py7on</b> as part of the <i>Python Project 2</i> for <b>Business IT 2</b> course at <b>Vietnamese–German University</b>.
        </p>
    </div>
""", unsafe_allow_html=True)



# ==== OUR TEAM section ====
st.markdown('<a name="team"></a>', unsafe_allow_html=True)
st.markdown('<div class="team-title">OUR TEAM</div>', unsafe_allow_html=True)


# ==== Danh sách thành viên ====
team_members = [
    {"name": "Nguyễn Kiều Anh", "image": "image/Nguyen Kieu Anh.png"},
    {"name": "Lê Nguyễn Khánh Phương", "image": "image/Le Nguyen Khanh Phuong.png"},
    {"name": "Nguyễn Bảo Ngọc", "image": "image/Nguyen Bao Ngoc.png"},
    {"name": "Nguyễn Trần Khánh Linh", "image": "image/Nguyen Tran Khanh Linh.png"},
    {"name": "Nguyễn Huỳnh Bảo Nguyên", "image": "image/Nguyen Huynh Bao Nguyen.png"},
    {"name": "Vũ Thị Thu Thảo", "image": "image/Vu Thi Thu Thao.png"},
    {"name": "Nguyễn Bội Ngọc", "image": "image/Nguyen Boi Ngoc.png"},
]

# ==== Top row ====
top_row = team_members[:4]
cols_top = st.columns(len(top_row))
for col, member in zip(cols_top, top_row):
    with col:
        st.image(member["image"], width=250)
        st.markdown( f"<div style='text-align:center; font-weight:bold; font-size:15px; color:black'>{member['name']}</div>", unsafe_allow_html=True)

# ==== Spacing ====
st.markdown("<div class='row-spacing'></div>", unsafe_allow_html=True)

# ==== Bottom row (3 people centered) ====
bottom_row = team_members[4:]
cols_bot = st.columns([1, 3, 3, 3, 1])  # center 3 members
for i, member in enumerate(bottom_row):
    with cols_bot[i + 1]:
        st.image(member["image"], width=300)
        st.markdown(f"<div style='text-align:center; font-weight:bold; font-size:15px; color:black'>{member['name']}</div>", unsafe_allow_html=True)
