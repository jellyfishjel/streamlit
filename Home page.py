# ... [giữ nguyên phần đầu]

# ========== Background images ==========
home_bg = get_base64("images/homepage_bg.png")
team_bg = get_base64("images/white_texture.png")  # đổi tên ảnh vừa upload

# ========== CSS ==========
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{home_bg}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
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
    .team-section {{
        background-image: url("data:image/png;base64,{team_bg}");
        background-size: cover;
        background-position: center;
        padding: 50px 20px;
        border-radius: 0px;
        margin-top: 30px;
    }}
    .team-img {{
        width: 200px;
        height: 200px;
        object-fit: cover;
        border-radius: 10px;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }}
    .team-name {{
        text-align: center;
        font-weight: bold;
        color: black;
        margin-top: 8px;
        font-size: 16px;
    }}
    </style>
""", unsafe_allow_html=True)

# ... [giữ nguyên phần còn lại như team member list, team section, v.v.]
