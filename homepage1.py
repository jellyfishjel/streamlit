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
    <link href="https://fonts.googleapis.com/css2?family=Bungee&family=Poppins:wght@400;600&display=swap" rel="stylesheet">
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
            padding: 80px 20px 40px;
        }

        .homepage h1 {
            font-family: 'Bungee', sans-serif;
            font-size: 64px;
            color: #cf5a2e;
            line-height: 1.2;
            margin-bottom: 10px;
        }

        .intro-box {
            max-width: 900px;
            margin: 0 auto;
            font-size: 18px;
            line-height: 1.6;
            color: #333;
            padding: 0 20px;
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

# ==== Main title ====
st.markdown("""
    <div class="homepage">
        <h1>EDUCATION<br>CAREER<br>SUCCESS</h1>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="padding: 2rem 2rem 3rem; background: linear-gradient(135deg, #ffe9d6, #fbe3e3); border-radius: 20px; box-shadow: 0 8px 16px rgba(0,0,0,0.1); text-align: center;">
    
    <h2 style="font-family:'Bungee', sans-serif; font-size: 36px; color: #cf5a2e; margin-bottom: 1rem;">
        🎓 How does education shape your future? <br>📊 Let the data tell the story!
    </h2>

    <p style="font-size: 18px; max-width: 850px; margin: 0 auto; color: #333;">
        <strong>Education Career App</strong> is an interactive platform that helps you explore the relationship between <strong>education</strong> and <strong>career success</strong>. Through stunning visualizations and data-driven insights, you'll be able to:
    </p>

    <ul style="text-align: left; max-width: 600px; margin: 2rem auto; font-size: 17px;">
        <li>🔍 Understand key factors that influence your career path</li>
        <li>📚 Compare trends across different education levels</li>
        <li>🚀 Make smarter, data-driven career decisions</li>
    </ul>

    <p style="font-size: 17px; color: #333;">
        This interactive web app is a student project by <strong>Team</strong>, developed as part of the <em>Business IT2</em> course at <strong>Vietnamese–German University (VGU)</strong>.
    </p>

    <a href="#chart" style="margin-top: 2rem; display: inline-block; background-color: #cf5a2e; color: white; padding: 12px 28px; border-radius: 30px; font-weight: bold; text-decoration: none; font-size: 16px;">
        🚀 Explore Now
    </a>

</div>
""", unsafe_allow_html=True)


# ==== Optional: Button dẫn đến phân tích ====
st.markdown("<br>", unsafe_allow_html=True)
if st.button("🚀 Khám phá ngay"):
    st.switch_page("pages/charts.py")  # đảm bảo file này tồn tại trong folder "pages/"

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
        st.markdown(f"<div style='text-align:center; font-weight:bold; font-size:15px; color:black'>{member['name']}</div>", unsafe_allow_html=True)

# ==== Spacing ====
st.markdown("<div class='row-spacing'></div>", unsafe_allow_html=True)

# ==== Bottom row ====
bottom_row = team_members[4:]
cols_bot = st.columns([1, 3, 3, 3, 1])
for i, member in enumerate(bottom_row):
    with cols_bot[i + 1]:
        st.image(member["image"], width=300)
        st.markdown(f"<div style='text-align:center; font-weight:bold; font-size:15px; color:black'>{member['name']}</div>", unsafe_allow_html=True)
