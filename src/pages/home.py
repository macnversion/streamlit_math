import streamlit as st
from src.utils.page_config import get_page_id_by_display_name, get_page_handler

def show_home_page():
    """显示主页内容"""
    st.markdown("""
    # 欢迎来到初等数学知识库 📐
    
    这是一个交互式的数学学习平台，我们将通过可视化和互动的方式来探索数学概念。
    
    ## 主要内容
    """)
    
    # 创建三列布局
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🔷 几何")
        if st.button("多边形探索", use_container_width=True):
            page_id = get_page_id_by_display_name("几何/多边形")
            if page_id:
                get_page_handler(page_id)()
        
        if st.button("圆与圆周率", use_container_width=True):
            page_id = get_page_id_by_display_name("几何/圆")
            if page_id:
                get_page_handler(page_id)()
                
        if st.button("长方体", use_container_width=True):
            page_id = get_page_id_by_display_name("几何/长方体")
            if page_id:
                get_page_handler(page_id)()
    
    with col2:
        st.markdown("### 🔶 代数")
        st.markdown("""
        - 基础代数概念
        - 方程与不等式
        - 函数与图像
        """)
    
    with col3:
        st.markdown("### 🔺 算术")
        st.markdown("""
        - 数系与运算
        - 比例与百分比
        - 数列与级数
        """)
    
    st.markdown("""
    ## 开始探索
    
    你可以：
    1. 在左侧边栏选择一个主题
    2. 或点击上面的按钮
    开始你的数学探索之旅！
    """)