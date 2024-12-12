"""
Manim 示例页面
"""
import streamlit as st
from src.components.manim_demo import ManimDemo

def render_manim_page():
    """渲染 Manim 示例页面"""
    st.title("数学动画演示")
    
    # 创建选项卡
    tab1, tab2 = st.tabs(["函数可视化", "几何变换"])
    
    # 实例化 Manim 演示类
    manim_demo = ManimDemo()
    
    # 函数可视化选项卡
    with tab1:
        st.header("函数可视化")
        func_type = st.selectbox(
            "选择函数类型",
            ["sin", "quadratic", "exponential"],
            format_func=lambda x: {
                "sin": "正弦函数",
                "quadratic": "二次函数",
                "exponential": "指数函数"
            }[x]
        )
        
        if st.button("生成函数动画"):
            with st.spinner("正在生成动画..."):
                manim_demo.show_function_animation(func_type)
    
    # 几何变换选项卡
    with tab2:
        st.header("几何变换")
        shape_type = st.selectbox(
            "选择几何形状",
            ["square", "circle", "triangle"],
            format_func=lambda x: {
                "square": "正方形",
                "circle": "圆形",
                "triangle": "三角形"
            }[x]
        )
        
        if st.button("生成几何动画"):
            with st.spinner("正在生成动画..."):
                manim_demo.show_geometry_animation(shape_type)
