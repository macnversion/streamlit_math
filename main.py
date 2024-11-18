# main.py

import streamlit as st

# 设置应用标题
st.title("Mathematics Knowledge App")

# 创建页面导航
page = st.sidebar.selectbox("Select a page", ["Home", "Draw a Regular n-gon"])

# 根据选择的页面显示内容
if page == "Home":
    st.write("Welcome to the Mathematics Knowledge App! Please select a page from the sidebar.")
elif page == "Draw a Regular n-gon":
    from pages.page1 import draw_polygon  # 导入绘制正n边形的功能
    draw_polygon()  # 调用绘制函数