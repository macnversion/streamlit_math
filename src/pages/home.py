import streamlit as st
from src.utils.page_config import get_page_id_by_display_name, get_page_handler
from src.i18n.language_manager import get_text, add_language_selector

def show_home_page():
    """显示主页内容"""
    # 添加语言选择器
    add_language_selector()
    
    st.title(get_text("home_title"))
    st.markdown(get_text("home_welcome"))
    st.markdown(get_text("home_description"))
    
    st.markdown("## " + get_text("geometry_title"))
    
    # 创建三列布局
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### " + get_text("geometry_title"))
        if st.button(get_text("polygons_title"), use_container_width=True):
            page_id = get_page_id_by_display_name("几何/多边形")
            if page_id:
                get_page_handler(page_id)()
        
        if st.button(get_text("circles_title"), use_container_width=True):
            page_id = get_page_id_by_display_name("几何/圆")
            if page_id:
                get_page_handler(page_id)()
                
        if st.button(get_text("cuboid_title"), use_container_width=True):
            page_id = get_page_id_by_display_name("几何/长方体")
            if page_id:
                get_page_handler(page_id)()
    
    with col2:
        st.markdown("### " + get_text("algebra_title"))
        st.markdown("""
        - 基础代数概念
        - 方程与不等式
        - 函数与图像
        """)
    
    with col3:
        st.markdown("### " + get_text("arithmetic_title"))
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